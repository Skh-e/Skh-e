from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='my_session', num_demo_participants=25, app_sequence=['Game', 'Task1', 'Task2', 'Questions'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['expiry', 'role', 'TASK_1_PAYOFF', 'TASK_2_PAYOFF', 'CHARITY_PAYOFF']
SESSION_FIELDS = ['condition', 'EXCHANGE_RATE', 'DECODE_PAYOFF', 'PAYOFF']
ROOMS = [    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
        use_secure_urls=True
    ),
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


