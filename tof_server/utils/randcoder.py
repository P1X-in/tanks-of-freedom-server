"""Module for random codes"""
import random

def get_random_code(length):
    """Method for generating random codes of set length"""
    new_code = ''

    characters_pool = "ACDEFHJKLMNPRTWXY3479"
    for _ in range(length):
        new_code = new_code + random.SystemRandom().choice(characters_pool)

    return new_code
