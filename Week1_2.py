# case 1
# a = [3,1,9,7,5,2,6,8,4]

# case 2
a = [1, 6, 3, 2, 7, 9]

L = [0] * len(a)
R = [0] * len(a)

def divide(array):
    
    # base case
    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    
    L_side = divide(array[:mid])
    R_side = divide(array[mid:])
    
    return merge(L_side, R_side)
    
def merge(sub_array_one, sub_array_two):
    
    global L,R
    
    A = []

    i = 0 
    j = 0
   
    # needed to be sort
    while (i < len(sub_array_one) and j < len(sub_array_two)):
        if sub_array_one[i] <= sub_array_two[j]:
            A.append(sub_array_one[i])
            R[a.index(sub_array_one[i])] += j
            i += 1
        elif sub_array_one[i] > sub_array_two[j]:
            A.append(sub_array_two[j])
            L[a.index(sub_array_two[j])] += i 
            j += 1 
            
    while (i < len(sub_array_one)):
        A.append(sub_array_one[i])
        R[a.index(sub_array_one[i])] += j
        i += 1
    while (j < len(sub_array_two)):
        A.append(sub_array_two[j])
        L[a.index(sub_array_two[j])] += i
        j += 1
        
    return A 
    
if __name__ == "__main__":
    sort = divide(a)
    print(sort)
    print(a)
    print(L)
    print(R)



