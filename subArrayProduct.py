def subarrayproduct(arr1,n,product):
    for i in range(0,n):
        cuur_product = arr1[i]
        if cuur_product == product:
            print("Product found at index",i)
            return
        else:
            for j in range(i+1,n):
                cuur_product = cuur_product * arr1[j]
                if cuur_product == product:
                    print("Product found at indexes",i,j)    
                    return
    print("product not found")
    
if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8]
    n = len(arr1)
    product = 12
    subarrayproduct(arr1,n,product)                
                    
                    
