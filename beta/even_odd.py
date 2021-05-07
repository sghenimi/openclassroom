# cracking-Coding-Interview
# www.codingame.com
# https://the-algorithms.com/
# https://leetcode.com/
# https://adventofcode.com/

n = int(input().strip())
    
def print_even_odd_0(s_original):
    print(s_original[::2], s_original[1::2])


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

for i in range(n):
    s = input()
    print_even_odd_0(s)