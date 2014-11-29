#!/usr/bin/env python
# -*- coding: utf-8 -*-

import basics

import unittest
import types
import sys
from StringIO import StringIO


class TestBasics(unittest.TestCase):

    # 1
    def test_unique_empty_list(self):
        self.assertEquals(basics.unique([]), [])

    def test_unique_numbers_list(self):
        self.assertEquals(sorted(basics.unique([1, 2, 3])), [1, 2, 3])
        self.assertEquals(sorted(basics.unique([1, 2, 2])), [1, 2])
        self.assertEquals(sorted(basics.unique([1, 1, 1, 1, 1, 1])), [1])
        self.assertEquals(
            sorted(basics.unique([1, 1, 1, 2, 2, 2, 2, 3])),
            [1, 2, 3]
        )
        self.assertEquals(
            sorted(basics.unique([-20, -2.1, 2, 4.12, 2])),
            [-20, -2.1, 2, 4.12]
        )

    # 2
    def test_day_from_int(self):
        self.assertEquals(basics.day_from_int(1), u"Poniedziałek")
        self.assertEquals(basics.day_from_int(4), u"Czwartek")
        self.assertEquals(basics.day_from_int(6), u"Sobota")

    def test_day_from_negative_int(self):
        self.assertEquals(basics.day_from_int(-199), u"")
        self.assertEquals(basics.day_from_int(-9), u"")

    def test_day_from_too_high_int(self):
        self.assertEquals(basics.day_from_int(100), u"")

    # 3
    def test_min_empty_dict_value(self):
        self.assertEquals(basics.min_dict_value({}), None)

    def test_min_dict_value(self):
        self.assertEquals(
            basics.min_dict_value({
                'kot': 1,
                'pies': 23,
                'sowa': 2}),
            1
        )
        self.assertEquals(
            basics.min_dict_value({
                '1': -100,
                '4': 231,
                '231': 23122}),
            -100
        )

    # 4
    def test_power_empty_list(self):
        self.assertEquals(basics.power_list([], 0), [])

    def test_power_list(self):
        self.assertEquals(basics.power_list([1, 2, 3, 4], 0), [1, 1, 1, 1])
        self.assertEquals(basics.power_list([3, 4], 2), [9, 16])
        self.assertEquals(basics.power_list([9, 16], .5), [3, 4])

    # 5
    def test_generator_9_divisible_type(self):
        self.assertEquals(type(basics.nine_divisible(10)), types.GeneratorType)

    def test_generator_9_divisible(self):
        self.assertEquals(list(basics.nine_divisible(10)), [9])
        self.assertEquals(list(basics.nine_divisible(1)), [])
        self.assertEquals(list(basics.nine_divisible(20)), [9, 18])
        self.assertEquals(list(basics.nine_divisible(30)), [9, 18, 27])

    # 6
    def test_is_palindrome(self):
        self.assertEquals(basics.is_palindrome(''), True)
        self.assertEquals(basics.is_palindrome('ab'), False)
        self.assertEquals(basics.is_palindrome('anna'), True)
        self.assertEquals(basics.is_palindrome('ccd'), False)
        self.assertEquals(basics.is_palindrome('ahsatanseesnatasha'), True)
        self.assertEquals(basics.is_palindrome('tenanimalsislaminanet'), True)

    # 7
    def test_fibonacci(self):
        self.assertEquals(basics.fibonacci(1), 1)
        self.assertEquals(basics.fibonacci(5), 5)
        self.assertEquals(basics.fibonacci(100), 354224848179261915075)

    # 8
    def test_sum_args(self):
        self.assertEquals(basics.sum_args(), 0)
        self.assertEquals(basics.sum_args(1, 2), 3)
        self.assertEquals(basics.sum_args(100), 100)
        self.assertEquals(basics.sum_args(-1, 2, 10, 20, 40), 71)
        self.assertEquals(basics.sum_args(1, 1, 1, 1, 1, 1, 1), 7)

    # 9
    def test_higher_than(self):
        self.assertEquals(basics.higher_than([1, 2, 3, 4, 5], 2), [3, 4, 5])
        self.assertEquals(basics.higher_than([3, 23, 1, -2, 5], 3), [23, 5])
        self.assertEquals(basics.higher_than([], 2), [])
        self.assertEquals(basics.higher_than([4, 3, 2, 1], 0), [4, 3, 2, 1])
        self.assertEquals(basics.higher_than([2, 2, 2, 2], 2), [])

    # 10
    def test_quicksort(self):
        self.assertEquals(basics.qsort([]), [])
        self.assertEquals(basics.qsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEquals(basics.qsort([2, 10, 3, 2]), [2, 2, 3, 10])
        self.assertEquals(basics.qsort([-1, 20, 3, 1]), [-1, 1, 3, 20])
        self.assertEquals(basics.qsort([1, 2, 3]), [1, 2, 3])

    # 11
    def test_animal_name(self):
        jacek = basics.Animal("Jacek")
        self.assertEquals(jacek.name, "Jacek")

    def test_dog_name(self):
        reksio = basics.Dog("Reksio")
        self.assertEquals(reksio.name, "Reksio")

    def test_dog_say(self):
        reksio = basics.Dog("Reksio")
        out = StringIO()
        sys.stdout = out
        reksio.say()
        self.assertEquals(out.getvalue().strip(), "Haw Haw")


if __name__ == '__main__':
    unittest.main()
