from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def new_test(self):
        res = calc.add(6, 5)
        self.assertEqual(res, 11)
