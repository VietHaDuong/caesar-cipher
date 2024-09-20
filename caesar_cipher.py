import string

alpha = list(string.ascii_lowercase)
current_place =''
result = []

def main():
    option = input("Encode or decode: ").lower()
    user_input = list(input("Enter a phrase: ").replace(" ",''))
    shift_number = int(input("Number of shift: "))
    if option == "encode":
        answer = encode(user_input, shift_number)
        print("".join(answer))
    elif option == "decode":
        answer = decode(user_input, shift_number)
        print("".join(answer))

def encode(user_input, shift_number):
    for i in user_input:
        i == alpha.index(i)
        new_place = (alpha.index(i) + shift_number)
        if new_place > 25:
            new_place -= 26
        new_char = alpha[new_place]
        result.append(new_char)
    return result

def decode(user_input, shift_number):
    for i in user_input:
        i == alpha.index(i)
        new_place = (alpha.index(i) - shift_number)
        new_char = alpha[new_place]
        result.append(new_char)
    return result

main()