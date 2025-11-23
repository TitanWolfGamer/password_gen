from datetime import datetime, date
import string
import os
import json

from secrets import choice
from argparse import ArgumentParser, Namespace


rich_installed: bool = False
try:
    from rich.progress import track
    rich_installed = True
except ImportError:
    pass

with open(os.getcwd() + '/settings.json', 'r') as f:
    SETTINGS = json.load(f)


SAVE_DIR: str = 'saved_passwords'
CHARACTER_POOL: str = string.ascii_letters + string.digits + string.punctuation

PARSER: ArgumentParser = ArgumentParser()

# add arguments
PARSER.add_argument('-c', '--count', required=False, default=SETTINGS['standard_count'], type=int, help='The amount of passwords to generate')
PARSER.add_argument('-l', '--length', required=False, default=SETTINGS['standard_length'], type=int, help='The length of each password')
PARSER.add_argument('-s', '--save', action='store_true', help='saves the password in a file')
PARSER.add_argument('-no', '--no-output', action='store_true', help='prevents passwords from showing in the terminal')
PARSER.add_argument('--bypass-warning', action='store_true', help='bypass the warning for insecure passwords')

# parse arguments for later use
ARGS: Namespace = PARSER.parse_args()
COUNT: int = ARGS.count
LENGTH: int = ARGS.length
SAVE: bool = ARGS.save
NO_OUTPUT: bool = ARGS.no_output
BYPASS_WARNING: bool = ARGS.bypass_warning
del ARGS

if LENGTH < SETTINGS['min_length'] and not BYPASS_WARNING:
    print(f'passwords shorter than {SETTINGS['min_length']} characters are insecure!')
    print(f'length of at least {SETTINGS['min_length']} characters advised!')
    user = input('Continue? [y/n]: ') == 'y'
    if not user:
        print('Exiting...')
        exit()

# generate passwords
passwords: list[str] = []
for _ in track(range(COUNT), description=f'Generating {COUNT:,} {LENGTH:,}-character passwords...') if rich_installed else range(COUNT):
    pw: str = ''.join(choice(list(CHARACTER_POOL)) for _ in range(LENGTH))
    passwords.append(pw)

# outputs passwords if needed
if not NO_OUTPUT:
    width: int = len(str(len(passwords)))
    for i, pwd in enumerate(passwords, start=1):
        print(f'{i:>{width}}: {pwd}')


# create filename
current_date: date = date.today()
current_time: str = datetime.now().strftime("%H-%M-%S")
file_name: str = f'saved_passwords_{current_date}_{current_time}.txt'

# saves passwords if needed
if SAVE:
    CWD: str = os.getcwd()
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(f'{CWD}/{SAVE_DIR}/{file_name}', 'w') as f:
        f.write(''.join([f'{password}\n' for password in passwords]))

    print(f'\npasswords saved in: {CWD}/{SAVE_DIR}/{file_name}')