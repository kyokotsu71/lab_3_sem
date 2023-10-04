
units = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
tens = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
        15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
decades = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
           8: 'восемьдесят', 9: 'девяносто'}
hundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот',
            7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}

number = int(input("Введите число от 1 до 1000: "))

if number < 10:
    number_in_words = units[number]
elif number < 20:
    number_in_words = tens[number]
elif number < 100:
    decade = number // 10
    unit = number % 10
    if unit != 0:
        number_in_words = decades[decade] + ' ' + units[unit]
    else:
        number_in_words = decades[decade]
elif number < 1000:
    hundred = number // 100
    remainder = number % 100
    if remainder != 0:
        if remainder < 10:
            number_in_words = hundreds[hundred] + ' ' + units[remainder]
        elif remainder < 20:
            number_in_words = hundreds[hundred] + ' ' + tens[remainder]
        else:
            decade = remainder // 10
            unit = remainder % 10
            if unit != 0:
                number_in_words = hundreds[hundred] + ' ' + decades[decade] + ' ' + units[unit]
            else:
                number_in_words = hundreds[hundred] + ' ' + decades[decade]
    else:
        number_in_words = hundreds[hundred]
elif number == 1000:
    print('тысяча')
    exit()
else:
    number_in_words = 'Число должно быть от 1 до 1000'

print(number_in_words)