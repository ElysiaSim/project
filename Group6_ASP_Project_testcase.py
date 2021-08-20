import unittest
import Group6_ASP_Project as prog

class test(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(round(prog.top3Mean, 2), 873071.33)

    """
    def test_total(self):
        self.assertEqual(prog.top3e, 2619214)"""