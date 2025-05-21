# assignment_2.py

def group_players_by_position(players_list):
    grouped = {}
    for player in players_list:
        position = player[1]
        player_dict = {
            'number': player[0],
            'position': position,
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        }
        if position not in grouped:
            grouped[position] = []
        grouped[position].append(player_dict)
    return grouped
