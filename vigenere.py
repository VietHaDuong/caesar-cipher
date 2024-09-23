import string


result = []

def main():
    num = 0
    option = input("Encode or decode: ").lower()
    user_input = list(input("Enter a phrase: ").replace(" ",''))
    key = list(input("Enter key: "))
    if option == "encode":
        answer = encode(user_input, key, num)
        print("".join(answer))
    elif option == "decode":
        answer = decode(user_input, key, num)
        print("".join(answer))

def encode(user_input, key, num):
    for i in user_input:
        if num > (len(key) - 1):
            num = 0
        encrypt_letter = ord(i) + ord(key[num]) - 97
        if encrypt_letter > 122:
            encrypt_letter -= 26
        result.append(chr(encrypt_letter))
        num += 1
    return result
        
    

def decode(user_input, key, num):
    for i in user_input:
        if num > (len(key) - 1):
            num = 0
        decrypt_letter = ord(i) - ord(key[num]) + 97
        if decrypt_letter < 97:
            decrypt_letter += 26
        result.append(chr(decrypt_letter))
        num += 1
    return result

main()