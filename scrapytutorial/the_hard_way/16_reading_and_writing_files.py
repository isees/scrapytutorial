filename = "D:/workspace/python/scrapytutorial/text/read_write.txt"

print "We're going to erase %r." % filename
print "If you don't want this, hit CTRL-C(^C)."
print "If you do want this, hit Enter."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you three questions"

line1 = raw_input("First, what's you name? ")
line2 = raw_input("Second, who do love? ")
line3 = raw_input("Last one, do you like yourself? ")

print "I'm going to record these to file: %r" % filename

target.write(line1+"\n")
target.write(line2+"\n")
target.write(line3+"\n")
target.close()

read_target = open(filename)
print read_target.read()
read_target.close()






