id = [1, 6, 3, 7, 2, 9]
miles = [400, 100, 200, 150, 50, 300]

over_used = 0

def divide(array):
    
    # base case
    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    
    L_side = divide(array[:mid])
    R_side = divide(array[mid:])
    
    return merge(L_side, R_side)
    
def merge(sub_array_one, sub_array_two):
    
    global over_used
    
    A = []

    i = 0 
    j = 0
   
    # needed to be sort
    while (i < len(sub_array_one) and j < len(sub_array_two)):
        if sub_array_one[i] < sub_array_two[j]:
            A.append(sub_array_one[i])
            if miles[id.index(sub_array_one[i])] > miles[id.index(sub_array_two[j])]:
                over_used += 1
            i += 1
        elif sub_array_one[i] > sub_array_two[j]:
            A.append(sub_array_two[j])
            if miles[id.index(sub_array_one[i])] < miles[id.index(sub_array_two[j])]:
                over_used += 1
            j += 1 
            
    while (j < len(sub_array_two)):
        A.append(sub_array_two[j])
        if miles[id.index(sub_array_one[i-1])] > miles[id.index(sub_array_two[j])]:
            over_used += 1
        j += 1
    while (i < len(sub_array_one)):
        A.append(sub_array_one[i])
        if miles[id.index(sub_array_one[i])] < miles[id.index(sub_array_two[j-1])]:
            over_used += 1
        i += 1
        
    return A 
    
if __name__ == "__main__":
    sorted = divide(id)
    print(sorted)
    print(over_used)



