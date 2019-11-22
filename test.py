#! /usr/bin/env python3
#-*- coding: utf-8 -*-
import appscript, argparse, io, os, pytube, random, subprocess, sys, time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from selenium import webdriver

import roslibpy

client = roslibpy.Ros('10.1.1.5', 9090)


def handler(request, response):
    print('Setting speed to {}'.format(request['data']))
    response['success'] = True
    return True



service = roslibpy.Service(client, '/set_ludicrous_speed', 'std_srvs/SetBool')
service.advertise(handler)
print('Service advertised.')

client.run_forever()
print(1)
client.terminate()
print(2)


