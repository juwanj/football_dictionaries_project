# test_assignments.py

import unittest
from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries
from assignment_2 import group_players_by_position
from assignment_3 import group_players_by_country_and_position

class TestFootballAssignments(unittest.TestCase):

    def test_assignment_1(self):
        result = players_as_dictionaries(SQUADS_DATA)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(player, dict) for player in result))
        self.assertEqual(len(result), len(SQUADS_DATA))
        self.assertIn('name', result[0])

    def test_assignment_2(self):
        result = group_players_by_position(SQUADS_DATA)
        self.assertIsInstance(result, dict)
        for position, players in result.items():
            self.assertIsInstance(position, str)
            self.assertIsInstance(players, list)
            self.assertTrue(all(isinstance(player, dict) for player in players))

    def test_assignment_3(self):
        result = group_players_by_country_and_position(SQUADS_DATA)
        self.assertIsInstance(result, dict)
        for country, positions in result.items():
            self.assertIsInstance(positions, dict)
            for position, players in positions.items():
                self.assertTrue(all(player['country'] == country for player in players))

if __name__ == "__main__":
    unittest.main()
