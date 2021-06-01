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
#print(res)

# MATCH
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

# SEARCH
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1)) : ", searchObj.group(1))
   print("searchObj.group(2)) : ", searchObj.group(2))
else:
   print("Nothing found!!")

str = 'an example word:cat!!'
is_match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if is_match:
  print('found', is_match.group()) ## 'found word:cat'
else:
  print('did not find')

## Search for pattern 'iii' in string 'piiig'.
  ## All of the pattern must match, but it may appear anywhere.
  ## On success, match.group() is matched text.
  match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
  match = re.search(r'igs', 'piiig') # not found, match == None

  ## . = any char but \n
  match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

  ## \d = digit char, \w = word char
  match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
  match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"

## i+ = one or more i's, as many as possible.
  match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

  ## Finds the first/leftmost solution, and within it drives the +
  ## as far as possible (aka 'leftmost and largest').
  ## In this example, note that it does not get to the second set of i's.
  match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

  ## \s* = zero or more whitespace chars
  ## Here look for 3 digits, possibly separated by whitespace.
  match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
  match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
  match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

  ## ^ = matches the start of string, so this fails:
  match = re.search(r'^b\w+', 'foobar') # not found, match == None
  ## but without the ^ it succeeds:
  match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"