#WE BIG WITH FOR LOOPS

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line
print("\n")
for planeti in planets:
    print(planeti) # print all on different lines

for i, planeti in enumerate(planets):
    print("\n",i,".",planeti) # print all on different lines

"""The for loop specifies the variable name to use (in this case, planet)
the set of values to loop over (in this case, planets) You use the word "in" to link them together.
The object to the right of the "in" can be any object that supports iteration. Basically, 
if it can be thought of as a group of things, you can probably loop over it. 
In addition to lists, we can iterate over the elements of a tuple:"""

multi = (2, 2, 2, 3, 3, 5)
product = 2
for i in multi:
    product = product * i
product

List =[1,2,5,6,7]
ans=0
print("\ni","Ans")
for i in List:
    ans =ans+i
    print(i, ans)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

for j in range(10):
    print("\nDoing important work for Python. j =", j)


#WHILE LOOP
"""The other type of loop in Python is a while loop, which iterates until some condition is met:"""
i =0
while i<30:
    j = i+1
    #print(i,j)
    print("when i=",i, "j=",j)
    i +=1

#Another example that is only met when the under limit is reached
"""i =-1
while i<20:
    j = i+1
    #print(i,j)
    print("when i=",i, "j=",j)
    i -=10"""

#LIST COMPREHENSION
"""List comprehensions are one of Python's most beloved and unique features. 
The easiest way to understand them is probably to just look at a few examples:"""

squares = [n**2 for n in range(10)]
print("\n",squares)

#This is the way we would do it with loops
Squares = []
for n in range(10):
    Squares.append(n**2)
print(Squares)


short_planets = [planet for planet in planets if len(planet) < 6]
print("\n\n",short_planets)

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print("\n\n",loud_short_planets)

