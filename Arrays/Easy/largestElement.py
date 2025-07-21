# Problem: Find the largest element in the array

# Approach:
# - Initialize a variable `largest` with negative infinity.
# - Iterate through the array and compare each element with `largest`.
# - Update `largest` if a bigger element is found.
# - Return `largest`.

def findLargest(nums):
    largest = float('-inf')
    for num in nums:
        if num > largest:
            largest = num
    return largest

# One-liner using built-in function
def findLarge(nums):
    return max(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)  