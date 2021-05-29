def score(word):
    word = word.lower()
    score = 0
    list_1 = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
    list_2 = ["d", "g"]
    list_3 = ["b", "c", "m", "p"]
    list_4 = ["f", "h", "v", "w", "y"]
    list_5 = ["k"]
    list_8 = ["j", "x"]
    list_10 = ["q", "z"]
    for char in word:
        if char in list_1:
            score += 1
        elif char in list_2:
            score += 2
        elif char in list_3:
            score += 3
        elif char in list_4:
            score += 4
        elif char in list_5:
            score += 5
        elif char in list_8:
            score += 8
        elif char in list_10:
            score += 10

    return score
