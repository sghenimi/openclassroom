import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

un_panda = [
    100,
    5,
    20,
    80,
]
un_panda_numpy = np.array(un_panda)


def cammenbert():
    ages = [
        25,
        65,
        26,
        26,
        46,
        37,
        36,
        36,
        28,
        28,
        57,
        37,
        48,
        48,
        37,
        28,
        60,
        25,
        65,
        46,
        26,
        46,
        37,
        36,
        37,
        29,
        58,
        47,
        47,
        48,
        48,
        47,
        48,
        60,
    ]

    fig, ax = plt.subplots()
    ax.hist(ages)
    plt.show()


class MyIterator:
    def __init__(self):
        print("we start at 5 : ")
        self.i = 5

    def __iter__(self):
        print(" iter it self : ")
        return self

    def __next__(self):
        print("the next element : ")
        self.i += 5
        if self.i >= 25:
            raise StopIteration()
        return self.i


for x in MyIterator():
    print(x)

big_data = """Le sénateur """
"""
dont il a été parlé plus haut, était un homme entendu qui 
    avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font 
    obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à 
    son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt. 
    C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant 
    tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à 
    des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes 
    aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré 
    pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun.
    [...]
    (Les Misérables, Victor Hugo)
    """


def is_part_of_a_word(character):
    res = len(re.findall("\w", character, flags=re.UNICODE))
    print(f"is_part_of_a_word : {res}")
    return res


def filter_by_size(words):
    return (w for w in words if len(w) >= 6)


def filter_by_letters(words):
    return (w for w in words if "a" in w)


def get_words_v0(text):
    print("Je commence à lire le texte maintenant : ")
    words = []
    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":
                words += [current_word]
                current_word = ""
        else:
            current_word += character
    return words


def get_words_v1(text):
    print("Je commence à lire le texte maintenant")

    words = []
    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":

                # code ajouté v1:
                if len(current_word) >= 6:
                    if "a" in current_word:
                        # fin du code ajouté

                        words += [current_word]
                current_word = ""
        else:
            current_word += character
    return words


def get_words(text):
    print("Je commence à lire le texte maintenant")

    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":
                print(f"not part of word  : {current_word}")
                yield current_word
                current_word = ""
        else:
            current_word += character
            print(f"yes part of word : {current_word}")


words = get_words(big_data)
words = filter_by_size(words)
words = filter_by_letters(words)
print("'words' est encore un générateur. Le texte n'a toujours pas été lu")

print("L'opération suivante va lancer la lecture du texte: ")
[w for w in words]


words = get_words(big_data)
print(words)

words = get_words(big_data)
# print("Nombre de mots: %i" % len(words))
words = filter_by_size(words)
# print("Nombre de mots: %i" % len(words))
words = filter_by_letters(words)
# print("Nombre de mots: %i" % len(words))
# print(words)

print("'words' est encore un générateur. Le texte n'a toujours pas été lu")

print("L'opération suivante va lancer la lecture du texte: ")
print([w for w in words])
