import string

all_letters = string.ascii_letters
user_input = input("Enter range (e.g., a-c or A-C): ")
first, last = user_input.split('-')
first_letter = all_letters.index(first)
last_letter = all_letters.index(last)
if first_letter <= last_letter:
    print(all_letters[first_letter:last_letter + 1])
else:
    print("Invalid range")