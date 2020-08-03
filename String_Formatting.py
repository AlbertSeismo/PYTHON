#A string is a word enclosed in quotes, it forms part of the python data, lets have an example
str1 ="My name is"
str2 ="Albert"
#displaying the variables str1 and str2, if you want to see what it does uncomment and see (remove harsh tag)
#print("\n",str1,"\n\n",str2,"\n\n",str1+" "+str2)
print("{} {}".format(str1,str2))   #string formating method 1
print(f"{str1} {str2}")   #This is the second way of formating strings f-string

def info():
    #if the input data/info is not float or integer we use str-for string, when it is a word
    First_Name = str(input("\n\nPlease what is your First name="))
    Last_Name = str(input("Please what is your Last name="))
    Country = str(input("What is country of Nationality ="))
    YearOfBirth = int(input("When were you born ="))
    Year_Now = int(input("Which year is it now="))
    Age_Now = Year_Now -YearOfBirth
    print(f"\n\nMy First name is {First_Name} and Last name is {Last_Name}. \nI am from {Country}.\nI was born in {YearOfBirth}.\
\nThe year now is {Year_Now}.\nThis means I am {Age_Now} years Now")
    #Another how you would format the string is below using the .format method
    """print("\n\nMy First name is {} and Last name is {}. \nI am from {}.\nI was born in {}.\
    \nThe year now is {}.\nThis means I am {} years Now".format(First_Name,Last_Name,Country,YearOfBirth,Year_Now,Age_Now))"""
info()


