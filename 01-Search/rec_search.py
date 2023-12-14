def search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
    
        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return search(lst[midpoint + 1:], target)
            else:
                return search(lst[:midpoint], target)

def verify(index):
    print("founded", index)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = search(num, 4)

verify(result)