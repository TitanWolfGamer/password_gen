import datetime
import string
import os

from secrets import choice
from rich.progress import track

from argparse import ArgumentParser, Namespace

SAVE_DIR: str = 'saved_passwords'
CHARACTER_POOL: str = string.ascii_letters + string.digits + string.punctuation

PARSER: ArgumentParser = ArgumentParser()

# add arguments
PARSER.add_argument('-c', '--count', required=False, default=10, type=int, help='The amount of passwords to generate')
PARSER.add_argument('-l', '--length', required=False, default=16, type=int, help='The length of each password')
PARSER.add_argument('-s', '--save', action='store_true', help='saves the password in a file')
PARSER.add_argument('-no', '--no-output', action='store_false', help='prevents passwords from showing in the terminal')

# parse arguments for later use
ARGS: Namespace = PARSER.parse_args()
count: int = ARGS.count
length: int = ARGS.length
save: bool = ARGS.save
output: bool = ARGS.no_output
del ARGS


# generate passwords
passwords: list[str] = []
for _ in track(range(count), description=f'Generating {count:,} {length:,}-character passwords...'):
    pw: str = ''.join(choice(list(CHARACTER_POOL)) for _ in range(length))
    passwords.append(pw)

# outputs them if needed
if output:
    width: int = len(str(len(passwords)))
    for i, pwd in enumerate(passwords, start=1):
        print(f'{i:>{width}}: {pwd}')


# create filename
current_date = datetime.date.today()
current_time = datetime.datetime.now().strftime("%H-%M-%S")
file_name = f'saved_passwords_{current_date}_{current_time}.txt'

# save passwords if needed
if save:
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(f'./{SAVE_DIR}/{file_name}', 'w') as f:
        f.write(''.join([f'{password}\n' for password in passwords]))

    print()
    print(f'passwords saved in: ./{SAVE_DIR}/{file_name}')