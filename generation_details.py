import os
import json
from password_creation import *


class JsonFiles:
    def __init__(self):
        self.current_directory = os.path.dirname(os.path.realpath(__file__))
        self.files_in_directory = os.listdir(self.current_directory)
        self.json_files_in_directory = [file for file in self.files_in_directory if file.endswith(".json")]

    def get_json_files(self):
        return self.json_files_in_directory

    def get_current_directory(self):
        return self.current_directory


def prompt_user_options():
    json_information = JsonFiles()
    print("[+] - This program is simply a diceware clone designed to take in file types, extract details such as "
          "Usernames, Emails, and Passwords so that further analysis can easily be done.\n"
          "Please note: This program will only take in files within the current directory.\n")
    selection = input("[+] Please specify the type of file you would like to extract inside of the directory: {} \n["
                      "\"json\"]\n".format(json_information.get_current_directory()))


def prompt_user_for_extraction():
    if selection == 'json':
        print("[+] - Please choose a JSON file to extract from the following list:")
        json_files = json_information.get_json_files()
        for i, json_file in enumerate(json_files):
            print(f"{i + 1}: {json_file}")

        file_choice = int(input("[+] Enter the number corresponding to the JSON file: \n")) - 1
        if 0 <= file_choice < len(json_files):
            json_specific_file = json_files[file_choice]
            print(f"[+] You have selected: {json_specific_file}")
            print("Please select an option to manipulate the JSON file:")
            user_input = input("[1] Find usernames\n"
                               "[2] Find emails\n"
                               "[3] Find passwords\n"
                               "[4] Exit\n")
            if user_input == '1':
                print("NULL WILL BE UPDATED LATER")
            elif user_input == '2':
                print("NULL WILL BE UPDATED LATER")
            elif user_input == '3':
                password_options = input("What would you like to do with the given passwords?\n"
                                         "[1] Generate and replace all \n"
                                         "[2] Generate and print new passwords \n")
                if password_options == '1':
                    new_passkey_lengths = int(input("What is your preferred passkey length?\n"))
                    data = read_specific_json_file(json_specific_file)
                    items = data['items']
                    for item in items:
                        new_password = generate_dice_rolls(new_passkey_lengths)
                        item['login']['password'] = new_password
                        username = item['login']['username']
                        password = item['login']['password']
                        print(f"[+] Username: {username} NEW Password: {new_password}")


                elif password_options == '2':
                    print("Attempting Password Pull")
                    data = read_specific_json_file(json_specific_file)
                    items = data['items']
                    amount_of_accounts = 0
                    for item in items:
                        amount_of_accounts += 1
                        username = item['login']['username']
                        password = item['login']['password']
                        print(f"[+] Username: {username} Password: {password}")
                    print(amount_of_accounts)
            elif user_input == '4':
                print("Exiting...JK")
        else:
            print("[-] Invalid selection. Please try again.")
    else:
        print("[-] Invalid file type selection. Please choose 'json'.")


def read_specific_json_file(json_specific_file):
    try:
        with open(json_specific_file, 'r') as file:
            data = json.load(file)
            return data
            # print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"[-] Error reading {json_specific_file}: {e}")


prompt_user_for_extraction()
