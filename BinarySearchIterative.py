nums = [1, 3, 5, 2, 9]
# my brain is so smooth
def BinarySearch(inputArray, target):
    inputArray = sorted(inputArray)
    l, r = 0 , len(inputArray) - 1
    
    while l <= r:
        current = (l + r) // 2
        if inputArray[current] < target:
            l = current + 1
        elif inputArray[current] > target:
            r = current - 1
        elif inputArray[current] == target:
            return current
    return -1

print(BinarySearch(nums, 9))

        
