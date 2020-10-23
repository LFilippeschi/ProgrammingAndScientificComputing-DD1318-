
alphabet = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

number_of_characters = len(alphabet)

SECRET_OFFSET = 1


def offset_encrypt(input_string, offset):
    output_string = ""
    for my_index in range(0, len(input_string)):
        character = input_string[my_index]
        if character in alphabet:
            output_string += alphabet[(offset + alphabet.index(character)) % number_of_characters]
        else:
            output_string += character
    return output_string


def encrypt(input_string):
    return offset_encrypt(input_string, SECRET_OFFSET)


def decrypt(input_string):
    return offset_encrypt(input_string, -SECRET_OFFSET)

if __name__ == "__main__":
    my_string = input("Write the message you want me to encrypt:")
    out = encrypt(my_string)
    print("Encrypted version:", out)
    print("Reversing encryption we get:", decrypt(out))
