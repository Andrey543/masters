# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_even(self):
        #self.assertEqual(lib.factorial(0),1)
        #self.assertEqual(lib.factorial(2),2)
        #self.assertEqual(lib.factorial(1),1)
        #self.assertEqual(lib.factorial(5),120)
        #self.assertEqual(lib.factorial(-2),1)
        self.assertEqual(lib.factorial(-1),1)
       # self.assertEqual(lib.factorial(-10),1)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
