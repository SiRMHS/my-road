def search(list , target):
    first = 0
    last = len(list) - 1  
    while first <= last :
        midpoint = (first+last)//2
        if list[midpoint] == target: 
            return target
        elif list[midpoint] < target :
            first = midpoint + 1
            return first
        else:
            last = midpoint - 1
            
    return None

def verify(index):
    if index is not None :
        print("founded in index : " , index)
    else:
        print("not found")


number = [1,2,3,4,5,6,7,8,9,10]

moz = search(number,6)
verify(moz)