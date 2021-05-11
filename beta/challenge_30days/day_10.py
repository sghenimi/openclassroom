n = int(input().strip())

def max_ones_0(val):
    print("####### builtIn : ", bin(n)[2:])

def max_ones_1(val):
    binary_str = ''
    # convert decimal to binary
    quotient = val
    while quotient != 0:
        reminder = quotient % 2
        binary_str =str(reminder) + binary_str
        quotient = quotient // 2
    # find the maximum number of consecutive One in the binary
    print(len(max(binary_str.split('0'))))

max_ones_0(n)
max_ones_1(n)







