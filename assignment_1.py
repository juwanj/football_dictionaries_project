# assignment_1.py

def players_as_dictionaries(players_list):
    players_dicts = []
    for player in players_list:
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        }
        players_dicts.append(player_dict)
    return players_dicts
