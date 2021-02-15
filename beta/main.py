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





# Press the green button in the gutter to run the script.
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




# See PyCharm help at https://www.jetbrains.com/help/pycharm/


