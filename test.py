import random
import array


def get_user_input():
    break_loop = False
    while not break_loop:
        try:
            user_input = int(input('[+] Please enter a passkey length you would like to have generated\n'))
        except ValueError:
            continue
        print(type(user_input))
        if type(user_input) == int:
            print("[-] DEBUG INFORMATION -- Integer Input Successful -- ")
            break
        else:
            print("[+] Please enter a numerical value between [3 - 8], not a String. ")
            continue
    generate_dice_rolls(user_input)


def generate_dice_rolls(user_input):
    number_list = []
    for i in range(user_input):
        number = "".join(str(random.randint(1,6)) for _ in range(5))
        number_list.append(number)
        print(number_list[i])
    create_Pass_Phrase(number_list)


def create_Pass_Phrase(number_list):
    diceware_dict = {}
    generatedPassPhrase = ''
    with open('wordlist.txt', 'r') as file:
        for line in file:
            number, word = line.split()
            diceware_dict[number] = word
    for number in number_list:
        generatedPassPhrase += diceware_dict.get(number)
    print(generatedPassPhrase)



get_user_input()
