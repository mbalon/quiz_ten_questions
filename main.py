from quiz_ten_questions import questions
from quiz_ten_questions import utils
from quiz_ten_questions import player
from quiz_ten_questions import gameplay

utils.welcome_message()

# TODO: Add admin mode here

ans = input('''1 - start new game
2 - load game ''')
if ans == '1':
    name = input("Enter your name")
    player = player.Player(name)
elif ans == '2':
    players = player.Player.load_players()
    player_1 = player.Player()
    players_list = []

    for item in players:
        player_1.parse_json_str(item)
        players_list.append(player_1)
        print(player_1)
    ans = input("Enter id: ")
    player_1 = player.Player.choose_player(ans, players_list)
    print(player_1)
else:
    print("Please enter proper value (1 or 2)")

# TODO: choose questions from base

# TODO: Display question



