
from players import save_players_score
class Match:
    def __init__(self,win_team,loose_team,result):
        self.win_team = win_team
        self.loose_team = loose_team
        self.result = result

    def __str__(self):
        return f"Match({self.win_team}, {self.loose_team}, {self.result})"


def add_match(data):
    win_team = input('win: ')
    loose_team = input('loose: ')
    result = input('Result: ')
    with open('data/matches.txt', "a+") as matches_file:
        matches_file.write(f'{win_team} {loose_team} {result}\n')
    match=Match(win_team, loose_team, int(result))
    data.matches.append(match)
    update_scores_for_players(data, match)

def calculate_moved_points(diff, bilans):
    return pow((diff/2720+1.7),7.25)*(bilans/10+0.5)

def calculate_ratio(player1, player2):
    return player1.points/(player1.points+player2.points) 

def calculate_diff(win_player1, win_player2, loose_player1, loose_player2):
    return -win_player1.points-win_player2.points+loose_player1.points+loose_player2.points

    
def update_scores_for_players(data, match):
    win_player1_name, win_player2_name = match.win_team.split(' ')
    win_player1=data.find_player(win_player1_name)
    win_player2=data.find_player(win_player2_name)
    loose_player1_name, loose_player2_name = match.loose_team.split(' ')
    loose_player1=data.find_player(loose_player1_name)
    loose_player2=data.find_player(loose_player2_name)
    win_player2_ratio=calculate_ratio(win_player1, win_player2)
    win_player1_ratio=1-win_player2_ratio
    loose_player1_ratio=calculate_ratio(loose_player1, loose_player2)
    loose_player2_ratio=1-loose_player1_ratio
    diff=calculate_diff(win_player1, win_player2, loose_player1, loose_player2)
    points_to_add=calculate_moved_points(diff, match.result)
    win_player1.points+=win_player1_ratio*points_to_add
    win_player2.points+=win_player2_ratio*points_to_add
    loose_player1.points-=loose_player1_ratio*points_to_add
    loose_player2.points-=loose_player2_ratio*points_to_add
    save_players_score(data)
    data.print_players()
