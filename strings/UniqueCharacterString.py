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


print(unique_character_string("abcdd"))
print(unique_character_string("abcde"))
