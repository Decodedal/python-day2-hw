# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(*args):
    return(max(args))

#print(max_num(5,10,2) )   

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(num_list):
    product = 1
    for number in num_list:
        product = product * number
    return product

#print(mult_list([5,2,1]))

# def recursive_mult_list(num_list, i = 0, product = 1):
#     if i = len(num_list):
#         return product
#     else:
        
# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

#print(rev_string("Dallas"))

# Write a Python function called num_within() to check whether a number falls in a given range.
#with iteration
def num_within(number,range_start, range_end):
    num_list = []
    for i in range(range_start,range_end + 1):
        num_list.append(i)
    return number in num_list

#print(num_within(3,1,10))  
#with recusion
def num_within_recursion(number,range_start, range_end):
    if range_end == range_start:
        return False
    elif number == range_start:
        return True
    else:
       return num_within_recursion(number, range_start + 1, range_end)        

print(num_within_recursion(2,1,10))
'''
 Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
 The function accepts the number n, the number of rows to print
 Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
'''

from math import factorial

def pascal(init_num):
  for i in range(init_num):
	  for j in range(i+1):
		  # nCr = n!/((n-r)!*r!)
		  print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	 # print each row in a new line
	  print("\n")

print(pascal(5))