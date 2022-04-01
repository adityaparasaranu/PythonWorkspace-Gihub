from unittest import TestCase
from app import multiply


class TestFunction(TestCase):
    def test_multiply_function(self):
        self.assertEqual(multiply(10, 2), 21)
