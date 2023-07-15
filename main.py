import sys
message = sys.argv[1]


def caeserEncryption(key):
    encryptedMessage = ""
    for letter in message:                                                                # jeder Buchstabe wird einzeln verschlüsselt
        newletter = ord(letter) + key                                                     # Wert des verschlüsselten Buchstabens
        if not (ord('A') < newletter < ord('Z') or ord('a') < newletter < ord('z')):      # damit Encryption innerhalb des Alphabetes bleibt
            newletter = newletter -26

        encryptedMessage = encryptedMessage + chr(newletter)                              # Zusammenfügen der einzelnen Symbole zur verschlüsselten Nachricht

    return encryptedMessage


def bruteForceCaeser(encryptedText):
    lettersLower = "abcdefghijklmnopqrstuvwxyz"
    lettersUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for key in range(len(lettersLower)):                                # alle möglichen keys durchprobieren
        translated = ""
        for symbol in encryptedText:                                    # encryption wird für jedes einzelne Zeichen ausgeführt
            if symbol.islower():
                letters = lettersLower                                  # Alphabet mit kleinen Buchstaben
            else:
                letters = lettersUpper                                  # Alphabet mit großen Buchstaben
            if symbol in letters:
                num = letters.find(symbol)                              # Nummer des Symbols
                num = num - key
                if num < 0:                                             # wenn das 'a' erreicht ist weiter von 'z' runter zählen
                    num = num + len(letters)
                    translated = translated + letters[num]              # entschlüsseltes Symbol wird der Übersetzung hinzugefügt
                else:
                    translated = translated + letters[num]              # entschlüsseltes Symbol wird der Übersetzung hinzugefügt

        print('Key #%s: %s' % (key, translated))                        # Möglichen Entschlüsselungen werden geprinted, ein kurzer Blick über die Ausgabe und man
                                                                        # sieht welcher Text der Originaltext ist und welcher Verschlüsselungskey verwendet wurde.


if __name__ == '__main__':
    key = 2
    print("Die verschlüsselte Nachricht lautet: " + caeserEncryption(key) + "\n")
    bruteForceCaeser(caeserEncryption(key))