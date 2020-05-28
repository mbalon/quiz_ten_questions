from quiz_ten_questions import player


def test_get_player_name_1():
    player_test = player.Player('Adam', 0)

    output = player_test.get_player_name()

    assert output == 'Adam'


def test_get_player_name_2():
    player_test = player.Player('Maciek', 0)

    output = player_test.get_player_name()

    assert output == 'Maciek'


def test_get_player_score_1():
    player_test = player.Player('Maciek', 0)

    output = player_test.get_player_score()

    assert output == 0


def test_get_player_score_2():
    player_test = player.Player('Maciek', 20)

    output = player_test.get_player_score()

    assert output == 20


def test_set_player_name_1():
    player_test = player.Player('Maciek', 20)

    player_test.set_player_name('Karol')

    assert player_test.name == 'Karol'


def test_set_player_name_2():
    player_test = player.Player('Maciek', 20)

    player_test.set_player_name('Wojtek')

    assert player_test.name == 'Wojtek'


def test_set_player_score_1():
    player_test = player.Player('Maciek', 20)

    player_test.set_player_score(5)

    assert player_test.score == 5


def test_set_player_score_2():
    player_test = player.Player('Maciek', 20)

    player_test.set_player_score(8)

    assert player_test.score == 8


def test_add_to_score_1():
    player_test = player.Player('Maciek', 20)

    player_test.add_to_score(5)

    assert player_test.score == 25


def test_load_players_1():
    player_test = player.Player('Maciek', 20)
    output = player_test.load_players()

    assert isinstance(output, list)


def test_parse_json_str_1():
    j_string = '{"id": "18ddb594-7246-4c05-a751-65a8271d71ed", "name": "Maciek", "score": 20}'
    player_test = player.Player('Maciek', 20)
    player_test.parse_json_str(j_string)
    player_2 = player.Player()
    player_2.name = "Maciek"
    player_2.id = "18ddb594-7246-4c05-a751-65a8271d71ed"
    player_2.score = 20
    assert player_2.id == player_test.id and player_2.name == player_test.name and player_2.score == player_test.score


def test_choose_player():
    player_1 = player.Player()
    player_1.id = 5
    players_list = [player_1]

    player_test = player.Player.choose_player(5, players_list)

    assert player_1 == player_test

