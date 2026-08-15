def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    """

    result = []
    shift = shift % 26

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            new_char = chr(
                (ord(char) - base + shift) % 26 + base
            )

            result.append(new_char)
        else:
            # Keep spaces, numbers, and punctuation unchanged
            result.append(char)

    return ''.join(result)


def encrypt(text, shift):
    return caesar_cipher(text, shift, mode='encrypt')


def decrypt(text, shift):
    return caesar_cipher(text, shift, mode='decrypt')


if __name__ == "__main__":

    while True:
        print("\n=== Caesar Cipher Tool ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose (1/2/3): ").strip()

        if choice == '1':
            message = input("Enter message: ")

            try:
                shift = int(input("Enter shift value: "))
                print("Encrypted message:", encrypt(message, shift))
            except ValueError:
                print("Shift must be an integer.")

        elif choice == '2':
            message = input("Enter message: ")

            try:
                shift = int(input("Enter shift value: "))
                print("Decrypted message:", decrypt(message, shift))
            except ValueError:
                print("Shift must be an integer.")

        elif choice == '3':
            print("Exiting Caesar Cipher Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")