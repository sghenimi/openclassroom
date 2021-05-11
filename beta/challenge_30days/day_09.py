
n = int(input().strip())
def get_factorial_with_recursion(n):
    factorial = lambda n: n if n <3 else n*factorial(n-1)
    print("with recursion : ", factorial(n))

def get_factorial_without_recursion(n):
    facto = 1
    for i in range(n,0, -1):
        facto *=i
    print("Without recursion", facto)
    print("2**8 : ", 2**8)
    print("2**32 : ", 2**32)
    
get_factorial_with_recursion(n)
get_factorial_without_recursion(n)


