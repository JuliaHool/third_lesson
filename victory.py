import random

name_a, data1 = 'Микела́нджело Буонарро́ти', '06.03.1475'  # 1
name_b, data2 = 'Леона́рдо да Ви́нчи', '15.04.1452'  # 2
name_c, data3 = 'Винсе́нт Ви́ллем ван Гог', '30.03.1853'  # 3
name_d, data4 = 'Сальвадо́р Дали́', '11.05.1904'  # 4
name_e, data5 = 'Пабло Пикассо', '25.10.1881'  # 5
name_f, data6 = 'Клод Моне', '14.11.1840 '
name_g, data7 = 'Рембрандт Ван Рейн', '15.07.1606'
name_h, data8 = 'Микеланджело Буонарроти', '06.03.1475'
name_i, data9 = 'Иван Айвазовский', '29.07.1817'
name_j, data10 = 'Питер Пауль Рубенс', '28.06.1577'
days = {'06': 'шестое', '30': 'тридцатое', '11': 'одиннадцатое', '25': 'двадцатьпятое', '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '29': 'двадцатьдевятое', '28': 'двадцатьвосьмое'}
months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
          '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
day1, month1, year1 = data1.split('.')
day2, month2, year2 = data2.split('.')
day3, month3, year3 = data3.split('.')
day4, month4, year4 = data4.split('.')
day5, month5, year5 = data5.split('.')
day6, month6, year6 = data6.split('.')
day7, month7, year7 = data7.split('.')
day8, month8, year8 = data8.split('.')
day9, month9, year9 = data9.split('.')
day10, month10, year10 = data10.split('.')
artist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
correctCount = 0
incorrectCount = 0
while True:
    result = random.sample(artist, 5)
    if 1 in result:
        print('Введите дату рождения', name_a, end='. ')
        name_answer1 = input('В формате dd.mm.yyyy:')
        if name_answer1 != data1:
            print(days[day1], months[month1], year1, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 2 in result:
        print('Введите дату рождения', name_b, end='. ')
        name_answer2 = input('В формате dd.mm.yyyy:')
        if name_answer2 != data2:
            print(days[day2], months[month2], year2, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 3 in result:
        print('Введите дату рождения', name_c, end='. ')
        name_answer3 = input('В формате dd.mm.yyyy:')
        if name_answer3 != data3:
            print(days[day3], months[month3], year3, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 4 in result:
        print('Введите дату рождения', name_d, end='. ')
        name_answer4 = input('В формате dd.mm.yyyy:')
        if name_answer4 != data4:
            print(days[day4], months[month4], year4, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 5 in result:
        print('Введите дату рождения', name_e, end='. ')
        name_answer5 = input('В формате dd.mm.yyyy:')
        if name_answer5 != data5:
            print(days[day5], months[month5], year5, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 6 in result:
        print('Введите дату рождения', name_f, end='. ')
        name_answer6 = input('В формате dd.mm.yyyy:')
        if name_answer6 != data6:
            print(days[day6], months[month6], year6, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 7 in result:
        print('Введите дату рождения', name_g, end='. ')
        name_answer7 = input('В формате dd.mm.yyyy:')
        if name_answer7 != data7:
            print(days[day7], months[month7], year7, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 8 in result:
        print('Введите дату рождения', name_h, end='. ')
        name_answer8 = input('В формате dd.mm.yyyy:')
        if name_answer8 != data8:
            print(days[day8], months[month8], year8, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 9 in result:
        print('Введите дату рождения', name_i, end='. ')
        name_answer9 = input('В формате dd.mm.yyyy:')
        if name_answer9 != data9:
            print(days[day9], months[month9], year9, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    if 10 in result:
        print('Введите дату рождения', name_j, end='. ')
        name_answer10 = input('В формате dd.mm.yyyy:')
        if name_answer10 != data1:
            print(days[day10], months[month10], year1, 'года')
            incorrectCount += 1
        else:
            correctCount += 1
    print('Количество верных ответов:', correctCount)
    print('Количество неверных ответов:', incorrectCount)

    answer = input('Начнем сначала?')
    if answer == 'нет':
        break
