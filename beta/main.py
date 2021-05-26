# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def reverse(x):
    if x < 0:
        rev_x = -int(str(abs(x))[::-1])
    else:
        rev_x = int(str(abs(x))[::-1])

    if rev_x > 2**31-1 or rev_x < -2**31:
        return 0
    return rev_x


if __name__ == '__main__':
    print_hi('PyCharm')

    v = 1534236469 > 2**31-1
    print("VRAI : ", v)
    print(reverse(1534236469))

    print("without if : ", [x**3 for x in range(6)])
    print("with if : ", [x**3 for x in range(6) if x % 2 == 0])

    mytuple = ()
    mydict = {}
    mylist = []
    print("mytuple : ", type(mytuple))
    print("mydict : ", type(mydict))
    print("mylist : ", type(mylist))

    print("mylist : ", type(mylist))
    print("========================")
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)

    print(next(myit))
    print(next(myit))
    print(next(myit))
# Files
with open("files/sample.txt", "a") as fichier:
    fichier.write("quit ;D")
    print(fichier.read())
'''
Regular Expression
.     Le point correspond à n'importe quel caractère.
^     Indique un commencement de segment mais signifie aussi "contraire de"
$     Fin de segment
[xy]  Une liste de segment possibble. Exemple [abc] équivaut à : a, b ou c
(x|y) Indique un choix multiple type (ps|ump) équivaut à "ps" OU "UMP" 
\d    le segment est composé uniquement de chiffre, ce qui équivaut à [0-9].
\D    le segment n'est pas composé de chiffre, ce qui équivaut à [^0-9].
\s    Un espace, ce qui équivaut à [ \t\n\r\f\v].
\S    Pas d'espace, ce qui équivaut à [^ \t\n\r\f\v].
\w    Présence alphanumérique, ce qui équivaut à [a-zA-Z0-9_].
\W    Pas de présence alphanumérique [^a-zA-Z0-9_].
\     Est un caractère d'échappement
'''



