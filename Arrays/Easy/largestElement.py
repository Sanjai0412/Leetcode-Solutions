
# Find the largest element in the array

def findLargest(nums):
    largest = float('-inf')
    
    for num in nums:
        if num > largest:
            largest = num
    return largest

# or

def findLarge(nums):
    return max(nums)
