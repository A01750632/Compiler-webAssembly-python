# File: tests/test_A_comparisons.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestComparisons(TestCase):

    def setUp(self):
        self.c = Compiler('expression_start')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('1 <=')

    def test_equal_true(self):
        self.assertEqual(1,
                         self.c.realize('1 + 2 == 3'))

    def test_equal_false(self):
        self.assertEqual(0,
                         self.c.realize('3 + 2 == 4'))

    def test_not_equal_true(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 != 4'))

    def test_not_equal_false(self):
        self.assertEqual(0,
                         self.c.realize('3 + 2 != 5'))

    def test_less_than_true(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 < 6'))

    def test_less_than_false(self):
        self.assertEqual(0,
                         self.c.realize('3 + 2 < 5'))

    def test_greater_than_true(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 > 4'))

    def test_greater_than_false(self):
        self.assertEqual(0,
                         self.c.realize('3 + 2 > 5'))

    def test_less_or_equal_true1(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 <= 5'))

    def test_less_or_equal_true2(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 <= 6'))

    def test_less_or_equal_false(self):
        self.assertEqual(0,
                         self.c.realize('3 + 2 <= 4'))

    def test_greater_or_equal_true1(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 >= 5'))

    def test_greater_or_equal_true2(self):
        self.assertEqual(1,
                         self.c.realize('3 + 2 >= 4'))

    def test_greater_or_equal_false(self):
        self.assertEqual(0,
                         self.c.realize('3 + 2 >= 6'))

    def test_mix_1(self):
        self.assertEqual(1,
                         self.c.realize('1 <= 2 == 1 != '
                                        '0 > 0 < 0 <= 1'))

    def test_mix_2(self):
        self.assertEqual(1,
                         self.c.realize('1 < 2 < 3 < 4'))

    def test_mix_3(self):
        self.assertEqual(1,
                         self.c.realize('(1 >= 2 > 3) == '
                                        '(4 <= 5 < 6) != 1'))