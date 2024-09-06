
from itertools import count
from operator import concat
import string

def findSomeLetter(target):
    counter = 0;
    for i in range(0, len(someText)):
        if someText[i] == target:
            counter += 1
    return counter


def getFullInfo(character):
    return "[Target: '{target}'; Repitions: {repitions}; Unicode: {unicode}]".format(target = character, repitions = findSomeLetter(character), unicode = ord(character))


#Text for manipulations
someText = ("English culture is a rich tapestry woven from centuries of history, tradition, and innovation. " 
"Renowned for its contributions to literature, with iconic writers like Shakespeare and Austen, it has shaped global narratives. "
"The arts, including music, theater, and visual arts, hold a prominent place, with institutions like the Royal Academy and the West End showcasing the nation's talent. "
"English customs, such as afternoon tea and the love for cricket, reflect a unique blend of formality and leisure. "
"The countryside, with its rolling hills and quaint villages, embodies the idyllic charm that has inspired poets and artists alike.")

print(getFullInfo('y'))

#       ↑
#Konoplenko KN-33-1

result=string.capwords(someText)
print(result)
print("-----")
print(someText.isdigit())
print("-----")
result=someText.replace('English', 'Ukraine')
print(result)

#       ↑
#Duzhak Ivan KN-33-1
