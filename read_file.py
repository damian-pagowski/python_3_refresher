from sys import argv
if len(argv) < 2:
    print("please specify file to open")
    exit(0)
script, filename = argv
txt = open(filename)
print("Here's your file %r:" % filename)
print(txt.read())