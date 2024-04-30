def one_edit_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    if len(string1) > len(string2):
        s1 = string2
        s2 = string1
    else:
        s2 = string1
        s1 = string2
    index1 = 0
    index2 = 0
    found_difference = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True
            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True

print(one_edit_away("pale","palse"))
print(one_edit_away("pale","ple"))
print(one_edit_away("pale","bae"))