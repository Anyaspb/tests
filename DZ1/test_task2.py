from unittest import TestCase


from task2 import sorted_list

class TestCase1(TestCase):
    def test_class(self):
        res = sorted_list()
        self.assertIsInstance(res, list)

    def test_qty(self):
        res = len(sorted_list())
        expected_result = 4
        self.assertEqual(res, expected_result)

    def test_regex(self):
        for x in range(4):
            res = sorted_list()[x]
            pattern ="\D{,100} - \d{2} месяцев"
            self.assertRegex(res, pattern)

#pytest
# from task2 import sorted_list
# import re
# import pytest
#
# @pytest.mark.parametrize('x',[0,1,2,3])
#
# def test_regex(x):
#     res = sorted_list()[x]
#     pattern =r"\D{,100} - \d{2} месяцев"
#     check = re.fullmatch(pattern, res) is not None
#     assert check == True