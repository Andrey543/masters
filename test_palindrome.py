# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_even(self):
        self.assertEqual(lib.palindrome('q'),True)
        self.assertEqual(lib.palindrome('wqw'),True)
        self.assertEqual(lib.palindrome('abbbbcbbbba'),True)
 


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
