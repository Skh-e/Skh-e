
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Task2'
    PLAYERS_PER_GROUP = 5
    NUM_ROUNDS = 1
    MANAGER_ROLE = 'manager'
    WORKER1_ROLE = 'employee'
    WORKER2_ROLE = 'employee'
    WORKER3_ROLE = 'employee'
    WORKER4_ROLE = 'employee'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    task_2_payoff = models.IntegerField(initial=0, max=2200)
    task_2_request = models.IntegerField(initial=0, max=2000, min=920)

class Task_2_emp_p1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return ( participant.role == 'employee')
class Task_2_emp_p2(Page):
    form_model = 'player'
    form_fields = ['task_2_request']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return ( participant.role == 'employee')
    def vars_for_template(player: Player):
        participant = player.participant
        payoff = round(participant.TASK_1_PAYOFF)
        donation = round(payoff * 0.2)
        bonus = round(payoff * 0.1)
        return dict(payoff=payoff, donation=donation, bonus = bonus)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.TASK_2_PAYOFF = player.task_2_request - 920
class Task_2_emp_p3(Page):
    form_model = 'player'
    form_fields = ['task_2_request']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return ( participant.role == 'employee')
    @staticmethod
    def vars_for_template(player: Player):
        
        e = player.task_2_request - 920
        m = 2200 - 920 - e
        return dict(e=e,m=m,)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.TASK_2_PAYOFF = player.task_2_payoff
class ManagerWaitPage(WaitPage):
    title_text = 'Waiting for employees to finish their requests'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == "manager"

class EmployeeWaitPage(WaitPage):
    title_text = 'Waiting for the manager and other participants to proceed.'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == "employee"


class Task_2_manager(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == 'manager'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        m = 2200 - group.get_player_by_id(player.id_in_group + 1).task_2_payoff
        
        emp_request_1 = group.get_player_by_id(player.id_in_group + 1).task_2_request
        emp_request_2 = group.get_player_by_id(player.id_in_group + 2).task_2_request
        emp_request_3 = group.get_player_by_id(player.id_in_group + 3).task_2_request
        emp_request_4 = group.get_player_by_id(player.id_in_group + 4 ).task_2_request
        
        emp_payoff_1 = group.get_player_by_id(player.id_in_group + 1).task_2_request -920
        emp_payoff_2 = group.get_player_by_id(player.id_in_group + 2).task_2_request -920
        emp_payoff_3 = group.get_player_by_id(player.id_in_group + 3).task_2_request -920
        emp_payoff_4 = group.get_player_by_id(player.id_in_group +4 ).task_2_request -920
        
        return dict( m=m, emp_request_1 = emp_request_1,
                    emp_request_2 = emp_request_2,
                    emp_request_3 = emp_request_3,
                    emp_request_4 = emp_request_4,
                    emp_payoff_1 = emp_payoff_1, 
                    emp_payoff_2 = emp_payoff_2,
                    emp_payoff_3 = emp_payoff_3,
                    emp_payoff_4 = emp_payoff_4,
                   )
class Task_2_res(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        participant = player.participant

        emp_request_1 = 0
        emp_request_2 = 0
        emp_request_3 = 0
        emp_request_4 = 0
        emp_payoff_1 = 0
        emp_payoff_2 = 0
        emp_payoff_3 = 0
        emp_payoff_4 = 0
        m = 0
        this_player_manager_payoff = 2200 - player.task_2_request
        player_payoff = player.task_2_request - 920

        if participant.role == 'manager':
             m = 2200 - group.get_player_by_id(player.id_in_group + 1).task_2_request
             emp_request_1 = group.get_player_by_id(player.id_in_group + 1).task_2_request
             emp_request_2 = group.get_player_by_id(player.id_in_group + 2).task_2_request
             emp_request_3 = group.get_player_by_id(player.id_in_group + 3).task_2_request
             emp_request_4 = group.get_player_by_id(player.id_in_group + 4).task_2_request

             emp_payoff_1 = group.get_player_by_id(player.id_in_group + 1).task_2_request - 920
             emp_payoff_2 = group.get_player_by_id(player.id_in_group + 2).task_2_request - 920
             emp_payoff_3 = group.get_player_by_id(player.id_in_group + 3).task_2_request - 920
             emp_payoff_4 = group.get_player_by_id(player.id_in_group + 4).task_2_request - 920
             participant.TASK_2_PAYOFF = m
        else:
             participant.TASK_2_PAYOFF = player_payoff

        return dict(m=m, emp_request_1=emp_request_1,
                emp_request_2=emp_request_2,
                emp_request_3=emp_request_3,
                emp_request_4=emp_request_4,
                emp_payoff_1=emp_payoff_1,
                emp_payoff_2=emp_payoff_2,
                emp_payoff_3=emp_payoff_3,
                emp_payoff_4=emp_payoff_4,
                player_payoff=player_payoff,
                this_player_manager_payoff=this_player_manager_payoff
                )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        group = player.group
        participant = player.participant
        emp_payoff_1 = group.get_player_by_id(2).task_2_request -920
        
        
        player_payoff = player.task_2_request - 920
        
        if participant.role == 'manager':
            participant.TASK_2_PAYOFF = emp_payoff_1

        else:
            participant.TASK_2_PAYOFF = player_payoff

page_sequence = [Task_2_emp_p1, Task_2_emp_p2, Task_2_emp_p3, ManagerWaitPage, Task_2_manager, EmployeeWaitPage, Task_2_res]