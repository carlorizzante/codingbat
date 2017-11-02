# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
# in the array somewhere.

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i]+2 == nums[i+1]+1 == nums[i+2]:
            return True
    return False
