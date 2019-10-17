#! /usr/bin/env python3
#-*- coding: utf-8 -*-
import appscript, argparse, io, os, pytube, subprocess, sys, time
import tkinter as tk
from tkinter import ttk
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.google.com.tw/"
driver.get(url)

tags = driver.find_elements_by_tag_name("input")
print('len: ', len(tags) )
print( 'type of tags[0]: ', type(tags[0]) )
print( 'name of tags[0]: ', tags[0].tag_name )

search_field = driver.find_element_by_name('q')

search_field.send_keys("玫瑰星雲")
search_field.submit()

# driver.quit()