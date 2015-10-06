# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_palindrome_1(self):
        self.assertEqual(lib.palindrome('q'),True)
    def test_palindrome_2(self):
        self.assertEqual(lib.palindrome('abbbbcbbbba'),True)
    def test_palindrome(self):
        self.assertEqual(lib.palindrome(''),True)
        self.assertEqual(lib.palindrome('1245'),False)
 


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
