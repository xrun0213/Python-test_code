#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, io, os, platform, sys, time

OS = platform.system()
t = time.localtime()

parser = argparse.ArgumentParser()
parser.add_argument('branch', help='the branch in Github')
args = parser.parse_args()

dict_exc = {'Windows':'git pull origin {0}'.format(args.branch),
			'Linux':'git pull origin {0}'.format(args.branch),
			'Darwin':'git pull'}

exc = dict_exc[OS]

print("Operation System: ", OS)
try:
	os.system(exc)
except Exception as exc:
	print("Error: ", exc)
	sys.exit(2)
else:
	sys.exit(0)

