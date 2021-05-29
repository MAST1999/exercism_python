def is_isogram(string):
    string = string.lower()
    char_set = set()
    for char in string:
        if char in char_set and char != "-" and char != " ":
            return False
        else:
            char_set.add(char)
    return True
