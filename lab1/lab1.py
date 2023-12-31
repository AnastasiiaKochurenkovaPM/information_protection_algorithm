# Функція для запису тексту у файл
def write_to_file(filename, text):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Текст був записаний у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі у файл: {str(e)}")

# Функція для зчитування тексту з файлу
def read_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Помилка при зчитуванні з файлу: {str(e)}")
        return None

# Функція для шифрування та розшифрування тексту
def encrypt_decrypt_text(text, shift, language):
    # Алгоритм шифрування
    encrypted_text = ""
    alphabet = ""

    if language == "english":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    elif language == "ukrainian":
        alphabet = "абвгдежзийклмнопрстуфхцчшщьюя"

    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_lower = char.lower()

            index = (alphabet.index(char_lower) + shift) % len(alphabet)
            shifted_char = alphabet[index]

            if is_upper:
                shifted_char = shifted_char.upper()

            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

# Текст про вулицю Лазаренка українською мовою
lviv_ukrainian_text = "Вулиця Солов'ївська має свій початок ще із часів панщини Старші люди говорять що назву дали таку бо тут гніздилося багато солов'їв і влітку вся вулиця яка простягається на 10км наповнювалася співом цих дивовижних птахів"

# Записуємо текст українською мовою у файл
write_to_file("street_ukrainian.txt", lviv_ukrainian_text)

# Зчитуємо текст українською мовою з файлу
read_ukrainian_text = read_from_file("street_ukrainian.txt")

if read_ukrainian_text:
    # Шифруємо текст українською мовою з використанням зсуву 11
    encrypted_ukrainian_text = encrypt_decrypt_text(read_ukrainian_text, 11, "ukrainian")

    # Записуємо зашифрований текст українською мовою у новий файл
    write_to_file("encrypted_text_ukrainian.txt", encrypted_ukrainian_text)

    # Зчитуємо зашифрований текст українською мовою з файлу
    encrypted_read_ukrainian_text = read_from_file("encrypted_text_ukrainian.txt")

    if encrypted_read_ukrainian_text:
        # Розшифровуємо текст українською мовою
        decrypted_ukrainian_text = encrypt_decrypt_text(encrypted_read_ukrainian_text, -11, "ukrainian")
        print("Розшифрований текст (українська мова): " + decrypted_ukrainian_text)