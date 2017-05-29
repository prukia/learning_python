#
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

# Declare a variable and initialize it
f = 0;
print f

# line 6 declares a variable
# line 7 prints the value of the variable (f)

# re-declaring the variable works
# f = "abc"
# print f
# redeclaring the variable f has a string

# print "string type " + 123

# TypeError: cannot concatenate 'str' and 'int' objects
# you get the above error cuz python is a "strongly typed language"
# you can't combine different types.

print "string type " + str(123)
# using python's built-in function "str" to convert it into a string
# so now you have a string + a string
# result: string type 123


# Global vs. local variables in functions
def someFunction():
  #global f
  global f
  f = "def"
  print f
someFunction()
print f
#defining a function and indenting it by 2 lines to say it's part of the function
# you have to tell the function it is a global variable  by saying "global"
# def is being printed twice because now it is a global variable
del f
print f

# deleted the definition of a variable that was previously declared
# you can undefine variables in real time by using del 
