def spin_words(sentence: str):
    list_of_words = sentence.split(" ")
    reversed_words = [
        "".join(reversed(word)) for word in list_of_words if len(word) >= 5
    ]
    return "".join(reversed_words)


print(spin_words("Welcome"))
