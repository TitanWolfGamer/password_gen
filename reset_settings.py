import os
import json
import argparse

rich_installed = True
try:
    import rich
    from rich.prompt import Prompt
except ImportError:
    rich_installed = False

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--yes', action='store_true', help="Automatically answer yes to all questions")

ARGS = PARSER.parse_args()


with open('./config.json', 'r') as f:
    CONFIG = json.load(f)

DEFAULT_SETTINGS = CONFIG['default_settings']

prompt: str = 'Are you sure you want to delete all settings?'

surety: bool = False
if not ARGS.yes:
    if rich_installed:
        surety = Prompt.ask(prompt=prompt, choices=['y', 'n'], show_choices=True, default='n', show_default=False) == 'y'
    else:
        surety = input(f'{prompt} (y/n): ') == 'y'
else:
    surety = True

if surety:
    # delete settings file
    if 'settings.json' in os.listdir(os.getcwd()):
        os.remove(os.getcwd() + '\\settings.json')

    # dump default settings in new file
    with open('settings.json', 'w') as file:
        json.dump(DEFAULT_SETTINGS, file)
    print('settings reset!')

