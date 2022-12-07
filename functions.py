"""
Name: Mr. C
Title: Live-coding Notes on Functions
Description: Defining functions, calling functions, and returning values.
"""

# FUNCTION - a mini-program that accomplishes some task and may return a value.

# function definition (creates a function; does not run it)
def welcome():	# function header
	print("Welcome to the program.") # function body

welcome()  # function call
welcome()
welcome()
print()

message = "Hello, world"

# ARGUMENT - value passed into the parentheses of a function call
# PARAMETER - variable used to accept arguments in a function; only exists inside the funciton body
def excited_print(param):  # 'param' variable is the parameter
	print(str(param) + "!!!!!!!!!!!!!!!")

excited_print(message)  # 'message' is the argument
excited_print("Yay")

#print(param)  # 'param' variable only exists inside function definition

# Challenge: Write a function that can print any word in pig latin (prints the first letter at the end of the word and adds "ay")  e.g. "pig" --> "igpay"
def pig_print(word):
	print(word[1:] + word[0] + "ay")

pig_print("pig")
pig_print("latin")

# RETURN VALUE - value received back from a function call
# DOCSTRING - first line of a function definition to document the purpose and uses of the function (uses a triple-quoted string)
def avg(seq):
	"""Accepts a sequence of numbers (seq) and returns the average."""
	total = 0
	for num in seq:
		total += float(num)
	average = total/len(seq)
	return average

print(avg([1,2,3,4,5,6,7,8,9,10]))

nums = (2, 4, 6, 8, 10, 12)
nums_avg = avg(nums)
print(nums_avg)

# CHALLENGE: Write functions to find the lowest number of an unsorted list of numbers and the highest number.
def min(nums):
	"""Returns the lowest number from a list of unsorted numbers"""
	nums = list(nums)
	nums.sort()
	low = nums[0]
	return low

def max(nums):
	"""Returns the highest number from a list of unsorted numbers"""
	nums = list(nums)
	nums.sort()
	high = nums[-1]
	return high

print(nums)
print("Min:", min(nums))
print("Max:", max(nums))
