'''String Rotation; Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to check if s2 is a
rotation of s1 using only one call to isSubstring (e.g.,"waterbottle"isa rotation
of'erbottlewat").'''


def is_substring(s1, s2):
    return s2 in s1


def is_string_rotated(s1, s2):
    if len(s1) != len(s2):
        return False
    s3 = s1 + s1
    return is_substring(s3, s2)

print(is_string_rotated("waterbottle","erbottlewat"))
print(is_string_rotated("waterbottle","erbottleway"))