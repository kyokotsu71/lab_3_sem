print('Вот вопросы')

score = 0

q1 = int(input('Сколько часов в день Вы спите?\n 1. 0-2 2. 2-6 3. 6 - ∞: '))
if q1 == 3:
    score += 2
elif q1 == 2:
    score += 1

q2 = int(input('Любите ли Вы читать?\n 1. Да 2. Не особо 3. 6 - Нет: '))
if q2 == 1:
    score += 2
elif q2 == 2:
    score += 1

q3 = int(input('Смотрите ли Вы аниме или читаете ли мангу?\n 1. Да 2. Нет 3. Каво?: '))
if q3 == 1:
    score += 2
elif q3 == 2:
    score += 0.01
elif q3 == 3:
    score += 0

q4 = int(input('Ваши любимые жанры?\n 1. Триллеры, хорроры 2. Сёнены и всё подобное 3. Комедия, '
               'романтика : '))
if q4 == 3:
    score += 1.5
elif q4 == 2:
    score += 1.8
elif q4 == 1:
    score += 0.8

q5 = int(input('Как бы Вы поступили на месте Ю Бина?\n 1. соль 2. не соль 3. не ушел бы вообще: '))
if q5 == 3:
    score += 2
elif q5 == 2:
    score += 1
elif q5 == 1:
    score = -10000


if 3 >= score > 0:
    print('Вы - дефолтный обитатель нашего мира')
elif score > 4:
    print('Вы - добротный кобольд')
elif score < 0:
    print('Вы - солевой король! FBBlock FBBlock FBBlock')