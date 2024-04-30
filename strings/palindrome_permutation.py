def is_permutation_palindrome(string):
    bit_vector = create_bit_vector(string.lower().replace(" ", ""))
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


def create_bit_vector(string):
    bit_vector = 0
    for char in string:
        index = ord(char) - ord('a')
        bit_vector = toggle_bit(bit_vector, index)
    return bit_vector


def toggle_bit(bit_vector, index):
    if index < 0:
        return bit_vector
    mask = 1 << index
    if (bit_vector & mask) == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    return bit_vector


def check_exactly_one_bit_set(bit_vector):
    return bit_vector & (bit_vector - 1) == 0

print(is_permutation_palindrome("Tact Coa"))