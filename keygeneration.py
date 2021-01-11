# choose a random element from a list
from random import seed
from random import choice
from random import randint
import secrets


# initialize random seed for random number generator
seed(randint(1, 3000))


def random_selector(name_list):
    # make choices from the sequence
    for _ in range(1):
        selection = choice(name_list)
        return str.lower(selection)


def generate_names_list():

    with open('first_names.txt', 'r') as f:
        separated_firsts = f.read()
        first_name_list = separated_firsts.split()
        print(first_name_list)
    with open('last_names.txt', 'r') as f:
        separated_lasts = f.read()
        last_name_list = separated_lasts.split()
        print(last_name_list)

    names_list = []
    for i in range(20):
        name = "{} {}".format(random_selector(first_name_list), random_selector(last_name_list) )
        names_list.append(name)

    return names_list


def attach_random_code():
    random_string = secrets.token_hex(15)
    return random_string


attach_random_code()


def generate_names_with_keys():
    names_and_codes = []
    for name in generate_names_list():
        entry = (name, attach_random_code())
        names_and_codes.append(entry)
    return names_and_codes


print(generate_names_with_keys())