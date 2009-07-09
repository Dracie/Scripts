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
	print('Encoder/Decoder\n\
Usage: [FORMAT] [e] [STRING TO ENCODE]\n\
       [FORMAT] [d] [STRING TO DECODE]\n\
       FORMAT KEYWORDS: b32 b64')
	sys.exit()

if len(sys.argv) <= 1:
	usage()

def b64():
	if sys.argv[2] == 'e':
		print base64.b64encode(sys.argv[3])
	elif sys.argv[2] == 'd':
		print base64.b64decode(sys.argv[3])
	else:
			usage()

def b32():
	if sys.argv[2] == 'e':
		print base64.b32encode(sys.argv[3])
	elif sys.argv[2] == 'd':
		print base64.b32decode(sys.argv[3])
	else:
			usage()

if sys.argv[1] == 'b64':
	b64()
elif sys.argv[1] == 'b32':
	b32()
else:
	usage()
