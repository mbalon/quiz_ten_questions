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
