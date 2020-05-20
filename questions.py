import uuid
import json


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
        self.id = uuid.uuid4()
        self.content = new_record[0]
        self.good_ans = new_record[1]
        self.wrong_ans = new_record[2:]
        self.question = {self.content: [self.good_ans]+self.wrong_ans}

        return self.question

    def convert_to_dict(self):
        question_dict = {"id": self.id, "content": self.content, "good_ans": self.good_ans, "wrong_ans": self.wrong_ans}
        return question_dict

    def save_question_to_file(self, path):
        with open(path, 'r') as file:
            content = json.load(file)

        content['questions'].append(self.convert_to_dict())

        with open(path, 'w') as file:
            json.dump(content, file)
        return

    def load(self):
        pass

    def display(self):
        pass
