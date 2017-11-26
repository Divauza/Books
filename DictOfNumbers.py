units = [
    [u'ноль'],
    [u'один', u'два', u'три', u'четыре', u'пять', u'шесть', u'семь', u'восемь', u'девять'],
    [u'одна', u'две'],
]

teens = [
    u'десять', u'одиннадцать',
    u'двенадцать', u'тринадцать',
    u'четырнадцать', u'пятнадцать',
    u'шестнадцать', u'семнадцать',
    u'восемнадцать', u'девятнадцать'
]

tens = [
    u'двадцать', u'тридцать',
    u'сорок', u'пятьдесят',
    u'шестьдесят', u'семьдесят',
    u'восемьдесят', u'девяносто'
]

hundreds = [
    u'сто', u'двести',
    u'триста', u'четыреста',
    u'пятьсот', u'шестьсот',
    u'семьсот', u'восемьсот',
    u'девятьсот'
]

orders = [
    [u'тысяча', u'тысячи', u'тысяч'],
    [u'миллион', u'миллиона', u'миллионов'],
    [u'миллиард', u'миллиарда', u'миллиардов'],
]

def fromStringNumber(str):
    args = str.split(' ')
    start = 0 #конечный автомат
    answ = 0
    curNumber = 0
    indexArgs = 0
    while (indexArgs < len(args)):
        if (start == 0):
            if args[indexArgs] in hundreds:
                for i in range(0, len(hundreds)):
                    if (args[indexArgs] == hundreds[i]):
                        curNumber = curNumber + (i + 1) * 100
                        indexArgs = indexArgs + 1
                        break
            start = 1
            continue

        if (start == 1):
            if (args[indexArgs] in teens):
                for i in range(0, len(teens)):
                    if (args[indexArgs] == teens[i]):
                        curNumber = curNumber + (i + 10)
                        indexArgs = indexArgs + 1
                        break
                start = 10
                continue

            if (args[indexArgs] in tens):
                for i in range(0, len(tens)):
                    if (args[indexArgs] == tens[i]):
                        curNumber = curNumber + (i + 2) * 10
                        indexArgs = indexArgs + 1
                        break
            start = 2
            continue

        if (start == 2):
            if (args[indexArgs] in units[1]):
                for i in range(0, len(units[1])):
                    if (args[indexArgs] == units[1][i]):
                        curNumber = curNumber + (i + 1)
                        indexArgs = indexArgs + 1
                        break
                start = 10
                continue

            if (args[indexArgs] in units[2]):
                for i in range(0, len(units[2])):
                    if (args[indexArgs] == units[2][i]):
                        curNumber = curNumber + (i + 1)
                        indexArgs = indexArgs + 1
                        break
                start = 10
                continue
            start = 10
            continue

        if (start == 10):
            if (args[indexArgs] in orders[0]):
                curNumber = curNumber * 1000
            if (args[indexArgs] in orders[1]):
                curNumber = curNumber * 1000000
            if (args[indexArgs] in orders[2]):
                curNumber = curNumber * 1000000000
            indexArgs = indexArgs + 1
            start = 0

    return curNumber

print(fromStringNumber('сто сорок одна тысяча девяносто три'))

