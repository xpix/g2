"""

Notes: Doing a text select from the forum resulted in unusable text. Procedure was:
  - capture text to a word document
  - save as plain text, Mac format, CR and LF (the defaults)
  - then run this file on it

"""

f = open("./testfile.gcode","r")
w = open("./testfile-NUMBERED.gcode","a+w")

count = 1
for line in f.readlines():
#  print("N%s %s" % (count, line))
  w.write("N%s %s" % (count, line))
  count = count + 1
w.close()
