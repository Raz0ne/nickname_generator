import random

length = random.randint(5, 8)

vowels = ['e', 'y', 'u', 'i', 'o', 'a']
consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
alphabet = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'e',
            'y', 'u', 'i', 'o', 'a']

single = ['q', 'w', 'r', 't', 'p', 'y', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'v', 'b', 'n', 'm', 'u']

nickname = ''

for i in range(length):
    if i > 0 and nickname[i - 1] in single:  # 2 подряд идущих буквы
        alphabet = alphabet[:alphabet.index(nickname[i - 1])] + alphabet[alphabet.index(nickname[i - 1]) + 1:]

    if i > 1:
        if nickname[i - 1] in vowels and nickname[i - 2] in vowels:  # 2 гласные поряд
            alpha = random.choice(consonants)
        elif nickname[i - 1] in consonants and nickname[i - 2] in consonants:  # 2 согласные подряд
            alpha = random.choice(vowels)
        else:
            alpha = random.choice(alphabet)
    else:
        alpha = random.choice(alphabet)

    nickname += alpha

    if nickname[i - 1] not in alphabet:
        alphabet += nickname[i - 1]

print(nickname.title())
