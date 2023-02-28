
class Player:
    def __init__(self,name,points):
        self.name = name
        self.points = points

    def __str__(self):
        return f"Player({self.name}, {self.points})"


def add_player(data):
    name = input('Name: ')
    points = input('Strating points: ')
    with open('data/players.txt', "a+") as players_file:
        players_file.write(f'{name} {points}\n')
    data.players.append(Player(name, int(points)))
    data.print_players()
