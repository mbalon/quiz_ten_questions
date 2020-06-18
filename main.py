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

question = questions.Questions()

for item in questions_list:
    question.convert_from_dict_to_instance(item)
    question.display()
    ans = gameplay.ask_for_answer()
    is_good = question.check_answer(ans)
    player.add_to_score(is_good)
player.save_player()
