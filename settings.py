import json
from better_functions import input

rich_installed: bool = True
try:
    import rich
    from rich import print as rprint
    from rich.prompt import Prompt
except ImportError:
    rich_installed = False

with open('settings.json', 'r') as f:
    settings = json.load(f)



print('Settings:')
for setting in settings:
    key: str = setting
    value: int | bool = settings[setting]
    if rich_installed:
        rprint(f'{key}: {value}')
    else:
        print(f'{key}: {value}')

print('\n')
if rich_installed:
    rprint(f'Enter name to change / nothing to exit')
else:
    print('Enter name to change / nothing to exit')

choices = list(settings.keys())
choices.append('')

setting_to_change: str = input.input('> ', choices=choices, show_choices=False, default='', show_default=False)

if not setting_to_change:
    exit()


new_value = input.input('Please enter new value\n> ', type=type(settings[setting_to_change]), required=True)

settings[setting_to_change] = new_value
with open('settings.json', 'w') as f:
    json.dump(settings, f)

if rich_installed:
    rprint(f'Setting changed to {new_value}')
else:
    print(f'Setting changed to {new_value}')