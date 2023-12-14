def linear_search(list,target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
        
        
def verify(index):
    if index is not None:
        print("founded :)" , index )
    else:
        print("not found" , index)

numb = [1,2,4,5,6,7,8]

Result = linear_search(numb, 2)
verify(Result)