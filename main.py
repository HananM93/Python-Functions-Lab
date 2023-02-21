'''
Challenges 

 1. Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n.
 For example:
 sum_to(6)  # returns 21
 sum_to(10) # returns 55
'''

def sum_to(n):
    return print(n * (n + 1) // 2)

sum_to(6)


'''
2. Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.

For example:

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231
'''

def largest(nums):
    largest_num = 0
    for num in nums:
        if num > largest_num:
            largest_num = num
    return print(largest_num)
    
    
largest([1, 2, 42, 4, 12])
