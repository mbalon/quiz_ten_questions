import json
import questions
import os


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


def test_convert_to_dict_1():
    quest_test = questions.Questions()
    quest_test.id = '1'
    quest_test.content = 'Q'
    quest_test.good_ans = 'ans_g'
    quest_test.wrong_ans = ['ans_w1', 'ans_w2', 'ans_w3']

    output = quest_test.convert_to_dict()
    question_dict = {"id": quest_test.id, "content": quest_test.content,
                     "good_ans": quest_test.good_ans, "wrong_ans": quest_test.wrong_ans}
    assert output == question_dict


def test_save_question_to_file_1():
    quest_test = questions.Questions()
    quest_test.id = '1'
    quest_test.content = 'Q'
    quest_test.good_ans = 'ans_g'
    quest_test.wrong_ans = ['ans_w1', 'ans_w2', 'ans_w3']
    path = 'c:/temp/question_file.json'

    quest_test.save_question_to_file(path)
    is_file_exist = os.path.isfile(path)

    assert is_file_exist


def test_save_question_to_file_2():
    quest_test = questions.Questions()
    quest_test.id = '1'
    quest_test.content = 'Q'
    quest_test.good_ans = 'ans_g'
    quest_test.wrong_ans = ['ans_w1', 'ans_w2', 'ans_w3']
    path = 'c:/temp/question_file.json'

    quest_test.save_question_to_file(path)

    with open(path, 'r') as file:
        content = json.load(file)

    assert quest_test.convert_to_dict() in content['questions']


def test_load_from_file():
    quest_test = questions.Questions()
    quest_test.id = '1'
    quest_test.content = 'Q'
    quest_test.good_ans = 'ans_g'
    quest_test.wrong_ans = ['ans_w1', 'ans_w2', 'ans_w3']
    path = 'c:/temp/question_file.json'

    output = quest_test.load_from_file(path)

    with open(path, 'r') as file:
        assert output == json.load(file)


