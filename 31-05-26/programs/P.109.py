def index_of_caps(word):

    return [i for i, char in enumerate(word) if char.isupper()]

print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))

print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))
