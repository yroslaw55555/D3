from django import template
from pathlib import Path

# badWords = [w for w in Path('static\bad_Words.txt').read_text(encoding="utf-8").replace("\n", " ").split()]
badWords = []

with open('static/bad_Words.txt','r', encoding="utf-8") as f:
    for line in f:
        for word in line.split(', '):
           badWords.append(word)


register = template.Library() # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(


@register.filter(name='Censor')



def Censor(words):
    for word in badWords:
        for part in words.split():
            if word == part:
                words = words.replace(part, "####")
    return words


        # if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
    #     return str(value) * arg
    # else:
    #     raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку
