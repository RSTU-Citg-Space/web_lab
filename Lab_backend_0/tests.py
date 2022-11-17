import unittest

import fixtures

try:
    from main import Solution
except ImportError:
    raise AssertionError('Отсутствует класс Solution')


solution = Solution()


class TestSolution(unittest.TestCase):
    def test_all_methods_allowed(self):
        for attrib in fixtures.ATTRIBUTES:
            try:
                attrib = getattr(solution, attrib)
            except AttributeError:
                raise AssertionError(
                    f'Атрибут {attrib} отсутствует у класса Solution'
                )

    @unittest.skip
    def test_sum_number_in_string(self):
        for key, value in fixtures.SUM_STRING_NUMBER.items():
            self.assertEqual(
                solution.sum_number_in_string(key), value,
                'Ваш скрипт работает неверно проверьте всё ещё раз)'
            )

    @unittest.skip
    def test_leader_string(self):
        for key, value in fixtures.LEADERS.items():
            self.assertEqual(
                solution.get_leader_string(key), value,
                'Если вас постигла неудача просто улыбнитесь этому сообщению'
            )

    @unittest.skip
    def test_to_json(self):
        @solution.to_json
        def test_func(data: dict):
            return data

        for string_json, value in fixtures.json_datas.items():
            self.assertEqual(
                test_func(value), string_json,
                'Убедитесь что ваш декоратор работает правильно.'
            )

    @unittest.skip
    def test_get_spiral_numbers(self):
        for key, value in fixtures.SPIRAL_NUMBERS.items():
            matrix = solution.get_spiral_number_matrix(key)
            self.assertIsInstance(matrix, list, 'Метод должен возвращать список')
            result_string = '\n'.join([' '.join(list(map(str, line))) for line in matrix])
            self.assertEqual(result_string, value)


if __name__ == '__main__':
    unittest.main()
