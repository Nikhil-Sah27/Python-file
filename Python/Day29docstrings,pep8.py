#Python Docstrings are strings used right after the definition of a function,method,class or module.
# we can access these Docstrings using the doc attribute


def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(6) 
print(square.__doc__) #(func name. double underscore doc double underscore)



def square(n):
    print(n**2)
    '''Takes in a number n, returns the square of n'''
    
square(6) 
print(square.__doc__)  #docstring is always just below the function definition



         # PEP8 (Python Enhancement Proposal)
#PEP8 is a document that provides guidlines and best practices on how to write python code.
#Its primary focus is to improve the readability and consistency of python code.
#Written in 2001 by Guido van Rossum,Barry Warsaw and Nick Coghlan.



             #The Zen of Python
#open trminal in your device
# type python
# type 'import this'
#then it will appear as:


#   Beautiful is better than ugly.
#   Explicit is better than implicit.
#   Simple is better than complex.
#   Complex is better than complicated.
#   Flat is better than nested.
#   Sparse is better than dense.
#   Readability counts.
#   Special cases aren't special enough to break the rules.
#   Although practicality beats purity.
#   Errors should never pass silently.
#   Unless explicitly silenced.
#   In the face of ambiguity, refuse the temptation to guess.
#   There should be one-- and preferably only one --obvious way to do it.
#   Although that way may not be obvious at first unless you're Dutch.
#   Now is better than never.
#   Although never is often better than *right* now.
#   If the implementation is hard to explain, it's a bad idea.
#   If the implementation is easy to explain, it may be a good idea.
#   Namespaces are one honking great idea -- let's do more of those! 