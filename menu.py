from players import add_player
from matches import add_match

def display_options():
    print('1) Add player')
    print('2) Add match')
    print('3) Show score')
    print('4) Show player\'s matches')


def menu(data):
    display_options()
    option_no = int(input())

    if option_no == 1:
        add_player(data)
    elif option_no == 2:
        add_match(data)
    elif option_no == 3:
        pass
    elif option_no == 4:
        pass
    else:
        print('option not found')
