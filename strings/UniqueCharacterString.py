def unique_character_string(string):
    length = len(string)
    if length > 128:
        return False
    array = [False] * 128
    for char in string:
        val = ord(char)
        if array[val]:
            return False
        array[val] = True
    return True


def unique_character_string_using_bit_man(string):
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (checker & 1 << val) > 0:
            return False
        checker |= 1 << val
    return True


print(unique_character_string("abcdd"))
print(unique_character_string("abcde"))

print(unique_character_string_using_bit_man("abcdd"))
