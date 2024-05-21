import os

import argparse
import random
import math


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


def password_analyzer(password, flag):
    if flag == 'length':
        return len(password)
    elif flag == 'complexity':
        entropy, char_set_size = calculate_entropy(password)
        print("Password to be analyzed: {}".format(password))
        print("Flag: {}".format(flag))
        print(f"Password: {password}")
        print(f"Character Set Size: {char_set_size}")
        print(f"Entropy: {entropy:.2f} bits")


def calculate_entropy(password):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "!@#$%^&*()"
    char_set = set()

    for char in password:
        if char in uppercase:
            char_set.update(uppercase)
        elif char in lowercase:
            char_set.update(lowercase)
        elif char in digits:
            char_set.update(digits)
        elif char in special_chars:
            char_set.update(special_chars)

    c = int(len(char_set))
    l = int(len(password))
    possible_combinations = c ** l
    entropy = math.log2(possible_combinations)
    return entropy, c


def main():
    parser = argparse.ArgumentParser(description="[+] A simple password creation tool")
    subparsers = parser.add_subparsers(dest='command', help='Subcommands')

    genpass_parser = subparsers.add_parser('genpass', help='Generate a password')
    genpass_parser.add_argument('-l', '--length', type=int, help='Length of the password', required=True)
    genpass_parser.add_argument('-q', '--quantity', type=int, help='Quantity of passwords', default=1)
    genpass_parser.add_argument('-s', '--storage', type=str, help='Storage location of the passwords')

    password_analyzer_parser = subparsers.add_parser('password-analyzer', help='Analyze passwords')
    password_analyzer_parser.add_argument('password', type=str, help='Password to be analyzed')
    password_analyzer_parser.add_argument('-f', '--flag', choices=['length', 'complexity'], help='Flag to be analyzed',
                                          required=True)

    parser.add_argument('-c2', '--command2', action='store_true', help='Run command 2')
    args = parser.parse_args()

    # Check which flag is given and execute the corresponding function
    if args.command == 'genpass':
        genpass(args.length, args.quantity, args.storage)
    elif args.command == 'command2':
        command2()
    elif args.command == 'password-analyzer':
        password_analyzer(args.password, args.flag)
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
