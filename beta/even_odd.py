# For a string S, print its even-indexed and odd-indexed characters

n = int(input().strip())

# with index
def print_even_odd_0(s_original):
    #even number starts at index 0 and continue bye 2 steps
    #odd number starts at 2end item and continue bye 2 steps
    print(s_original[::2], s_original[1::2])


#with loop and compare
def print_even_odd_1(s_original):
    s_even = s_original[0]
    s_odd = ''
    length = len(s_original)

    for i in range(1,length):
        if i%2 == 0:
            s_even +=s_original[i]
        else:
            s_odd += s_original[i]

    print(f'{s_even} {s_odd}')

# for i in range(n):
#     s = input()
#     print_even_odd_3(s)

# split a list  if even/odd with list comprehension
def print_even_odd_3(s_original):
    print([x for x in s_original if x%2 == 0], [x for x in s_original if x%2 != 0])

#print_even_odd_3([10, 33, 2, 5, 6, 7, 71])

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))