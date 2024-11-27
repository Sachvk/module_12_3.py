import module_12_2
import tests_12_1
import unittest

frTest = unittest.TestSuite()
frTest.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
frTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runer = unittest.TextTestRunner(verbosity=2)
runer.run(frTest)
