"""We create any function in python by using the def command, any functions in python programming
are just created and collected in one file, written by random developers like you or me
below is how some small functions can be used"""

#Lets learn how to create or write a program that does some mathematics or anything
#Lets have a program that works as a calculator by adding numbers together
#from the input user using the input command
print("Program 1")
#boserve below that when you type colon and enter, a,b DO NOT start on the same
#line as def or from margin, that is called-INDENT, so entire block is indented
#and thats the nature of the programming language, try remooving the space before a or b
#and see what will happen if you run the program
def add_numbers():
    # a, b are the random number you choose when the program asks you
    a = float(input("\nplease enter the number of a="))
    b = float(input("please enter the number of b="))
    Answer = a+b      #created a variable Answer to be printed out
    print("\nThe Answer =", Answer)
add_numbers()

def multiply_numbers():
    # a, b are the random number you choose when the program asks you
    a = float(input("\nplease enter the number of a="))
    b = float(input("please enter the number of b="))
    Answer = a*b      #created a variable Answer to be printed out
    print("\nThe Answer =", Answer)
multiply_numbers()

#
def maths_program():
    x = float(input("\nplease enter the number of x="))
    y = float(input("please enter the number of y="))
    z = x*y/(x**2+y**2)
    """z is equal to x times y everything over or divide by brackets
    x-squared plus or add y-squared brackets"""
    print("\nThe Value of Z =",z)
maths_program()

#YOUR TASK BELOW
"""1-write a function following the above procedure, but this function has to divide a by b (a/b)
These numbers must be choices input by the user"""