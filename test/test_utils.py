from unittest import TestCase
from app.utils.utils import *

class Test(TestCase):
    def test_sum(self):
        assert sum(3,2) == 5

    def test_hw(self):
        assert HW() == "Hello World"

    def test_greater_than(self):
        assert greaterThan(50) is True
        assert greaterThan(7) is False

    def test_smaller_than(self):
        assert smallerThan(50) is False
        assert smallerThan(7) is True
