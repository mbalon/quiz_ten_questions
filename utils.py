import random
from quiz_ten_questions import questions
from quiz_ten_questions import player


def welcome_message():
    print('''Welcome in quiz ten question game
    Each game contain ten questions
    Only one answer in question is good
    Every good answer gives you 2 points
    Every wrong answer takes you 1 point
    Game is and after 10 questions or if you have
    less than 0 points
    Are you ready?
    ''')


def load_game():
    players = player.Player.load_players()
    player_1 = player.Player()
    players_list = []

    for item in players:
        player_1.parse_json_str(item)
        players_list.append(player_1)
        print(player_1)
    ans = input("Enter id: ")
    return player.Player.choose_player(ans, players_list)

def choose_questions():
    path = 'c:/temp/question_file.json'
    file_content = questions.Questions.load_from_file(path)
    return random.sample(file_content['questions'], 10)

# TODO: Add 50:50 option
