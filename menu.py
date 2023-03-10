from players import add_player
from matches import add_match
from players import save_players_score


def display_options():
    print('1) Add player')
    print('2) Add match')
    print('3) Quit')
    
def menu(data):
    display_options()
    option_no = int(input())

    if option_no == 1:
        add_player(data)
    elif option_no == 2:
        add_match(data)
    elif option_no == 3:
        quit()
    else:
        print('option not found')
