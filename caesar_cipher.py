import string

user_input = list(input("Enter a phrase: "))
shift_number = int(input("Number of shift: "))
alpha = list(string.ascii_lowercase)
encrypt = []

for i in user_input:
    new_place = user_input.index(i) + shift_number
    new_char = alpha[new_place]
    encrypt.append(new_char)

print("".join(encrypt))