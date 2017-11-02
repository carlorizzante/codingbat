# Given an array of ints, return True if one of the first 4 elements in the
# array is a 9. The array length may be less than 4.

def array_front9(nums):
    count = 0
    for n in nums[:4]:
        if n == 9:
            count += 1
    return count > 0
