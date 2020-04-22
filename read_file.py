from sys import argv
if len(argv) < 2:
    print("please specify file to open")
    exit(0)
script, filename = argv
# 'r' : use for reading
# 'w' : use for writing
# 'x' : use for creating and writing to a new file
# 'a' : use for appending to a file
# 'r+' : use for reading and writing to the same file
f = open(filename, 'r')

# close  - close file 
# read - read file and assign content to a variable
# readline - read single line
# truncate - empties file
# write(text) - writes text into a file
print("Here's your file %r:" % filename)
# print(f.read())

print("now with readlines")
for line in f.readlines() :
    print(line)

f.close()