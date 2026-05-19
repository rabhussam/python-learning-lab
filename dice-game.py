import random
import string


chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

print(f"Chars: {chars}")
print(f"Keys: {keys}")


def encrypt():
    original_text = input("Enter text: ")
    deciphered_text = ""

    for letter in original_text:
        index = chars.index(letter)
        deciphered_text += keys[index]
    return deciphered_text

def decrypt():
    text_to_decrypt = input("Enter text: ")
    original_text1 = ""

    for letter in text_to_decrypt:
        index = keys.index(letter)
        original_text1 += chars[index]
    return original_text1


while True:
    print("-----ENCRYPTION PROGRAM-----")
    print("1- Encrypt text")
    print("2- Decrypt text")
    print("3- Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = encrypt()
        print(f"Encrypted text: {val}")
    elif choice == 2:
        val = decrypt()
        print(f"Decrypted text: {val}")
    elif choice == 3:
        break
    else:
        print("Invalid choice")



