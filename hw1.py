'''Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
'''
from functools import reduce

'''Задача №2
Написать точно такую же процедуру, но в декларативном стиле'''
def bubbleSortImperative(array, N):
    for i in range(N):
        for j in range(N-1-i):
            if array[j]<array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

array=[1,2,5,-3,5,0,8,10,332]
print(bubbleSortImperative(array,len(array)))

def sortDeclarative1(array, N):
    return sorted(array,reverse=True)

array=[1,2,5,-3,5,0,8,10,332]
print(sortDeclarative1(array,len(array)))

def sortDeclarative2(array, N):
    sorted_arr = reduce(
        lambda a, b: [x for x in a if x >= b] + [b] + [x for x in a if x < b],
        array,
        []
    )
    return sorted_arr

array=[1,2,5,-3,5,0,8,10,332]
print(sortDeclarative2(array,len(array)))

def swap(array,ii,jj):
    array[ii],array[jj]=array[jj],array[ii]

def sortDeclarative3(array, N):
    for i in range(N-1):
        if array[i]<array[i+1]:
            swap(array,i,i+1)
    if(N-1>1): sortDeclarative3(array,N-1)
    return array

array=[1,2,5,-3,5,0,8,10,332]
print(sortDeclarative3(array,len(array)))