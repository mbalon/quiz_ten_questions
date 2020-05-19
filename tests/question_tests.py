import json
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


def test_create_1():
    quest_test = questions.Questions()
    record = ['Ques', 'ans1', 'ans2', 'ans3', 'ans4']
    output = quest_test.create(record)
    assert output == {'Ques': ['ans1', 'ans2', 'ans3', 'ans4']}


def test_create_2():
    quest_test = questions.Questions()
    record = ['Ques_sec', 'ans_g', 'ans_w1', 'ans_w2', 'ans_w3']
    output = quest_test.create(record)
    assert output == {'Ques_sec': ['ans_g', 'ans_w1', 'ans_w2', 'ans_w3']}


def test_convert_to_json_1():
    quest_test = questions.Questions()
    quest_test.id = '1'
    quest_test.content = 'Q'
    quest_test.good_ans = 'ans_g'
    quest_test.wrong_ans = ['ans_w1', 'ans_w2', 'ans_w3']

    output = quest_test.convert_to_json()
    jstr = ''' "id": {} "content": {} "good_ans": {} "wrong_ans": {}'''\
            .format(quest_test.id, quest_test.content, quest_test.good_ans, quest_test.wrong_ans)

    assert output == json.dumps(jstr)
