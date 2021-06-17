# Assignment 4
# Problem 3
# Stubborn Vowels

string = input()
vowels = []
words = []
start_index = 0

for index in range(len(string)):
    if string[index].lower() in "aeiou":
        vowels.append(string[index])
        words.append(string[start_index:index])
        start_index = index+1
if string[start_index:] != "":
    words.append(string[start_index:])
print(vowels)
print(words)