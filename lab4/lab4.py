import random

# функція створює новий "шифрований" алфавіт, перемішуючи вхідний алфавіт
def cipheredAlphabet(abc, abcLength):
    cipheredAbc = [[], []]
    for i in range(abcLength):
        index = random.randint(0, len(abc) - 1)
        cipheredAbc[0].append(abc[index])
        cipheredAbc[1].append(i)
        abc.pop(index)
    return cipheredAbc

# функція застосовує метод модулярної інгібіції до вхідного рядка з ключем
def ModularInhibition(line, key, abc, spec):
    cipheredLine, k = "", 0
    for i in range(len(line)):
        if k >= 6: k = 0
        numCiphered = abc[1][abc[0].index(line[i].lower())] + spec * abc[1][abc[0].index(key[k])]
        if numCiphered > len(abc[0]) - 1: numCiphered -= len(abc[0])
        cipheredLine += abc[0][numCiphered]
        k += 1
    return cipheredLine

# функція відповідає за запис рядка 
def writeFile(line, fileName, type):
    with open(fileName, type) as file: file.write(line)
    file.close()


# функція виводить на екран інформацію про вхідний текст, зашифрований текст, дешифрований текст і ключ
def printMessage(line, cipheredLine, encryptedLine, key):
    print("\nЗашифрований текст:\n" + cipheredLine + 
          "\n\nДешифрований текст:\n" + encryptedLine + 
          "\n\nВідкритий текст:\n" + line + "\n\nГама: " + key + "\n")


alphabet = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р",
            "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
randomAlphabet, gamma = cipheredAlphabet(alphabet.copy(), len(alphabet)), "колізей"
text = "вулицясоловївськамаєсвійпочатокщеізчасівпанщинистаршілюдиговорятьщоназвудалитакуботутгніздилосябагатосоловївівліткувсявулицянаповнюваласяспівомцихдивовижнихптахів"

writeFile(text + "\n", "cipheredText.txt", "w")
cipheredText = ModularInhibition(text, gamma, randomAlphabet, 1)
writeFile(cipheredText, "cipheredText.txt", "a")
encryptedText = ModularInhibition(cipheredText, gamma, randomAlphabet, -1)
printMessage(text, cipheredText, encryptedText, gamma)
