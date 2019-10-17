#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, io, os, sys, time

time_str = time.strftime( '%m/%d', time.localtime() )

parser = argparse.ArgumentParser()
parser.add_argument('branch', help='the branch the file is updated')
parser.add_argument('message', help='message of updated file')
args = parser.parse_args()

scr = []
scr.append(' git add -A ')
scr.append(f' git commit -m "{args.message} {time_str}" ')
scr.append(f' git push -u origin HEAD:{args.branch} ')

for i in scr:
    os.system(i)

sys.exit(2)
