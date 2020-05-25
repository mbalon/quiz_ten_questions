from quiz_ten_questions import player


def test_get_player_name():
    player_test = player.Player('Adam', '0')

    output = player_test.get_player_name()

    assert output == 'Adam'