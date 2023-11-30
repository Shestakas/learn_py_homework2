# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

letter = set('а')

def entry(word, set_let):
    count = 0
    for strng in word.lower():
        if strng in set_let:
            count +=1
    return count

print(f'Количество букв "а" в слове {word} - {entry(word.lower(), letter)}')

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set("аеиоуыэюя")

print(f'Количество гласных букв в слове {word} - {entry(word.lower(), vowels)}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

def split_word(word):
    return word.split(' ')

print(f'Количество слов в предложении - {len(split_word(sentence))}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
x = [print(x[0]) for x in split_word(sentence)]


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
x = [len(x) for x in split_word(sentence)]
print(f'Усреднённая длина слова в предложении - {sum(x)/len(x)}')

