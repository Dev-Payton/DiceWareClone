import random


def generate_dice_rolls(number_of_words):
    number_list = []
    for i in range(number_of_words):
        number = "".join(str(random.randint(1, 6)) for _ in range(5))
        number_list.append(number)
    return create_Pass_Phrase(number_list)


def create_Pass_Phrase(number_list):
    diceware_dict = {}
    generatedPassPhrase = ''
    with open('wordlist.txt', 'r') as file:
        for line in file:
            number, word = line.split()
            diceware_dict[number] = word
    for number in number_list:
        generatedPassPhrase += diceware_dict.get(number).capitalize()
    return generatedPassPhrase


generate_dice_rolls(6)
