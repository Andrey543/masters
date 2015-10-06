# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_even(self):
        self.assertEqual(lib.even(0),True)
        self.assertEqual(lib.even(-2),True)



# Запускаем тесты на исполнение
unittest.main(verbosity=2)
