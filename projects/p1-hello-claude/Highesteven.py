# Write a function called highest_even that takes a list of numbers as input and returns the highest even number in the list. If there are no even numbers, the function should return None.
#1. Define the function highest_even that takes a list of numbers as an argument.
#2. Create an empty list called evennumbers to store the even numbers from the input list
#3. Loop through each number in the input list:
#   a. Check if the number is even (i.e., num % 2 == 0).
#   b. If it is even, append it to the evennumbers list.
#4. After the loop, check if the evennumbers list is empty - this is a guard clause to handle the case where there are no even numbers in the input list.
#   a. If it is empty, return None (indicating there are no even numbers
#   b. If it is not empty, return the maximum value from the evennumbers list using the max() function.

def highest_even(li):
    evennumbers = []
    for num in li:
        if num % 2 == 0:
            evennumbers.append(num)
    if len(evennumbers) == 0:
        return None
    else: return(max(evennumbers))

print(highest_even([25,26,3,8,49,56]))

