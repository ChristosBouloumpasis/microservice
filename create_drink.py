from connect_to_db import *


def make_random_drink():
    strength = get_random("strength")
    temp = get_random("temperature")
    taste = get_random("taste")
    name = get_random("name")
    extra = get_random("extra")
    return f"{strength} {taste} {temp} {name} {extra}"
