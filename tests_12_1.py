import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        test1 = Runner('name1')
        for i in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        test2 = Runner('name2')
        for i in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        test3, test4 = Runner('name3'), Runner('name4')
        for i in range(10):
            test3.run()
            test4.walk()
        self.assertNotEqual(test3.distance, test4.distance)
