def encode(phraze, key):
    coded = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    key *= len(phraze)
    key = key.lower()
    phraze = phraze.lower()
    key = list(key)
    for i in range(len(phraze)):
        if phraze[i] == ' ':
            key.insert(i, ' ')
            coded.append(' ')
        else:
            a = alphabet.index(phraze[i])
            b = alphabet.index(key[i])
            if (a+b-1) >= 25:
                coded.append(alphabet[a+b-26])
            else:
                coded.append(alphabet[a + b])
    print(str(''.join(coded)))

code('programming is cool', 'laxar')