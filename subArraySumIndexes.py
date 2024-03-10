def subarraysumcheck(arr1,ln,sum):
    for i in range(0,ln):
        c_sum  = arr1[i]   # it is the cuurent sum 
        if c_sum == sum:
            print(f"sum found at index {i}")
            return
        else:
            for j in range(i+1,ln):
                c_sum = c_sum+arr1[j]
                if c_sum == sum:
                    print(f"sum found at indexes {i},{j}")
                    return
    print("sum not found in array")            
               
if __name__ == "__main__":
    array1  = [12,43,65,13,20]
    length = len(array1)
    sum = 33
    subarraysumcheck(array1,length,sum)                
                    
