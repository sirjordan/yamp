import unittest
import dices


class YampDiceTests(unittest.TestCase):
    def test_roll_dices(self):
        _dices = dices.roll_dices()
        self.assertEqual(len(_dices), 5)

    def test_score_matching(self):
        self.assertEqual(dices.score_matching([1, 1, 1, 3, 4], 1), 3)
        self.assertEqual(dices.score_matching([2, 2, 2, 5, 6], 2), 6)
        self.assertEqual(dices.score_matching([3, 3, 3, 3, 4], 3), 12)
        self.assertEqual(dices.score_matching([4, 4, 5, 5, 5], 4), 8)
        self.assertEqual(dices.score_matching([1, 1, 2, 2, 5], 5), 5)
        self.assertEqual(dices.score_matching([1, 3, 6, 6, 6], 6), 18)
        self.assertEqual(dices.score_matching([1, 3, 6, 6, 6], 2), 0)

    def test_score_n_of_a_kind_throw_ex(self):
        args = ([1, 3, 6, 6, 6], 5)
        self.assertRaises(ValueError, dices.score_n_of_a_kind, *args)

    def test_score_n_of_a_kind(self):
        self.assertEqual(dices.score_n_of_a_kind([2, 3, 4, 4, 4], 3), 17)
        self.assertEqual(dices.score_n_of_a_kind([4, 5, 5, 5, 5], 4), 24)
        self.assertEqual(dices.score_n_of_a_kind([1, 2, 3, 4, 5], 4), 0)

    def test_count_n_of_a_kind(self):
        self.assertEqual(dices.count_equal([2, 3, 4, 4, 4], 4), 3)
        self.assertEqual(dices.count_equal([2, 3, 4, 4, 4], 2), 1)
        self.assertEqual(dices.count_equal([2, 3, 4, 4, 4], 6), 0)

    def test_score_full(self):
        self.assertEqual(dices.score_full([2, 2, 5, 5, 5]), 25)
        self.assertEqual(dices.score_full([2, 2, 5, 5, 1]), 0)
        self.assertEqual(dices.score_full([3, 1, 3, 1, 1]), 25)
        self.assertEqual(dices.score_full([1, 2, 3, 4, 5]), 0)
        self.assertEqual(dices.score_full([2, 3, 3, 3, 2]), 25)

if __name__ == '__main__':
    unittest.main()

