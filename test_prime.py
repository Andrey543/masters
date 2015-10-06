# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_prime_1(self):
        self.assertEqual(lib.prime(-100),False) #wrong test
    def test_prime_2(self):
        self.assertEqual(lib.prime(-1),False)   #wrong test
    def test_prime_3(self):
        self.assertEqual(lib.prime(-2),False)   #wrong test
    def test_prime_4(self):    
        self.assertEqual(lib.prime(1),False)    #wrong test
    def test_prime(self):
        self.assertEqual(lib.prime(2),True)
        self.assertEqual(lib.prime(5),True)
        self.assertEqual(lib.prime(3),True)
        self.assertEqual(lib.prime(22),False)
        self.assertEqual(lib.prime(100),False)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
