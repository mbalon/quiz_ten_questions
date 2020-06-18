import uuid
import json
import pickle


class Player:
    def __init__(self, name='unknown_player', score=0):
        self.name = name
        self.score = score
        self.id = uuid.uuid4()

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, score: {self.score}'

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, score: {self.score}'

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
        content = Player.load_players()
        item = {"id": str(self.id), "name": self.name, "score": self.score}
        content.append(json.dumps(item))
        with open(path, 'wb') as file:
            pickle.dump(content, file)

    @staticmethod
    def load_players():
        path = r'C:\temp\players.txt'
        try:
            with open(path, 'rb') as file:
                return pickle.load(file)
        except EOFError:
            return []

    def parse_json_str(self, j_string):
        content = json.loads(j_string)
        self.id = content["id"]
        self.name = content["name"]
        self.score = content["score"]

    @staticmethod
    def choose_player(id, players_list):
        for player in players_list:
            if str(player.id) == str(id):
                return player

    def add_points(self, is_good):
        if is_good:
            self.score += 2
        else:
            self.score -= 1










