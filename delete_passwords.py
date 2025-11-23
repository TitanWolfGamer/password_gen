import os
import argparse

rich_installed = False
try:
    import rich
    from rich.prompt import Prompt
    rich_installed = True
except ImportError:
    pass

def show_warning() -> None:
    print('Deleting all passwords in irreversible!')


PARSER = argparse.ArgumentParser()
PARSER.add_argument('-y', '--yes', action='store_true', help="suppress prompts")
ARGS = PARSER.parse_args()

surety: bool = False
if not ARGS.yes:
    show_warning()
    if rich_installed:
        surety = True if Prompt.ask('Are you sure?', choices=['y', 'n'], default='n', show_default=False, case_sensitive=False) == 'y' else False
    else:
        surety = True if input('Are you sure?') == 'y' else False
else:
    surety = True


FOLDER = os.getcwd() + '\\saved_passwords'

if surety:
    if not os.path.exists(FOLDER):
        print('Folder does not exist, exiting...')
        exit()
    # deleting all files
    for file in os.listdir(FOLDER):
        os.remove(FOLDER + '\\' + file)

    # deleting the directory
    os.rmdir(FOLDER)

    print('Passwords deleted.')
else:
    print('Exiting...')
    exit()