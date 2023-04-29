# Author: A01750632 Liam Garay Monroy
from arpeggio import PTNodeVisitor


class CodeGenerationVisitor(PTNodeVisitor):

    WAT_TEMPLATE = ''';; Code generated by the Delta compiler
(module
  (func
    (export "_start")
    (result i32)
{}  )
)
'''

    def __init__(self, symbol_table, **kwargs):
        super().__init__(**kwargs)
        self.__symbol_table = symbol_table

    def visit_expression_start(self, node, children):
        return CodeGenerationVisitor.WAT_TEMPLATE.format(children[0])
    
    def visit_expression(self, node, children):
        result = [children[0]]
        for i in range(1, len(children), 2):
            result.append(children[i + 1])
            match children[i]:
                case '>=':
                    result.append('    i32.ge_s\n')
                case '==':
                    result.append('    i32.eq\n')
                case '!=':
                    result.append('    i32.ne\n')
                case '>':
                    result.append('    i32.gt_s\n')
                case '<':
                    result.append('    i32.lt_s\n')
                case '<=':
                    result.append('    i32.le_s\n')
        return ''.join(result)

    def visit_operators(self, node, children):
        result = [children[0]]
        for i in range(1, len(children), 2):
            result.append(children[i + 1])
            match children[i]:
                case '+':
                    result.append('    i32.add\n')
                case '-':
                    result.append('    i32.sub\n')
        return ''.join(result)

    def visit_multiplicative(self, node, children):
        result = [children[0]]
        for i in range(1, len(children), 2):
            result.append(children[i + 1])
            match children[i]:
                case '*':
                    result.append('    i32.mul\n')
                case '/':
                    result.append('    i32.div_s\n')
                case '%':
                    result.append('    i32.rem_s\n')
        return ''.join(result)

    def visit_primary(self, node, children):
        return children[0]

    def visit_decimal(self, node, children):
        return f'    i32.const {node.value}\n'

    def visit_boolean(self, node, children):
        if children[0] == 'true':
            return '    i32.const 1\n'
        return '    i32.const 0\n'

    def visit_parenthesis(self, node, children):
        return children[0]

    def visit_unary(self, node, children):
        result = children[-1]
        for op in children[-2::-1]:
            match op:
                case '+':
                    ...  # do nothing
                case '-':
                    result = (
                        '    i32.const 0\n'
                        + result
                        + '    i32.sub\n'
                    )
                case '!':
                    result += '    i32.eqz\n'
        return result

    def visit_program_start(self, node, children):

        def declare_wat_vars():
            return ''.join([f'    (local ${v} i32)\n'
                            for v in self.__symbol_table])

        return CodeGenerationVisitor.WAT_TEMPLATE.format(
            declare_wat_vars()
            + ''.join(children)
        )

    def visit_statement(self, node, children):
        return children[0]

    def visit_declaration(self, node, children):
        return ''

    def visit_assignment(self, node, children):
        return children[1] + children[0]

    def visit_lhs_variable(self, node, children):
        name = node.value
        return f'    local.set ${name}\n'

    def visit_rhs_variable(self, node, children):
        name = node.value
        return f'    local.get ${name}\n'

    def visit_block(self, node, children):
        return ''.join(children)

    def visit_if(self, node, children):
        result = children[0] + '    if\n' + children[1] + '    else\n'
        if len(children) >3:
            if len(children) % 2 == 0:
                for i in range(2, len(children),2):
                    result += children[i] + '    if\n' + children[i+1]
                    result+= '    else\n'
                result+= '    end\n'*int(((len(children))/2)-1)
            else:
                for i in range(2, len(children)-1,2):
                    result += children[i] + '    if\n' + children[i+1]
                    result+= '    else\n'
                result+= children[-1]
                result+= '    end\n'*int(((len(children)-1)/2)-1)   
        if len(children) == 3:
            result += children[2]
        result += '    end\n'
        return result

    def visit_while(self, node, children):
        return ('    block\n'
                + '    loop\n'
                + children[0]
                + '    i32.eqz\n'
                + '    br_if 1\n'
                + children[1]
                + '    br 0\n'
                + '    end\n'
                + '    end\n')
    
    def visit_do_while(self, node, children):
        return (  '    loop\n'
                + children[0]
                + children[1]
                + '    br_if 0\n'
                + '    end\n')
    
