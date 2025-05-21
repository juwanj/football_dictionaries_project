# main.py

from squads_data import SQUADS_DATA
from assignment_1 import players_as_dictionaries
from assignment_2 import group_players_by_position
from assignment_3 import group_players_by_country_and_position
from pprint import pprint

print("\nAssignment 1: Players as Dictionaries\n")
players_dicts = players_as_dictionaries(SQUADS_DATA)
pprint(players_dicts)

print("\nAssignment 2: Grouped by Position\n")
grouped_by_position = group_players_by_position(SQUADS_DATA)
pprint(grouped_by_position)

print("\nAssignment 3: Grouped by Country and Position\n")
grouped_by_country = group_players_by_country_and_position(SQUADS_DATA)
pprint(grouped_by_country)
