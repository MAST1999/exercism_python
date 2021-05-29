def abbreviate(words):
    list_words = words.upper().replace("_", "").replace("-", " ").split()
    acronym = ""
    for word in list_words:
        acronym += word[0]
    return acronym
