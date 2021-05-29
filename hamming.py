def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")

    return sum(char1 != char2 for (char1, char2) in zip(strand_a, strand_b))
