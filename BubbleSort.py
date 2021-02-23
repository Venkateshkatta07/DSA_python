'''
Created on 23-Feb-2021

@author: Venky 07
'''

def swap_elements(array,index_1,index_2):
    temp=array[index_1]
    array[index_1]=array[index_2]
    array[index_2]=temp


def bubble_sort(array):
    
    for i in range(0,len(array)):
        sorted_flag=False
        for j in range(len(array)-1-i):
            if (array[j]>array[j+1]):
                swap_elements(array,j,j+1)
                sorted_flag=True
        if(sorted_flag==False):
            break
    
    return array



test_array=[99, 6, 8, 2, 5, 7, 22, 87, 34, 76, 5]

print(test_array)
bubble_sort(test_array)

print(test_array)
