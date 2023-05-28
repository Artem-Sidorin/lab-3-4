import unittest
import calc


class TestMethods(unittest.TestCase):

    def test_diff(self):
        self.assertEqual(calc.diff(1000, 1, 10),
                         [91.67, 90.97, 90.28, 89.58, 88.89, 88.19, 87.5, 86.81, 86.11, 85.42, 84.72,
                          84.03])

    def test_ann_zero(self):
        self.assertEqual(calc.annuity(0, 0), 0)

    def test_diff_zero(self):
        self.assertEqual(calc.diff(1000, 0, 10), [])

    def test_diff_warning(self):
        warning = 'Значения суммы, срока и процентной ставки не может быть меньше 0'
        self.assertEqual(calc.diff_result(-10, -14, 32), (warning, warning, warning))


if __name__ == '__main__':
    unittest.main()
