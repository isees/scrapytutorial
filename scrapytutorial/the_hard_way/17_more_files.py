from os.path import exists

from_file = "D:/workspace/python/scrapytutorial/text/from_file.txt"
to_file = "D:/workspace/python/scrapytutorial/text/to_file.txt"

print "Copying from %s to %s" % (from_file, to_file)

read_data = open(from_file).read()
print "Does the output file exist? %r" % exists(to_file)

write_object = open(to_file, "w")
write_object.write(read_data)

print "Allright, it's all done."
write_object.close()
