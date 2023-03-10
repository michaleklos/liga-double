
from players import Player
from matches import Match

class Data:
    def __init__(self):
        self.players= []
        self.matches= []
    def print_players(self):
        for player in self.players:
            print(player)
    def print_matches(self):
        for match in self.matches:
            print(match)
    def find_player(self,name):
        for player in self.players:
            if name==player.name:
                return player
        raise RuntimeError("literowka")        

    
class Team:
    def __init__(self, player1, player2):
        self.player1= player1
        self.player2= player2
    def __str__(self):
        return f"Team({self.player1}, {self.player2})"


def load_players(data):
    with open('data/players.txt', "r") as players_file:
        lines = players_file.readlines()
    for line in lines:
        name, points = line.split(' ')
        data.players.append(Player(name, float(points)))


def load_matches(data):
    with open('data/matches.txt', "r") as matches_file:
        lines = matches_file.readlines()
    for line in lines:
        win_player1, win_player2, loose_player1, loose_player2, result = line.split(' ')
        data.matches.append(Match(Team(win_player1,win_player2), Team(loose_player1, loose_player2), int(result)))


def load_data():
    data = Data()
    load_players(data)
    data.print_players()
    load_matches(data)
    
    return data
