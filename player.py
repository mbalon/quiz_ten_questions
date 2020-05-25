class Player:
    def __init__(self, name='unknown_player', score=0):
        self.name = name
        self.score = score

    def get_player_name(self):
        return self.name
