

def bubbleSort(l):
        for i in range(len(l)):
                for j in range(i,len(l)-1):
                        if(l[i]>l[j+1]):
                                temp = l[j+1]
                                l[j+1] = l[i]
                                l[i] = temp
        return l
                


list = [int(item) for item in input().split()]
print(bubbleSort(list))

