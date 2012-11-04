#!/usr/bin/env python

# after downloading through sab, 
# convert epub files to mobi files
# and send to kindle
import sys
import os

if len(sys.argv) >= 2:
	book_dir = sys.argv[1]
	for files in os.listdir(book_dir):
		# convert epub files to mobi
		full_path = os.path.abspath(book_dir + "/" + files)
		if files.endswith(".epub"):
			cmd = "kindlegen \"" + full_path + "\" -o \"" + files + ".mobi\""			
			os.system(cmd)
			# change the full_path variable to the new file's full path
			# so we can send the new file to amazon
			full_path = full_path + ".mobi"
		if os.path.isfile("sendKindle.py"):
			if full_path.endswith(".mobi"):
				os.system("sendKindle.py \"" + full_path + "\"")
else:
	print("something is busted")
	sys.exit()