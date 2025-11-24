from collections.abc import Callable
from typing import Any
__vanilla_input: Callable = input
__vanilla_type: type = type

def input(prompt: str, choices: list[str] = None, default: str = '', show_choices: bool = True, show_default: bool = True, type: __vanilla_type = str, required: bool = False) -> Any:
    given_choices: bool = bool(choices)

    prompt += f' [{'/'.join(choices)}]' if given_choices and show_choices else ''
    prompt += f' [{default}]' if default and show_default else ''

    prompt += ': ' if choices and show_choices or default and show_default else ''
    while True:
        user: Any = __vanilla_input(prompt)

        if given_choices:
            if user not in choices:
                print('Please enter a valid given choice.')
                continue

        try:
            user = type(user)
        except ValueError:
            print(f'Please enter a valid given type. ({'Integer' if type == int else 'string' if type == str else 'boolean' if type == bool else 'list' if type == list else ''})')
            continue

        if user == '':
            user = default

        if required and user == '':
            continue

        break
    return user


def main() -> None:
    a = input('How many do you want? ', default='0', choices=[''], show_default=False, type=int)
    print(a+2)

if __name__ == '__main__':
    main()