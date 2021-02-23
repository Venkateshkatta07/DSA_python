'''
Created on 23-Feb-2021

@author: Venky 07
'''

def binary_search(array,element,start,end):
    
    
    mid=(start+end)//2
    print(start,end,mid)
    
    if (array[mid]==element):
        print("element is found")
        return mid
    
    elif(array[mid]<element):
        return binary_search(array, element, mid+1, end)
    
    elif(array[mid]>element):
        return binary_search(array, element, start, mid)
        
    #return None


test_array=[]

for i in range (1,101):
    test_array.append(i)
    
#print(test_array)
print(binary_search(test_array, 100,0,len(test_array)))
    