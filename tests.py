import Task1 as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        if (self.player.round_number == 1 or player.round_number == 5+1) and self.participant.role == 'employee':
            yield Start_emp