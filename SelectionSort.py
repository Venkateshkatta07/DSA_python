'''
Created on 23-Feb-2021

@author: Venky 07
'''

def swap_elements(array,index_1,index_2):
    temp=array[index_1]
    array[index_1]=array[index_2]
    array[index_2]=temp


def selection_sort(array):
    
    for i in range(0,len(array)):
        temp_min=array[i]
        min_index=i
        for j in range(i,len(array)):
            if(array[j]<temp_min):
                temp_min=array[j]
                min_index=j
        
        #print("minimum is "+str(array[min_index]))
        
        swap_elements(array, i, min_index)
    
    
    return array


test_array=[99,6,8,2,5,7,22,87,34,76,5]

print(test_array)
selection_sort(test_array)

print(test_array)