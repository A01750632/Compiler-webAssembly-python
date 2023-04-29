# Author: A01750632 Liam Garay Monroy
from delta import Compiler, Phase

source = '''
    3 + 2 >= 5
'''

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)
