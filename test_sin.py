# Подключаем библиотеку для тестирования
import unittest
import math
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):


    def test_sin(self):
        self.assertEqual(lib.sin(0),math.sin(0))
        self.assertEqual(lib.sin(3),math.sin(3))
        self.assertEqual(lib.sin(0),math.sin(0))
        self.assertEqual(lib.sin(math.pi),math.sin(math.pi))
        self.assertEqual(lib.sin(-3),math.sin(-3))
        self.assertEqual(lib.sin(math.pi//2),math.sin(math.pi//2))
    def test_sin_1(self):
        self.assertEqual(lib.sin(35),math.sin(35)) # wront test
    def test_sin_2(self):
        self.assertEqual(lib.sin(-35),math.sin(-35)) # wrong test
        



# Запускаем тесты на исполнение
unittest.main(verbosity=2)
