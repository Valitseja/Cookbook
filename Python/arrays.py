import random


def random_array(width, length):
    """Random data array."""
    return [random.getrandbits(width) for _ in range(length)]


def random_number(width, length):
    """Generator."""
    for _ in range(length):
        yield random.getrandbits(width)


print(", ".join(["{0:#0{1}x}".format(val, 4) for val in random_number(8, 16)]))
