from random import shuffle


def changeWord(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


    
words = ['babies', 'girls', 'boys']
anagrams = []

"""
## 1- with for loop
for word in words:
    anagrams.append(changeWord(word))


print(anagrams)


## 2- list Comprehension
print([changeWord(word) for word in words])

"""
## 3- Map method map(function, iterable)
print(tuple(map(changeWord, words )))
