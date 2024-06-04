from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'Task1'
    PLAYERS_PER_GROUP = 5
    NUM_ROUNDS = 200
    TASKS = (
        39, 23, 30, 33, 37, 35, 44, 22, 32, 42, 36, 40, 21, 25, 41, 45, 38, 29, 28, 24, 34, 20, 31, 27, 43, 26, 36, 24,
        32,
        29, 31, 37, 27, 22, 28, 41, 38, 23, 25, 43, 44, 42, 20, 33, 34, 35, 39, 21, 40, 26, 30, 45, 26, 29, 39, 41, 34,
        43,
        22, 37, 24, 27, 25, 36, 23, 38, 45, 40, 33, 35, 44, 32, 20, 30, 31, 42, 21, 28, 34, 42, 37, 22, 24, 39, 20, 30,
        29,
        26, 38, 36, 40, 25, 43, 41, 27, 45, 35, 33, 21, 44, 32, 31, 23, 28, 28, 31, 35, 20, 41, 33, 21, 24, 32, 29, 43,
        26,
        38, 36, 22, 23, 25, 30, 37, 27, 40, 45, 44, 34, 39, 42, 32, 25, 40, 39, 34, 36, 37, 35, 22, 26, 27, 24, 33, 38,
        29,
        41, 43, 21, 42, 45, 23, 30, 28, 44, 31, 20, 43, 27, 44, 23, 28, 38, 34, 39, 40, 36, 42, 33, 29, 25, 32, 35, 45,
        20,
        22, 30, 31, 37, 41, 24, 26, 21, 24, 38, 39, 32, 27, 30, 31, 45, 36, 44, 22, 25, 28, 20, 26, 42, 35, 43, 37, 21,
        40,
        29, 41, 34, 33, 23)
    ANSWERS = (
        'A', 'Y', 'V', 'D', 'K', 'L', 'P', 'E', 'C', 'J', 'H', 'F', 'B', 'Z', 'W', 'T', 'S', 'U', 'O', 'G', 'R', 'I',
        'X',
        'M', 'Q', 'N', 'H', 'G', 'C', 'U', 'X', 'K', 'M', 'E', 'O', 'W', 'S', 'Y', 'Z', 'Q', 'P', 'J', 'I', 'D', 'R',
        'L',
        'A', 'B', 'F', 'N', 'V', 'T', 'N', 'U', 'A', 'W', 'R', 'Q', 'E', 'K', 'G', 'M', 'Z', 'H', 'Y', 'S', 'T', 'F',
        'D',
        'L', 'P', 'C', 'I', 'V', 'X', 'J', 'B', 'O', 'R', 'J', 'K', 'E', 'G', 'A', 'I', 'V', 'U', 'N', 'S', 'H', 'F',
        'Z',
        'Q', 'W', 'M', 'T', 'L', 'D', 'B', 'P', 'C', 'X', 'Y', 'O', 'O', 'X', 'L', 'I', 'W', 'D', 'B', 'G', 'C', 'U',
        'Q',
        'N', 'S', 'H', 'E', 'Y', 'Z', 'V', 'K', 'M', 'F', 'T', 'P', 'R', 'A', 'J', 'C', 'Z', 'F', 'A', 'R', 'H', 'K',
        'L',
        'E', 'N', 'M', 'G', 'D', 'S', 'U', 'W', 'Q', 'B', 'J', 'T', 'Y', 'V', 'O', 'P', 'X', 'I', 'Q', 'M', 'P', 'Y',
        'O',
        'S', 'R', 'A', 'F', 'H', 'J', 'D', 'U', 'Z', 'C', 'L', 'T', 'I', 'E', 'V', 'X', 'K', 'W', 'G', 'N', 'B', 'G',
        'S',
        'A', 'C', 'M', 'V', 'X', 'T', 'H', 'P', 'E', 'Z', 'O', 'I', 'N', 'J', 'L', 'Q', 'K', 'B', 'F', 'U', 'W', 'R',
        'D',
        'Y')
    M_ROLE = 'manager'
    W1_ROLE = 'employee'
    W2_ROLE = 'employee'
    W3_ROLE = 'employee'
    W4_ROLE = 'employee'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    right_answers = models.IntegerField(initial=0)
    answer = models.StringField(blank=True)
    end_task = models.StringField(blank=True, choices=[['1', 'End Task']])
    practice_right_answers = models.IntegerField(initial=0)
    my_page_timeout_seconds = 360
    my_page_timeout_seconds = models.IntegerField(initial=360)

