import string

user_input = list(input("Enter a phrase: "))
shift_number = int(input("Number of shift: "))
alpha = list(string.ascii_lowercase)
current_place =''
encrypt = []

for i in user_input:
    i == alpha.index(i)
    new_place = (alpha.index(i) + shift_number)
    if new_place > 25:
        new_place -= 26
    new_char = alpha[new_place]
    encrypt.append(new_char)

print("".join(encrypt))