import Game as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        yield Start_Consent_Form, dict(consent=True)
        yield Your_Role
        yield General_information
        yield The_Firm_and_the_Roles, dict(
            keep_same_role=True,
            identity_will_be_disclosed=True,
        )
        if (self.session.condition == 5):
            yield Task1_cond5
        if self.session.condition != 5:
            yield The_Financial_Consequences_of_Task_1_p1
        if self.session.condition != 5:
            yield The_Financial_Consequences_of_Task_1_p2
        if self.session.condition != 5 and self.player.role == 'employee':
            yield Task1_example_employee_p1, dict(answer="xyz")
        if self.session.condition != 5 and self.player.role == 'employee':
            yield Task1_example_employee_p2, dict(
                how_many_output_points=50,
                can_end_the_task_earlier=True,
                manager_informed_about_the_output=True,
                how_many_points=50,
            )
        if self.session.condition != 5 and self.player.role == 'manager':
            yield Task1_example_manager, dict(
                how_many_output_points=50,
                can_end_the_task_earlier=True,
                manager_informed_about_the_output=True,
                how_many_points=50,
                answer="xyz",
            )
        if self.player.role == 'employee':
            yield Task_2_explanation_employee, dict(
                requested_funds_are_higher=True,
                the_firm_will_always_pay=True,
                manager_informed_about_actual_costs=True,
            )
        if self.player.role == 'manager':
            yield Task_2_explanation_manager, dict(
                requested_funds_are_higher=True,
                the_firm_will_always_pay=True,
                manager_informed_about_actual_costs=True,
            )
        if self.session.condition != 5:
            yield Payoffs
        if self.session.condition != 5:
            yield Start_practice_round
        if ( self.player.role == 'employee') and self.session.condition != 5:
            yield Preparation_Task_1
        if ( self.player.role == 'manager'):
            yield Task_1_manager