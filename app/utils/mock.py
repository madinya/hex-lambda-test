import random
import string
from typing import Any, Union


def get_random_int() -> int:
    return random.choice(range(1, 10))


def get_random_string() -> str:
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters[:10])


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def get_random_email() -> str:
    return f"{get_random_string()}@{get_random_choice(['hotmail.com', 'gmail.com', 'test.com'])}"


def get_random_sequence(length: int) -> str:
    digits = list(map(str, range(10)))
    sequence = [digits[random.randint(0, 9)] for _ in range(length)]
    return ''.join(sequence)


def get_random_phone() -> str:
    return get_random_sequence(10)


def get_random_elements_from_set(data: list) -> list:
    safe_data = data.copy()
    random.shuffle(safe_data)
    return safe_data[:random.randint(1, len(safe_data))]
