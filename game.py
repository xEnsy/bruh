import random
def numbers():
    return random.randint(1, 50)
def lucky(selected_number, winning_number):
    return selected_number == winning_number