import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.name1 = Runner('Усэйн', 10)
        self.name2 = Runner('Андрей', 9)
        self.name3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            result = {}
            for key, value in i.items():
                result[key] = value.name
            print(result)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament1(self):
        self.all_results = Tournament(90, self.name1, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament2(self):
        self.all_results = Tournament(90, self.name2, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament3(self):
        self.all_results = Tournament(90, self.name1, self.name2, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[3] = self.all_results
