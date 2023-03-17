"""
Sample Test
"""


from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def add_test(self):
        res = calc.add(6, 5)
        self.assertEqual(res, 11)
