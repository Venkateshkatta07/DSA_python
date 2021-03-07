'''
Created on 23-Feb-2021

@author: Venky 07
'''
def merge(array_1,array_2):
    i=0
    j=0
    result_array=[]
     
    while(i<len(array_1) and j<len(array_2)):
        if(array_1[i]<=array_2[j]):
            result_array.append(array_1[i])
            i+=1
        else:
            result_array.append(array_2[j])
            j+=1
    while(i<len(array_1)):
        result_array.append(array_1[i])
        i+=1
    while(j<len(array_2)):
        result_array.append(array_2[j])
        j+=1
      
    return result_array

def merge_sort(array):
    
    if (len(array))>1:
        mid =(len(array))//2
        
        left_array=array[:mid]
        right_array=array[mid:]
        
        #print("left and right arrays  before : " ,left_array,right_array)
        
        m=merge_sort(left_array)
        n=merge_sort(right_array)
        #print("left and right arrays afer : " ,m,n)
        #print(" after sorting the list is : " ,merge(m, n))
        
        return merge(m, n)
    else:
        return array
    
test_array=[99, 6, 8, 2, 5, 7, 22, 87, 34, 76, 5]
print(test_array)
#merge_sort(test_array)
print(merge_sort(test_array))


#print(merge(a1, a2))