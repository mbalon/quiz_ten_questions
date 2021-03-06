import uuid
import json
import random


class Questions:

    def __init__(self, content='', good_ans='', wrong_ans=None):
        self.id = None
        self.content = content
        self.good_ans = good_ans
        if not wrong_ans:
            self.wrong_ans = ['']

        self.question = {self.content: [self.good_ans]+self.wrong_ans}

    @staticmethod
    def get_user_question():
        print('''
                    Input a new question in following way:
                    Question;goodAnswer;wrongAnswer;wrongAnswer;wrongAnswer
                ''')
        new_record = input().split(';')
        return new_record

    def create(self, new_record):
        self.id = str(uuid.uuid4())
        self.content = new_record[0]
        self.good_ans = new_record[1]
        self.wrong_ans = new_record[2:]
        self.question = {self.content: [self.good_ans]+self.wrong_ans}

        return self.question

    def convert_from_dict_to_instance(self, dict):
        self.id = dict['id']
        self.content = dict['content']
        self.good_ans = dict['good_ans']
        self.wrong_ans = dict['wrong_ans']

    def convert_to_dict(self):
        question_dict = {"id": self.id, "content": self.content, "good_ans": self.good_ans, "wrong_ans": self.wrong_ans}
        return question_dict

    def save_question_to_file(self, path):
        content = self.load_from_file(path)

        content['questions'].append(self.convert_to_dict())

        with open(path, 'w') as file:
            json.dump(content, file)
        return

    @staticmethod
    def load_from_file(path):
        with open(path, 'r') as file:
            return json.load(file)

    def display(self):
        answers = [self.good_ans] + self.wrong_ans
        random.shuffle(answers)
        print(answers)
        print(
            f'''{self.content}
1. {answers[0]} \t 2. {answers[1]}
3. {answers[2]} \t 4. {answers[3]}'''
        )

    def check_answer(self, answer):
        return answer == self.good_ans
