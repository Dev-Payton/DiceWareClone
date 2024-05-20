import os

import argparse
import random


def program_entry():
    print("""
    ██▀███  ▓█████  ▄████▄   ██░ ██ ▓█████ ▒██   ██▒
    ▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒▒ █ █ ▒░
    ▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██▀▀██░▒███   ░░  █   ░
    ▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄  ░ █ █ ▒
    ░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒██▒ ▒██▒
    ░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░▒▒ ░ ░▓ ░
    ░▒ ░ ▒░ ░ ░  ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░░░   ░▒ ░
    ░░   ░    ░   ░         ░  ░░ ░   ░    ░    ░
    ░        ░  ░░ ░       ░  ░  ░   ░  ░ ░    ░
    ░   
        
    """)


def genpass(password_length, quantity_of_passwords, storage_for_passwords):
    password_list = []
    diceware_dict = {}
    with open('wordlist.txt', 'r') as file:
        for line in file:
            number, word = line.split()
            diceware_dict[number] = word
    for k in range(quantity_of_passwords):
        current_passphrase = ""
        for i in range(password_length):
            number = "".join(str(random.randint(1, 6)) for j in range(5))
            current_passphrase += diceware_dict.get(number).capitalize()
        password_list.append(current_passphrase)
    for element in password_list:
        print(element)


def command2():
    print('Executing command 2')


def main():
    parser = argparse.ArgumentParser(description="[+] A simple password creation tool")
    subparsers = parser.add_subparsers(dest='command', help='Subcommands')

    genpass_parser = subparsers.add_parser('genpass', help='Generate a password')
    genpass_parser.add_argument('-l', '--length', type=int, help='Length of the password', required=True)
    genpass_parser.add_argument('-q', '--quantity', type=int, help='Quantity of passwords', default=1)
    genpass_parser.add_argument('-s', '--storage', type=str, help='Storage location of the passwords')
    parser.add_argument('-c2', '--command2', action='store_true', help='Run command 2')
    args = parser.parse_args()

    # Check which flag is given and execute the corresponding function
    if args.command == 'genpass':
        genpass(args.length, args.quantity, args.storage)
    elif args.command == 'command2':
        command2()
    else:
        parser.print_help()


if __name__ == '__main__':
    program_entry()
    main()


class CurrentDirectoryJsonFiles:
    def __init__(self):
        self.current_directory = os.path.dirname(os.path.realpath(__file__))
        self.files_in_directory = os.listdir(self.current_directory)
        self.json_files_in_directory = [file for file in self.files_in_directory if file.endswith(".json")]

    def get_json_files(self):
        return self.json_files_in_directory

    def get_current_directory(self):
        return self.current_directory
