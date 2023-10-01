import numpy as np

# Function to create the key table
def create_key_table():
    alphabet = "кабвгдежзийлмнопрстуфхцчшьюя"
    key_table = np.array(list(alphabet)).reshape(4, 7)
    return key_table

# Function to decrypt text using the Playfair cipher
def playfair_decrypt(ciphertext, key_table):
    ciphertext = ciphertext.replace(" ", "")  # Remove spaces
    plaintext = []
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        if len(pair) == 2:  # Check if 'pair' contains two characters
            row1, col1 = np.where(key_table == pair[0])
            row2, col2 = np.where(key_table == pair[1])
            if row1.size > 0 and row2.size > 0:  # Check if not empty
                if row1 == row2:
                    plaintext.append(key_table[row1, (col1 - 1) % 7][0])
                    plaintext.append(key_table[row2, (col2 - 1) % 7][0])
                elif col1 == col2:
                    plaintext.append(key_table[(row1 - 1) % 4, col1][0])
                    plaintext.append(key_table[(row2 - 1) % 4, col2][0])
                else:
                    plaintext.append(key_table[row1, col2][0])
                    plaintext.append(key_table[row2, col1][0])
            else:
                # Handle the case when a character is not found in the key table
                plaintext.append(pair[0])
                plaintext.append(pair[1])
        else:
            # If 'pair' does not contain two characters (e.g., at the end of the ciphertext)
            plaintext.append(pair[0])
    return "".join(plaintext)

# Create the key table
key_table = create_key_table()

# Read the ciphertext from the file
with open("cipheredText.txt", "r") as file:
    ciphertext = file.read()

# Decrypt the text using the key table
decrypted_text = playfair_decrypt(ciphertext, key_table)

# Print the decrypted text
print("\nРозшифрований текст:\n" + decrypted_text + "\n")
