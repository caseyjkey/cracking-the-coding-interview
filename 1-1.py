# Determine if a string is all unique characters

def unique(word):
    chars = set()
    for letter in word:
        if letter in chars:
            return False
        chars.add(letter)
    return True

print(unique("abc"))
print(unique("aabc"))
