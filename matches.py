

class Match:
    def __init__(self,blue_team,white_team,result):
        self.blue_team = blue_team
        self.white_team = white_team
        self.result = result

    def __str__(self):
        return f"Match({self.blue_team}, {self.white_team}, {self.result})"


def add_match(data):
    blue_team = input('Blue: ')
    white_team = input('White: ')
    result = input('Result: ')
    with open('data/matches.txt', "a+") as matches_file:
        matches_file.write(f'{blue_team} {white_team} {result}\n')
    data.matches.append(Match(blue_team, white_team, result))
    data.print_matches()