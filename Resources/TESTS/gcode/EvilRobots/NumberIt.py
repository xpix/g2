"""

Notes: Doing a text select from the forum resulted in unusable text. Procedure was:
  - capture text to a word document
  - save as plain text, Mac format, CR and LF (the defaults)
  - then run this file on it

"""

f = open("./UltimakerRobot_support_100.20141124.gcode","r")
w = open("./UltimakerRobot_support_100.20141124-NUMBERED.gcode","a+w")

count = 1
for line in f.readlines():
#  print("N%s %s" % (count, line))
  w.write("N%s %s" % (count, line))
  count = count + 1
w.close()
