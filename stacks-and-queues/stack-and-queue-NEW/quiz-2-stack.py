# Python3 program to reverse an integer using a stack 

# create stack
stack = []


# Function to push digits from integer into the stack

def push_digits(number):
    # while the number is not 0
    while number != 0:
        # add to the stack the modulus 10 of the number
        # which is the same as the last digit
        stack.append(number % 10)
        # divide number by 10 and convert to int to remove decimal numbers
        number = int(number / 10)
        # effectively removing the last digit in the number
        
# Function to reverse number by pulling it off the stack
def reverse_num(number):
    # call function that pushes digits to stack
    push_digits(number)
    
    # create variable to hold reversed number
    reverse = 0
    # set i equal to 1 for the power/coefficient
    i = 1
    
    # pop digits from stack to form reversed number
    while (len(stack) > 0):
        # update reversed number by adding the number on the top og the stack
        reverse = reverse + (stack[len(stack) - 1] * i)
        # remove the number from the top of the stack
        stack.pop()
        # increase i to the next power of 10/next higher decimal place
        i = i * 10
        
    # return the reversed number
    return reverse

# input number
number = 1234567


# Call and print function to reverse number
print(reverse_num(number))