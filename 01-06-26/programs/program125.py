def is_isogram(word):
    word=word.lower()
    unique=set()
    for letter in word:
        if letter in unique:
            return False
        unique.add(letter)
    return True
print(is_isogram("Algorism"))
