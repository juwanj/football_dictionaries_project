# assignment_3.py

def group_players_by_country_and_position(players_list):
    grouped = {}
    for player in players_list:
        country = player[6]
        position = player[1]
        player_dict = {
            'number': player[0],
            'position': position,
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': country,
            'club_country': player[7],
            'year': player[8]
        }
        if country not in grouped:
            grouped[country] = {}
        if position not in grouped[country]:
            grouped[country][position] = []
        grouped[country][position].append(player_dict)
    return grouped
