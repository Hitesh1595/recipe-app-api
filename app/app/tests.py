"""
Sample test
"""

from django.test import SimpleTestCase
from app import calc


class ClacTests(SimpleTestCase):
    """ Test the cacl module """

    def test_add_numbers(self):
        """ Test adding number together """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """ Test Subtract the number """
        res = calc.subtract(3, 5)
        self.assertEqual(res, 2)
