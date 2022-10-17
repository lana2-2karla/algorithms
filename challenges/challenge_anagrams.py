def is_anagram(first_string, second_string):

    first = list(first_string.lower())
    second = list(second_string.lower())

    if len(first) == 0 or len(second) == 0:
        return False

    if len(first) != len(second):
        return False

    for letter in first:
        if letter in second:
            second.remove(letter)
        else:
            return False
    return True
    
