
def print_vowels(str):
    vowels="aeiou"
    for char in str:
        if char in vowels:
            print(char, end="")
text=input()

print_vowels(text)