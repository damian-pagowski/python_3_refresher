import sys
  
# reading command line arguments
#  first is filename
# ternar operator syntax much dirrefent from java  and JS
name = "Stranger" if len(sys.argv) < 2 else sys.argv[1] 
print("hello {}".format(name))

