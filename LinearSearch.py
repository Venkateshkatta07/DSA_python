'''
Created on 23-Feb-2021

@author: Venky 07
'''

def linear_search(array,element):
    
    for i in array:
        if (i==element):
            return element
    
    return None


test_array=[]

for i in range (1,101):
    test_array.append(i)

#print(test_array)

print(linear_search(test_array, 56))
print(linear_search(test_array, 566))