# Word Counter
# Counts the Character in your name or something else and show you the strenght of character

# Solution
def word_counter(s):
    character = {}
    for char in s:
        character[char] = s.count(char)
    return character

character = input("Enter Characters : ")
print(word_counter(character))