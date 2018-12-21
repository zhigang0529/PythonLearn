#!/usr/bin/python
# _*_ coding = UTF-8 _*_


try:
    f = open("File.py")
    # line = f.read(2)
    # num = int(line)
except IOError, e:
    print("error: ", e)
except ValueError, ve:
    print("value error: ", ve)
else:
    print "open file ", f.name
finally:
    print "over"
    f.close()
