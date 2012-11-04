#!/usr/bin/env python

# after downloading through sab, 
# convert epub files to mobi files
# and send to kindle
import sys
import os

if len(sys.argv) >= 2:
	book = sys.argv[1]
	if ".epub" in book:
		cmd = "kindlegen " + book + " -o " + book + ".mobi"
		os.system(cmd)
		if os.path.isfile("sendKindle.py"):
			os.system("python sendKindle.py " + book + ".mobi")
	else:
		sys.exit()
else:
	sys.exit()