import numpy as np

# Function to create the key table
def create_key_table():
    alphabet = "кабвгдежзийлмнопрстуфхцчшьюя"
    key_table = np.array(list(alphabet)).reshape(4, 7)
    return key_table

# Function to encrypt text using the Playfair cipher
def playfair_encrypt(plaintext, key_table):
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    ciphertext = []
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        row1, col1 = np.where(key_table == pair[0])
        row2, col2 = np.where(key_table == pair[1])
        if row1.size > 0 and row2.size > 0:  # Check if not empty
            if row1 == row2:
                ciphertext.append(key_table[row1, (col1 + 1) % 7][0])
                ciphertext.append(key_table[row2, (col2 + 1) % 7][0])
            elif col1 == col2:
                ciphertext.append(key_table[(row1 + 1) % 4, col1][0])
                ciphertext.append(key_table[(row2 + 1) % 4, col2][0])
            else:
                ciphertext.append(key_table[row1, col2][0])
                ciphertext.append(key_table[row2, col1][0])
        else:
            # Handle the case when a character is not found in the key table
            ciphertext.append(pair[0])
            ciphertext.append(pair[1])
    return "".join(ciphertext)

def writeFile(line, fileName, type):
    with open(fileName, type) as file: file.write(line)
    file.close()

# Open text
plaintext = "вулицясоловївськамаєсвійпочатокщеізчасівпанщинистаршілюдиговорятьщоназвудалитакуботутгніздилосябагатосоловївівліткувсявулицянаповнюваласяспівомцихдивовижнихптахів"

writeFile(plaintext + "\n", "openText.txt", "w")

# Create the key table
key_table = create_key_table()

# Encrypt the text and write to a file
ciphertext = playfair_encrypt(plaintext, key_table)
writeFile(ciphertext + "\n", "cipheredText.txt", "w")

print("\nВідкритий текст:\n" + plaintext + 
          "\n\nЗашифрований текст:\n" + ciphertext + "\n")