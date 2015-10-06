# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_sqrt(self):
        self.assertEqual(lib.sqrt(0),0)
        self.assertEqual(lib.sqrt(36),6) 
        self.assertEqual(lib.sqrt(35),35**0.5)
    def test_sqrt_3(self):
        self.assertEqual(lib.sqrt(-35),0) 
        



# Запускаем тесты на исполнение
unittest.main(verbosity=2)
