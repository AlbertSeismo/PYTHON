#TASK 4
#HERE IS A MORE DETAILED STRING METHODS & PRACTICE
Str = ("Here are some of the most common string methods. A method is like a function, \n"
                 "but it runs \"on\" an object. If the variable s is a string, then the code s.lower() runs \n"
                 "the lower() method on that string object and returns the result (this idea of a method running \n"
                 "on an object is one of the basic ideas that make up Object Oriented Programming, OOP). \n"
                 "Here are some of the most common string methods")
print(Str)

#TRY PRINTING EACH OF THE FOLLOWING BELOW METHODS and understand what each does
#Remember Str is our variable above that conatins the string text
#the .upper,.lower are the methods that perform the necessary changes as below
Str.upper()
Str.lower()
Str.split(' ')
Str.split(".")
Str.strip()
Str.replace('old word', 'new word')   #method to replace words with new words of your choice
#feel free to write new strings of your choice and test these methods
Str.startswith('other')   #other is just an example you can test using other words
Str.endswith('other')
Str.split('delim')  #splits the entire text and returns a list based on the delimeter like delim =(comas,fullstop, space)
#eg Str.split(",") will split the text based on where the comma is
Str.find('method')   #returns the index/position of the first word "method in Str"

#HINT FOR MORE EXPLANATION
"""Str.lower(), Str.upper() -- returns the lowercase or uppercase version of the string
Str.strip() -- returns a string with whitespace removed from the start and end
Str.isalpha()/Str.isdigit()/Str.isspace()... -- tests if all the string chars are in the various character classes
Str.startswith('other'), Str.endswith('other') -- tests if the string starts or ends with the given other string
Str.find('other') -- searches for the given other string (not a regular expression) within str, and returns the first index where it begins or -1 if not found
Str.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
Str.split('delim')"""

#TASK 5
#I would like to see also some work on index,slicing and concatenation, create strings of your choice