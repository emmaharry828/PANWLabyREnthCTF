#!/usr/bin/python
import sys
import binascii
file_in = open("key_str.txt","rb")
file_out = open("final_key.txt","wb")
rs = ''
last = 0
for s in file_in:
  str = s.strip('\n')
  hex_string = str.decode("hex")
  a = bytearray(hex_string)
  for i in a:
    tmp =((last&0xff^i)+0x66&0xff ^ 0x55) - 0x44^0x33
    rs += hex(tmp)
    last += i
 
# write output
file_out.write(rs)
file_out.close()
file_in.close()
