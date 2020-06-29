#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, io, os, platform, sys

system = platform.system()
dict_sys = {'Darwin':None, 'Linux':None}

parser = argparse.ArgumentParser()
# parser.add_argument('account', help='the account of GITHUB')
parser.add_argument('repository', help='name of the repository')
args = parser.parse_args()

exc0 = '  '
exc2 = '  '
#exc0 = ' echo "# git" >> README.md '
#exc2 = ' git add README.md '

exc1 = ' git init '
exc3 = f' git remote add origin git@github.com:xrun0213/{0}.git '.format(args.repository)

excs = [exc0, exc1, exc2, exc3]

for exc in excs:
    os.system(exc)


#msg = "&".join( ( exc0, exc1, exc2, exc3, exc4) )
#os.system(msg)

