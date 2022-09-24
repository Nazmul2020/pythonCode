def swap(a,b):
    return b,a

    

def selectionSort(list):
    for i in range(len(list)):
        key = i
        for j in range(i,len(list)-1):
            if(list[key]>list[j+1]):
                key = j+1
        list[i],list[key] = swap(list[i],list[key])

list = [int(item) for item in input().split()]

selectionSort(list)

print(list)
