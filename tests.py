import Task2 as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        if ( self.participant.role == 'employee'):
            yield Task_2_emp_p1
