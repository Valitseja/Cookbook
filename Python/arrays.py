import random


def generate_byte_array(length):
    """Generates a byte array of array_length elements with 8 random bits"""
    return bytearray(random.getrandbits(8) for _ in range(length))


def generate_hex_array(width, length):
    """Generates array with hex values in string format"""
    return [hex(random.getrandbits(width)) for _ in range(length)]
