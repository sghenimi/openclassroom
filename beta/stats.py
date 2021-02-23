import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

un_panda = [100,5, 20, 80,]
un_panda_numpy = np.array(un_panda)

def cammenbert():
    ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
       25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

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


