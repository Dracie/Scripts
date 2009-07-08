#!/usr/bin/python
#Authored by Exteris and Dracie
#The GNU General Public License is a Free Software license. Like any Free Software license, it grants to you the four following freedoms:
#   1. The freedom to run the program for any purpose.
#   2. The freedom to study how the program works and adapt it to your needs.
#   3. The freedom to redistribute copies so you can help your neighbor.
#   4. The freedom to improve the program and release your improvements to the public, so that the whole community benefits.

import sys
import base64

def usage():
	print('Base64 Encoder/Decoder\n\
	Usage: [e] [STRING TO ENCODE]\n\
	       [d] [STRING TO DECODE]')
	sys.exit()

if len(sys.argv) <= 1:
	usage()

if sys.argv[1] == 'e':
	print base64.b64encode(sys.argv[2])
elif sys.argv[1] == 'd':
	print base64.b64decode(sys.argv[2])
else:
	usage()