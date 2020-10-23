
import unittest
import my_module
import using_my_module
import math
import random


def fun(x):
    return x + 1


class MyTestClass(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(3), 4)

    def test2(self):
        self.assertAlmostEqual(my_module.my_function(0), 0, "Verkar vara en bugg i my_function...")
        self.assertAlmostEqual(my_module.my_function(math.pi/2), 1 + math.pi * math.pi / 4,
                               "Verkar vara en bugg i my_function...")

    def test_roll_dice(self):
        for i in range(0, 10):
            result = my_module.roll_dice(3)
            self.assertLessEqual(1, result, "Verkar vara en bugg i roll_dice...")
            self.assertLessEqual(result, 18, "Verkar vara en bugg i roll_dice...")

    def test_sort_list(self):
        my_list = []
        for i in range(0, 10):
            my_list.append(random.randint(0, 10))
        my_sorted_list = my_module.my_sort_list(my_list)
        my_list.sort()
        self.assertEqual(my_sorted_list, my_list, "Verkar vara en bugg i my_sort_list...")

    def test_bandit_language(self):
        original_string = "det rockar fett"
        translated_string = "dodetot rorocockokaror fofetottot"
        self.assertEqual(translated_string, my_module.bandit_language(original_string),
                         "Verkar vara en bugg i bandit_language...")

    def test_bandit_animals(self):
        my_dict = using_my_module.make_bandit_dictionary(using_my_module.animals)
        self.assertIn("tiger", my_dict)
        self.assertIn("coclolawowsos", my_dict["tiger"])

if __name__ == '__main__':
    unittest.main()