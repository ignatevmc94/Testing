import unittest

from main import check_month, vote, solution

class TestMain(unittest.TestCase):

    def test_сheck_month(self):
        for i, (month, expected) in enumerate((
                (0, 'Некорректный номер месяца'),
                (20, 'Некорректный номер месяца'),
                (1, 'Зима'),
                (5, 'Весна'),
                (6, 'Лето'),
                (11, 'Осень'),
                (12, 'Зима')
        )):
            with self.subTest(i):
                result = check_month(month)
                self.assertEqual(expected, result, f'Ответ должен быть {expected}')

    def test_votes(self):
        for i, (input_list, expected) in enumerate((
                ([], None),
                ([1,1,1,2,3,4], 1),
                ([1,2,3,1,2,1], 1),
                ([1,2,3,3,4,4,4], 4),
        )):
            with self.subTest(i):
                result = vote(input_list)
                self.assertEqual(result, expected,f'Ответ должен быть {expected}')

    def test_discriminant(self):
        for i, (a,b,c,expected) in enumerate((
                (1, 8, 15, (-3, -5)),
                (1, -13, 12, (12, 1)),
                (-4, 28, -49, 3.5),
                (1, 1, 1, 'корней нет')
        )):
            with self.subTest(i):
                result = solution(a,b,c)
                self.assertEqual(expected, result, f'Ответ должен быть {expected}')

