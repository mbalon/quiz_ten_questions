import uuid
import pickle


class Player:
    def __init__(self, name='unknown_player', score=0):
        self.name = name
        self.score = score
        self.id = uuid.uuid4()

    def get_player_name(self):
        return self.name

    def get_player_score(self):
        return self.score

    def set_player_name(self, name):
        self.name = name

    def set_player_score(self, score):
        self.score = score

    def add_to_score(self, points):
        self.score += points

    def save_player(self):
        path = r'C:\temp\players.txt'
        with open(path, 'wb') as file:
            pickle.dump(self, file)







