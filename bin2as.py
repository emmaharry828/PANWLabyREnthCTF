#!/usr/bin/python
import sys
file_in = open("ch3_clean.txt")
file_out = open("ch3_final.txt","wb")
bl = 8

bitlist = map(int,''.join(file_in.read().split()))
if len(bitlist)%bl != 0:
    sys.exit("length of bitlist not integer multiple of %s" % bl)

# assemble resultstring:
# - make list of bytes from `bitlist`
# - evaluate each byte -> int -> ascii char
rs = ''.join([chr(sum(bit<<abs(idx-bl)-1 for idx,bit in enumerate(y)))
               for y in zip(*[bitlist[x::bl] for x in range(bl)])
              ])
 
# write output
file_out.write(rs)
file_out.close()


