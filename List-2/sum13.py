# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

def sum13(nums):
    index = result = 0
    while index < len(nums):
        n = nums[index]
        if n == 13:
            index += 2
        else:
            result += n
            index += 1
    return result
