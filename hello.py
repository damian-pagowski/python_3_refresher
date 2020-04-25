import sys
  
# reading command line arguments
#  first is filename
# ternar operator syntax much dirrefent from java  and JS
name = "Stranger" if len(sys.argv) < 2 else sys.argv[1] 
# first argument is always script name
print("hello {}".format(name))

#  comments
#  "pound character"

# math operators
# same as js, but division is a bit different // vs /
# //drops fractional part after decimal
print(7//2)
print(7.0//2.0)
print(7.0//2)
print(7/2)
print(7.0/2)
print(7/4)
print(7.0/4)


# string templates with %
print("this is string %s" % "strng")
print("I want my caffe with %s and %s" % ('sugar', 'milk'))
print("this is number %d" % 3.14) # will drop fractional part
print("pi =  %1.2f" % 3.14)  # python 2 style
print(" pi = {:.2f}".format( 3.14 )) # new


# get user input - prompt
# answer = input("whats your favourite color?")
# print(answer)

# functions

# *args varargs
def print_two(*args):
    one, two = args
    print("first %s and second %s" % (one, two))

print_two("a", "b")

# default arguments in function
#  function doc string
def greetings(first="hello", second="Damian"):
    '''prints greeting
    doc string 
    can have
    multiple 
    lines''' 
    print("%s %s" % (first, second))

greetings("hi", "Joe")
greetings()


# logic operators
# and
# or
# not
# != (not equal)
# == (equal)
# >= (greater- than- equal)
# <= (less- than- equal)
# True
# False


# conditionals

apples = 5
cherries = 10

#  if--elif-else
if apples < cherries:
    print('cherry wins')
elif apples == cherries:
    print('draft')
else:
    print('apple wins')

# loops
colors = ['blue', 'red', 'green']
# iterate over colection
for i in colors:
    print("color: %s" % i)

# iterate over colection using index 
for i in range(len(colors)):
    print("color with index %d is %s" % (i, colors[i]))

# while loop
j=0
while j < len(colors):
    print("in while loop. current color: %s" % colors[j])
    j+=1

# data structures

# data types
