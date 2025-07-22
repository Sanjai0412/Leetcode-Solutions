# Problem: Find the second largest distinct element in the array
#
# Approach:
# - Initialize `largest` and `second` with negative infinity.
# - Iterate through each number in the array:
#     - If number > largest → update second = largest, then largest = number.
#     - Else if number > second and number != largest → update second.
# - Return `second` if it was updated; otherwise return None.
#
# Handles cases where:
# - All elements are the same
# - Less than 2 elements in the list

def secondLargest(nums):
    largest = float('-inf')
    second = largest
    
    for num in nums:
        if num > largest:
            second = largest
            largest = num 
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

# Time Complexity: O(n)
# Space Complexity: O(1)



# or

def secondLarge(nums):
    nums.sort()
    return nums[-2]
