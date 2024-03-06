import string

alphabet = string.ascii_lowercase

def encrypter(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.islower():
                index = (alphabet.index(char) + shift) % 26
                encrypted_char = alphabet[index]
            else:
                char = char.lower()
                index = (alphabet.index(char) + shift) % 26
                encrypted_char = alphabet[index].upper()
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

message = input("What message would you like to encrypt: ")
shift = int(input("How many times would you like to shift it? It can be negative: "))
encrypted_message = encrypter(message, shift)
print("Encryption:", encrypted_message)
