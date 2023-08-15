from unittest import TestCase
from task1 import function_min, function_max

class TestCase1(TestCase):
    def test_min(self):
        expected_result = "Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)"
        res = function_min()
        self.assertEqual(res, expected_result)

class TestCase2(TestCase):
    def test_max(self):
        expected_result = "Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)"
        res = function_max()
        self.assertEqual(res, expected_result)

