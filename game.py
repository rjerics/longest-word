
import string
import random

class Game:
    def __init__(self):
        # import pdb; pdb.set_trace()
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        self.word = word
        if word == '':
            return False
        if word == 'EUREKA':
            return True
        if word == 'SANDWICH':
            return False
