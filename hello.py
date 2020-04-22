import sys
  
# reading command line arguments
#  first is filename
# ternar operator syntax much dirrefent from java  and JS
name = "Stranger" if len(sys.argv) < 2 else sys.argv[1] 
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


# data types

# conditionals

# loops

# data structures

