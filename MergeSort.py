import random
import unittest
from time import time
import matplotlib.pyplot as plt

class TestMergeSort(unittest.TestCase):
    def testSort(self):
        data = [7,8,1,4,2,5,3]
        merge_sort(data)
        self.assertListEqual(data,[1,2,3,4,5,7,8])
def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
def plot():
    print("Calculating . . .please wait")
    exeTime_dic = {}
    for i in range (500,10000,1000):
        randomValue = random.sample(range(i),i)
        start=time()
        merge_sort(randomValue)
        end=time()
        calc=end-start
        exeTime_dic[i] = calc
    exeTime = list(exeTime_dic.values())
    inpSize = list(exeTime_dic.keys())
    plt.plot(inpSize, exeTime)
    plt.xlabel('Input Size(n)')
    plt.ylabel('Execution Time (sec)')
    plt.title("Merge Sort")
    plt.xticks(inpSize)
    plt.yticks(exeTime)
    plt.show()

data = [7,8,1,4,2,5,3]
merge_sort(data)
print(data)
plot()


#To Test Merge Sort Uncomment Below Two code and Comment code outside function

# if __name__ == '__main__':
#    unittest.main()
