from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %r to %r" % (from_file, to_file)

#figure out how to do this in one line:
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % indata

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()
