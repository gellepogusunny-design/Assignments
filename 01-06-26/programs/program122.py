def list_operations(x,y,n):
    return [num for num in range(x,y+1) if num%n==0]
print(list_operations(1,10,13))
