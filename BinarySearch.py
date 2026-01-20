nums = [1, 3, 5, 2, 9]

def BinarySearch(self, inputArray, target):
    inputArray = sorted(inputArray)
    l, r = nums[0], nums[len(nums)]
    
    while l < r:
        current = (r - l) // 2
        if current < target:
            r = current
        elif current > target:
            l = current
        elif current == target:
            return current
        else:
            return -1
    return


        
