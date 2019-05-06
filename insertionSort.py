import unittest
import random
from time import time
import matplotlib.pyplot as plt

class TestInsertionSort(unittest.TestCase):
    def testSort(self):
        data = [7,8,1,4,2,5,3]
        insertionSort(data)
        self.assertListEqual(data,[1,2,3,4,5,7,8])

def insertionSort(data):
    for j in range(1,len(data)):
        i=j-1
        key=data[j]
        while i>=0 and data[i]>key:
            data[i+1]=data[i]
            i=i-1
        data[i+1]=key

def plot():
    print("Calculating . . .please wait")
    exeTime_dic = {}
    for i in range (500,10000,1000):
        randomValue = random.sample(range(i),i)
        start=time()
        insertionSort(randomValue)
        end=time()
        calc=end-start
        exeTime_dic[i] = calc
    exeTime = list(exeTime_dic.values())
    inpSize = list(exeTime_dic.keys())
    plt.plot(inpSize, exeTime)
    plt.xlabel('Input Size(n)')
    plt.ylabel('Execution Time (sec)')
    plt.title("Insertion Sort")
    plt.xticks(inpSize)
    plt.yticks(exeTime)
    plt.show()

data = [7,8,1,4,2,5,3]
insertionSort(data)
plot()

#To Test Insertion Sort Uncomment Below Two code and Comment code outside function

# if __name__ == '__main__':
#    unittest.main()
