#!/usr/bin/python
fname =  'ch3_raw.txt'
file_out = open("ch3_clean.txt","wb")
fh = open(fname,"r")
s = ''
for line in fh:
 s += line.strip('\n')
#ps = s[500:]
#ps = s
ps = s.replace(" ","")
print " length:", len(ps)
file_out.write(ps)
