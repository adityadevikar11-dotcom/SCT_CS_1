🔐 Caesar Cipher Encryption & Decryption

A simple Python-based implementation of the Caesar Cipher, a classical substitution cipher used to demonstrate the fundamentals of encryption and decryption.

📌 About the Project

This project implements the Caesar Cipher algorithm in Python.

The program allows the user to:

- Encrypt a message using a shift value
- Decrypt an encrypted message
- Use both uppercase and lowercase letters
- Preserve spaces, numbers, and special characters
- Use positive or large shift values
- Exit the program through an interactive menu

⚙️ How Caesar Cipher Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions.

For example, with a shift of 3:

A → D
B → E
C → F
...
X → A
Y → B
Z → C

The program uses modulo 26 to handle wrapping around the alphabet.

Encryption

C = (P + K) mod 26

Decryption

P = (C - K) mod 26

Where:

- "P" = Plaintext
- "C" = Ciphertext
- "K" = Shift/Key

🚀 Features

- 🔒 Message encryption
- 🔓 Message decryption
- 🔤 Uppercase and lowercase support
- 🔢 Numbers remain unchanged
- ✨ Special characters remain unchanged
- 🔄 Supports repeated operations
- 🚪 Exit option
- ⚡ Simple command-line interface

🛠️ Technologies Used

- Python 3
- Modular Arithmetic
- String Manipulation
- Functions
- Conditional Statements
- Loops


💻 Example

=== Caesar Cipher Tool ===
1. Encrypt a message
2. Decrypt a message
3. Exit

Choose (1/2/3): 1
Enter message: Hello World
Enter shift value: 3

Encrypted message: Khoor Zruog

Decryption Example

Choose (1/2/3): 2
Enter message: Khoor Zruog
Enter shift value: 3

Decrypted message: Hello World

Exit

Choose (1/2/3): 3

Exiting Caesar Cipher Tool. Goodbye!

⚠️ Security Note

The Caesar Cipher is a classical educational cipher and is not considered secure for protecting real-world sensitive information. It is useful for learning basic concepts of cryptography, substitution ciphers, keys, and modular arithmetic.

🎯 Learning Objectives

Through this project, I learned:

- The basic concept of classical cryptography
- How Caesar Cipher encryption works
- How decryption reverses encryption
- Modular arithmetic in cryptography
- Python functions and loops
- String and character manipulation
- Using Git and GitHub for version control

👨‍💻 Author

Developed as a learning project to explore Python Programming and the fundamentals of cryptography



