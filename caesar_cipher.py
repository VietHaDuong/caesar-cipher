import string

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
        new_place = (ord(i) + shift_number)
        if new_place > 122:
            new_place -= 26
        result.append(chr(new_place))
    return result

def decode(user_input, shift_number):
    for i in user_input:
        new_place = (ord(i) - shift_number)
        if new_place < 97:
            new_place += 26
        result.append(chr(new_place))
    return result

main()