class Manager_text(Page):
    form_model = 'player'
    timeout_seconds = 10

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (participant.role == 'manager') and player.round_number == 1

    @staticmethod
    def get_timeout_seconds(player):
        return player.my_page_timeout_seconds


class Start_emp(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 1 or player.round_number == 5 + 1) and participant.role == 'employee'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS.
        if player.round_number == 1:
            participant.expiry = time.time() + 40

        if player.round_number == 6:
            participant.expiry = time.time() + 60 * 5
            form_model = 'player'


class Practice_emp(Page):
    form_model = 'player'
    form_fields = ['answer']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        import time
        return (participant.expiry - time.time() > 3) and player.round_number <= 5

    @staticmethod
    def vars_for_template(player: Player):
        res = 0

        for i in player.in_previous_rounds():
            res += i.practice_right_answers

        task = C.TASKS[player.round_number]
        ra = C.ANSWERS[player.round_number]

        return dict(task=task, res=res, ra=ra)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # import time

        if C.ANSWERS[player.round_number] == player.answer:
            player.practice_right_answers = + 1

    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry - time.time()


class Task_1_emp(Page):
    form_model = 'player'
    form_fields = ['answer', 'end_task']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        import time

        return (
                participant.expiry - time.time() > 3) and 5 < player.round_number < 200

    @staticmethod
    def vars_for_template(player: Player):
        res = 0

        for i in player.in_previous_rounds():
            res += i.right_answers

        task = C.TASKS[player.round_number]
        ra = C.ANSWERS[player.round_number]

        return dict(task=task, res=res, ra=ra)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        # import time
        if player.end_task == '1':
            participant.expiry = 0

        if C.ANSWERS[player.round_number] == player.answer:
            player.right_answers = +1

    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry - time.time()


class Wait_page(WaitPage):
    title_text = 'Waiting for all players to finish task 1'

    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.condition != 5 and participant.expiry < 3 and player.round_number == 200 and participant.role == 'manager'


class Summary_manager(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return session.condition != 5 and player.round_number == 200 and participant.role == 'manager'

    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        group = player.group
        res = []

        for i in range(player.id_in_group + 1, player.id_in_group + 5):
            t = 0
            for j in group.get_player_by_id(i).in_previous_rounds():
                t += j.right_answers
            res.append(t)

        emp_payoff_1 = res[0] * session.DECODE_PAYOFF
        emp_payoff_2 = res[1] * session.DECODE_PAYOFF
        emp_payoff_3 = res[2] * session.DECODE_PAYOFF
        emp_payoff_4 = res[3] * session.DECODE_PAYOFF

        m = emp_payoff_1 * 0.1

        return dict(m=m, emp_payoff_1=emp_payoff_1, emp_payoff_2=emp_payoff_2, emp_payoff_3=emp_payoff_3,
                    emp_payoff_4=emp_payoff_4)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        group = player.group
        participant = player.participant
        personal_payoff = 0
        for j in group.get_player_by_id(player.id_in_group).in_previous_rounds():
            personal_payoff += j.right_answers

        if participant.role == "manager":
            for j in group.get_player_by_id(player.id_in_group + 1).in_previous_rounds():
                personal_payoff += j.right_answers
            participant.TASK_1_PAYOFF = personal_payoff * session.DECODE_PAYOFF


class Task1_complete(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return player.round_number == 200 and participant.role == 'employee'


class Summary_emp(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        participant = player.participant
        return player.round_number == 200 and participant.role == 'employee'

    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        group = player.group
        personal_payoff = 0
        for j in group.get_player_by_id(player.id_in_group).in_previous_rounds():
            personal_payoff += j.right_answers

        personal_payoff *= session.DECODE_PAYOFF

        charity = round(personal_payoff * 0.2)
        bonus = round(personal_payoff * 0.1)

        return dict(personal_payoff=personal_payoff, charity=charity, bonus=bonus)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        group = player.group
        participant = player.participant
        personal_payoff = 0
        for j in group.get_player_by_id(player.id_in_group).in_previous_rounds():
            personal_payoff += j.right_answers

        if participant.role == "employee":
            participant.TASK_1_PAYOFF = personal_payoff * session.DECODE_PAYOFF
            if session.condition == 2 or session.condition == 4:
                participant.TASK_1_PAYOFF = participant.TASK_1_PAYOFF * 1
            if session.condition == 1 or session.condition == 2:
                participant.CHARITY_PAYOFF = participant.TASK_1_PAYOFF * 0.2


page_sequence = [Start_emp, Practice_emp, Manager_text, Task_1_emp, Wait_page, Summary_manager, Task1_complete, Summary_emp ]
