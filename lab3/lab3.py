# Завдання 1: Таблиця пропорційної заміни
substitution_table = {
    'А': 100, 'Б': 101, 'В': 102, 'Г': 103, 'Д': 104, 'Е': 105, 'Є': 106, 'Ж': 107, 'З': 108, 'И': 109,
    'І': 110, 'Ї': 111, 'Й': 112, 'К': 113, 'Л': 114, 'М': 115, 'Н': 116, 'О': 117, 'П': 118, 'Р': 119,
    'С': 120, 'Т': 121, 'У': 122, 'Ф': 123, 'Х': 124, 'Ц': 125, 'Ч': 126, 'Ш': 127, 'Щ': 128, 'Ь': 129,
    'Ю': 130, 'Я': 131, 'а': 200, 'б': 201, 'в': 202, 'г': 203, 'д': 204, 'е': 205, 'є': 206, 'ж': 207,
    'з': 208, 'и': 209, 'і': 210, 'ї': 211, 'й': 212, 'к': 213, 'л': 214, 'м': 215, 'н': 216, 'о': 217,
    'п': 218, 'р': 219, 'с': 220, 'т': 221, 'у': 222, 'ф': 223, 'х': 224, 'ц': 225, 'ч': 226, 'ш': 227,
    'щ': 228, 'ь': 229, 'ю': 230, 'я': 231, ' ': 232
}

# Завдання 2: Функція для дешифрування криптограми
def decrypt(ciphertext):
    decrypted_text = ""
    buffer = ""
    i = 0
    while i < len(ciphertext):
        char = ciphertext[i]
        if char.isdigit():
            buffer += char
        else:
            if buffer:
                code = int(buffer)
                for key, value in substitution_table.items():
                    if value == code:
                        decrypted_text += key
                        break
                buffer = ""
            if char != ' ':
                decrypted_text += char
        i += 1
    return decrypted_text



# Зчитуємо криптограму з файлу
with open('encrypted.txt', 'r', encoding='utf-8') as cipher_file:
    ciphertext = cipher_file.read()

# Дешифруємо криптограму
decrypted_text = decrypt(ciphertext)

# Записуємо розшифрований текст у файл
with open('decrypted_text.txt', 'w', encoding='utf-8') as decrypted_file:
    decrypted_file.write(decrypted_text)

# Завдання 3: Перевірка правильності дешифрування
original_text = "Вулиця Соловївська має свій початок ще із часів панщини. Старші люди говорять, що назву дали таку бо тут гніздилося багато соловїв і влітку вся вулиця, яка простягається на 10 км, наповнювалася співом цих дивовижних птахів."

print("\nЗавдання 3: Перевірка правильності дешифрування")
print("\nПочатковий текст:", original_text)
print("\nДешифрований текст:", decrypted_text)

# Завдання 4: Аналіз частоти символів
from collections import Counter

def analyze_frequency(text):
    frequency_table = dict(Counter(text))
    total_characters = len(text)
    frequency_percentages = {char: count / total_characters * 100 for char, count in frequency_table.items()}
    return frequency_percentages

# Аналіз частоти символів у відкритому тексті та криптограмі
frequency_table_open_text = analyze_frequency(original_text)
frequency_table_ciphertext = analyze_frequency(ciphertext)

# Вивід результатів аналізу частоти символів
print("\nЗавдання 4: Аналіз частоти символів у відкритому тексті")
for char, percentage in frequency_table_open_text.items():
    print(f"Літера '{char}': {percentage:.2f}%")

print("\nЗавдання 4: Аналіз частоти символів у криптограмі")
for char, percentage in frequency_table_ciphertext.items():
    print(f"Символ '{char}': {percentage:.2f}%")