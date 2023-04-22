# File: tests/test_C_do_while.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestDoWhile(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('do {} while;')

    def test_semantic_mistake(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var do; 0')

    def test_do_while_zero(self):
        self.assertEqual(1,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 1;
                            y = 0;
                            do {
                                x = x - 1;
                                y = 1;
                            } while x;
                            x + y
                            '''))

    def test_do_while_fact(self):
        self.assertEqual(120,
                         self.c.realize(
                            '''
                            var n, r, i;
                            n = 5;
                            r = 1;
                            i = 0;
                            do {
                                i = i + 1;
                                r = r * i;
                            } while n - i;
                            r
                            '''))

    def test_do_while_count_down(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var i;
                            i = 10;
                            do {
                                i = i - 1;
                            } while i;
                            i
                            '''))

    def test_do_while_skip_body(self):
        self.assertEqual(9,
                         self.c.realize(
                            '''
                            var n;
                            n = 10;
                            do {
                                n = n - 1;
                            } while !n;
                            n
                            '''))

    def test_do_while_fibo(self):
        self.assertEqual(55,
                         self.c.realize(
                            '''
                            var n, a, b;
                            n = 10;
                            a = 0;
                            b = 1;
                            do {
                                var t;
                                t = b;
                                b = a + b;
                                a = t;
                                n = n - 1;
                            } while n;
                            a
                            '''))

    def test_do_while_nested(self):
        self.assertEqual(1500,
                         self.c.realize(
                            '''
                            var r, i;
                            r = 0;
                            i = 10;
                            do {
                                var j;
                                j = 50;
                                do {
                                    var k;
                                    k = 3;
                                    do {
                                        r = r + 1;
                                        k = k - 1;
                                    } while k;
                                    j = j - 1;
                                } while j;
                                i = i - 1;
                            } while i;
                            r
                            '''))