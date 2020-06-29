#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, io, os, platform, socket, sys, time

OS = platform.system()
hostname = socket.gethostname()
t = time.localtime()


parser = argparse.ArgumentParser()
parser.add_argument('branch', help='the local branch where the file is updated')
parser.add_argument('message', help='updating message')
args = parser.parse_args()

exc1 = 'git add -A'
dict_exc2 = {'Windows':' git commit -m "{0}/{1} {2} from {3}" '.format(t.tm_mon, t.tm_mday, args.message, hostname),
			'Linux':' git commit -m "{0}/{1} {2} from {3}" '.format(t.tm_mon, t.tm_mday, args.message, hostname),
			'Darwin':' git commit -m "{0}/{1} {2} form {3}" '.format(t.tm_mon, t.tm_mday, args.message, hostname)
			}
dict_exc3 = {'Windows':'git push origin {0}:osx'.format(args.branch),
			'Linux':'git push origin {0}:osx'.format(args.branch),
			'Darwin':'git push origin {0}:osx'.format(args.branch)
			}

exc2 = dict_exc2[OS]
exc3 = dict_exc3[OS]

excs = [exc1, exc2, exc3]

print("Operating System: ", OS)
try:
	for exc in excs:
		os.system(exc)
except Exception as exc:
	print("ERROR: ", exc)
	sys.exit(2)
else:
	sys.exit(0)

