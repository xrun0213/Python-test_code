#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, io, os, sys

parser = argparse.ArgumentParser()
# parser.add_argument('account', help='the account of GITHUB')
parser.add_argument('repository', help='name of the repository')
args = parser.parse_args()

scr = []
scr.append(' echo "# git" >> README.md ')
scr.append(' git init ')
scr.append(' git add README.md ')
scr.append(f' git remote add origin git@github.com:xrun0213/{args.repository}.git ')
scr.append(' git push -u origin master ')

for i in scr:
    os.system(i)

sys.exit(2)
