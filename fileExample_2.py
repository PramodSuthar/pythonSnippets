from random import randint

names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn","Liam", "Noah","William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Owen"]

def textGenerator(word):
    randomPosition = randint(0, len(names)-1 )
    return f"{word} {names[randomPosition]}"


nbParagrph = int(input('How many paragraphs you need: '))

with open('example_2.txt') as rf:
    list_of_words = rf.read().split();
    ##print(list_of_words)
    for n in range(nbParagrph):
        new_generated_list = list(map(textGenerator, list_of_words))
        with open('./output.txt', 'a') as personFile:
            personFile.write(' '.join(new_generated_list) + '\n\n')
