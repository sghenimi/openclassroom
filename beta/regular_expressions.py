import re
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
val = re.match(r"GR(.)?S", "GRIS")
print("result : ", val)

s = """date 0 : 14/9/2000
    date 1 : 20/04/1971     date 2 : 14/09/1913     date 3 : 2/3/1978
    date 4 : 1/7/1986     date 5 : 7/3/47     date 6 : 15/10/1914
    date 7 : 08/03/1941     date 8 : 8/1/1980     date 9 : 30/6/1976"""

# première étape : construction
expression = re.compile("([0-3]?[0-9]/[0-1]?[0-9]/([0-2][0-9])?[0-9][0-9])")
# seconde étape : recherche
res = expression.findall(s)
print(res)