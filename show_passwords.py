import os

PASSWORDS_PATH: str = os.getcwd() + '\\saved_passwords'
FOLDER_EXISTS = os.path.exists(PASSWORDS_PATH)
if not FOLDER_EXISTS or not os.listdir(PASSWORDS_PATH):
    print('no saved passwords found.')
    exit()
for filename in os.listdir(PASSWORDS_PATH):
    print(f'{'=' * 10}  {filename}  {'=' * 10}')
    with open(PASSWORDS_PATH + '/' + filename, 'r') as file:
        print(file.read())