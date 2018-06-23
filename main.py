import os
import re
import DictOfNumbers
#test string
def getFullNextWord(startIndex, text):
    textFind = ''
    while text[startIndex] in [' ']:
        startIndex = startIndex + 1
    while (startIndex < len(text) and (text[startIndex].isalpha())):
        textFind = textFind + text[startIndex]
        startIndex = startIndex + 1
    return textFind

dict = {'метров' : [20, 'сантиметров']}

f = open("C:\\Users\\Zerg1\\PycharmProjects\\fb2\\1.fb2", 'r', encoding="UTF-8")
for line in f:
    Encoding = re.findall(r'encoding=".+"', line)[0]
    Encoding = Encoding.replace('encoding="', '')
    Encoding = Encoding.replace('"', '')
    break
f.close()
f = open("C:\\Users\\Zerg1\\PycharmProjects\\fb2\\1.fb2", 'r', encoding=Encoding)
for line in f:
    print(line)
    numbersInText = re.findall(r'\d+',line)
    for curNumber in numbersInText:
        indexCurNumber = line.find(curNumber)
        nextWord = getFullNextWord(indexCurNumber + len(curNumber), line)
        if dict.get(nextWord) is not None:
            line = line[ : indexCurNumber] + '1 ' + dict.get(nextWord)[1] + line[indexCurNumber + len(curNumber) + 1 + len(nextWord) : ]
            print (line)

