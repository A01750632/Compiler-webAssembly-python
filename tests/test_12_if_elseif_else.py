# File: tests/test_12_if_elseif_else.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestIfElseIfElse(TestCase):

    def setUp(self):
        self.c = Compiler('program_start')

    def test_syntax_mistake1(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('if true {} else if {}')

    def test_if_elseif_else_1(self):
        self.assertEqual(3,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 5;
                            if x - 5 {
                                y = 1;
                            } else if x * 0 {
                                y = 2;
                            } else if x - 1 {
                                y = 3;
                            } else {
                                y = 4;
                            }
                            y
                            '''))

    def test_if_elseif_else_2(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 5;
                            if x - 5 {
                                y = 1;
                            } else if x * 0 {
                                y = 2;
                            } else if x - x {
                                y = 3;
                            } else if x / x - 1 {
                                y = 4;
                            }
                            y
                            '''))

    def test_if_elseif_else_3(self):
        self.assertEqual(5,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 5;
                            if x - 5 {
                                y = 1;
                            } else if x * 0 {
                                y = 2;
                            } else if x - x {
                                y = 3;
                            } else if x / x - 1 {
                                y = 4;
                            } else {
                                y = x;
                            }
                            y
                            '''))

    def test_if_elseif_else_4(self):
        self.assertEqual(1,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 5;
                            if x {
                                y = 1;
                            } else if x * 0 {
                                y = 2;
                            } else if x - x {
                                y = 3;
                            } else if x / x - 1 {
                                y = 4;
                            } else {
                                y = x;
                            }
                            y
                            '''))

    def test_if_elseif_else_5(self):
        self.assertEqual(3,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 5;
                            if x - 5 {
                                y = 1;
                            } else if x * 0 {
                                y = 2;
                            } else if x - 1 {
                                y = 3;
                            } else if x / x - 1 {
                                y = 4;
                            } else {
                                y = x;
                            }
                            y
                            '''))

    def test_if_elseif_else_6(self):
        self.assertEqual(27,
                         self.c.realize(
                            '''
                            var a, b, c;
                            a = 4;
                            b = 2 * a - 5;
                            c = a * b;
                            if a - a {
                                a = a * 2;
                                b = b - 1;
                                c = c + 1;
                            } else if a - b {
                                a = a * 3;
                                b = b - 2;
                                c = c + 2;
                            } else if c + 1 {
                                a = a * 4;
                                b = b - 3;
                                c = c + 3;
                            } else {
                                a = a * 5;
                                b = b - 4;
                                c = c + 4;
                            }
                            a + b + c
                            '''))