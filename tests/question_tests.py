import questions


def test_get_user_question_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "Ques;ans1;ans2;ans3;ans4")
    quest_test = questions.Questions()
    output = quest_test.get_user_question()
    assert output == ['Ques', 'ans1', 'ans2', 'ans3', 'ans4']


def test_get_user_question_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "Ques_sec;ans_g;ans_w1;ans_w2;ans_w3")
    quest_test = questions.Questions()
    output = quest_test.get_user_question()
    assert output == ['Ques_sec', 'ans_g', 'ans_w1', 'ans_w2', 'ans_w3']