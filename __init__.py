
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Game'
    PLAYERS_PER_GROUP = 5
    NUM_ROUNDS = 1
    MANAGER_ROLE = 'manager'
    WORKER1_ROLE = 'employee'
    EXCHANGE_RATE = 100
    DECODE_PAYOFF = 100
    WORKER2_ROLE = 'employee'
    WORKER3_ROLE = 'employee'
    WORKER4_ROLE = 'employee'
class Subsession(BaseSubsession):
    pass
def my_function(subsession: Subsession):
    pass
class Group(BaseGroup):
    task_2_manager_payoff = models.IntegerField()
    task_2_employee_payoff = models.IntegerField()
class Player(BasePlayer):
    consent = models.BooleanField(choices=[[True, 'I consent, begin the study.'], [False, 'I do not consent, I do not wish to take part in the study.']])
    keep_same_role = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    identity_will_be_disclosed = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    how_many_output_points = models.IntegerField(choices=[[100, '100'], [200, '200'], [400, '400']])
    can_end_the_task_earlier = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    manager_informed_about_the_output = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    manager_informed_about_actual_costs = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    the_firm_will_always_pay = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    requested_funds_are_higher = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    answer = models.StringField(blank=True)
    numbers_decoded_correctly = models.IntegerField(initial=0)
    fin_cos_q1 = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    fin_cos_q2 = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    button = models.BooleanField(choices=[[True, 'True'], [False, 'False']])

class Start_Consent_Form(Page):
    form_model = 'player'
    form_fields = ['consent']
    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        participant = player.participant
        session.condition = ((participant.id_in_session -1) // 5 ) + 1
        con = session.condition
        return dict(con = con)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        group = player.group
        participant = player.participant
        import math
        
        con = ((participant.id_in_session -1) // 5 ) + 1
        session.condition = math.trunc(con)
        #session.condition = 1 # variable for condition for the group
        
        session.EXCHANGE_RATE = 100 # variable for points\money exchange 
        
        session.DECODE_PAYOFF = 100 # variable for decoding payoff
        
        participant.expiry = 0 # setting expiry time to 0 here, so Task 1 works for manager
        
        if player.id_in_group % 5 == 1:
            participant.role = 'manager'
        else:
            participant.role = 'employee'
        
        participant.TASK_1_PAYOFF = 0 # setting payoff for taks 1, so it works for manager
    @staticmethod
    def error_message(player: Player, values):
        if values['consent'] == False:
            return 'This answer option will not allow you to continue the experiment. Please report this to the experiment administrator.'


class General_information(Page):
    form_model = 'player'


class new_page(Page):
    form_model = 'player'


class The_Firm_and_the_Roles(Page):
    form_model = 'player'
    form_fields = ['keep_same_role', 'identity_will_be_disclosed']
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
                keep_same_role=True,
                identity_will_be_disclosed=False
            )
        
        error_messages = dict()
        
        for field_name in solutions:
             if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
        
        return error_messages
class Your_Role(Page):
    form_model = 'player'
class Task1_cond5(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        return (session.condition == 5)

class Task1_explanation_employee_p1(Page):
    form_model = 'player'
    form_fields = ['answer']
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.condition != 5 and participant.role == 'employee'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.answer = ''
class Task1_explanation_employee_p2(Page):
    form_model = 'player'
    form_fields = ['how_many_output_points', 'can_end_the_task_earlier', 'manager_informed_about_the_output']
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.condition != 5 and participant.role == 'employee'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.answer = ''
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
                how_many_output_points = 100,
                can_end_the_task_earlier = True,
                manager_informed_about_the_output = True,

            )
        
        error_messages = dict()
        
        for field_name in solutions:
             if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
        
        return error_messages

class Task1_example_manager_p1(Page):
    form_model = 'player'
    form_fields = ['answer']
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.condition != 5 and participant.role == 'manager'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.answer = ''
class Task1_example_manager_p2(Page):
    form_model = 'player'
    form_fields = ['how_many_output_points', 'can_end_the_task_earlier', 'manager_informed_about_the_output']
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.condition != 5 and participant.role == 'manager'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.answer = ''
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
                how_many_output_points = 100,
                can_end_the_task_earlier = True,
                manager_informed_about_the_output = True,

            )
        
        error_messages = dict()
        
        for field_name in solutions:
             if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
        
        return error_messages
class The_Financial_Consequences_of_Task_1_p1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        return session.condition != 5
class WIP_The_Financial_Consequences_of_Task_1_p2(Page):
    form_model = 'player'
    form_fields = ['fin_cos_q1', 'fin_cos_q2',]
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        return session.condition != 5
    @staticmethod
    def error_message(player: Player, values):
        session = player.session
        if session.condition == 1 or session.condition == 3:
            solutions = dict(fin_cos_q1=True, fin_cos_q2=False)
        if session.condition == 2 or session.condition == 4:
            solutions = dict(fin_cos_q1=False, fin_cos_q2=True)

        
        error_messages = dict()
        
        for field_name in solutions:
             if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
        
        return error_messages
class Task_2_explanation_employee_p1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == 'employee'
class Task_2_explanation_employee_p2(Page):
    form_model = 'player'
    form_fields = ['manager_informed_about_actual_costs', 'the_firm_will_always_pay', 'requested_funds_are_higher']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role== 'employee'
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
                requested_funds_are_higher = True,
                the_firm_will_always_pay = True,
                manager_informed_about_actual_costs = False,
        
            )
        
        error_messages = dict()
        
        for field_name in solutions:
             if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
        
        return error_messages


class Task_2_explanation_manager_p1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == 'manager'
class Task_2_explanation_manager_p2(Page):
    form_model = 'player'
    form_fields = ['requested_funds_are_higher', 'the_firm_will_always_pay', 'manager_informed_about_actual_costs']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == 'manager'
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
                requested_funds_are_higher = True,
                the_firm_will_always_pay = True,
                manager_informed_about_actual_costs = False,
        
            )
        
        error_messages = dict()
        
        for field_name in solutions:
             if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
        
        return error_messages


class Payoffs(Page):
    form_model = 'player'



class Start_practice_round(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        return session.condition != 5
class FALSE_Task_1_manager(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.role == 'manager' and False
page_sequence = [Start_Consent_Form, General_information, The_Firm_and_the_Roles, Your_Role, Task1_cond5, Task1_explanation_employee_p1, Task1_explanation_employee_p2, Task1_example_manager_p1, Task1_example_manager_p2, The_Financial_Consequences_of_Task_1_p1, WIP_The_Financial_Consequences_of_Task_1_p2, Task_2_explanation_employee_p1, Task_2_explanation_employee_p2, Task_2_explanation_manager_p1, Task_2_explanation_manager_p2, Payoffs, Start_practice_round]