import random
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
    player.save_player()
elif ans == '2':
    player_1 = utils.load_game()
    player = player_1
    print(player)
else:
    print("Please enter proper value (1 or 2)")

questions_list = utils.choose_questions()
print(questions_list)



