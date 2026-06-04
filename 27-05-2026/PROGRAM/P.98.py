def replace_vowels(string, char):
    vowels = "AEIOUaeiou"  # List of vowels to be replaced
    for vowel in vowels:
        string = string.replace(vowel, char)  # Replace each vowel with
    return string

print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
