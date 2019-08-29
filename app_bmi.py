# -*- coding: utf-8 -*-

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import tkinter as tk


app = tk.Tk()
app.title("BMI實作app")
app.geometry('300x200')

intheight = tk.IntVar()
intweight = tk.IntVar()

t = False
def result():
    global t
    t = True
    height = intheight.get()
    weight = intweight.get()
    bmi = weight/(height/100)**2
    if bmi < 18.5:
        level = '過輕'
    elif bmi < 24:
        level = '健康'
    elif bmi < 27:
        level = '過重'
    elif bmi < 30:
        level = '輕肥'
    elif bmi < 35:
        level = '中肥'
    else:
        level = '癡肥'

    tk.Label(app, text = '%s  %f' %(level, bmi)).grid(column=1, row=3, sticky=tk.W)



tk.Label(app, text = '身高').grid(column=0, row=0, sticky=tk.W)
tk.Entry(app, width = 20, textvariable = intheight).grid(column=1, row=0, sticky=tk.W)
tk.Label(app, text = '體重').grid(column=0, row=1, sticky=tk.W)
tk.Entry(app, width = 20, textvariable = intweight).grid(column=1, row=1, sticky=tk.W)
tk.Button(app, text='確認', width = 5, command = result).grid(column=0, row=2, sticky=tk.W)
tk.Label(app, text = 'BMI').grid(column=0, row=3, sticky=tk.W)
tk.Label(app, text = 'bmi值').grid(column=1, row=3, sticky=tk.W)

tk.mainloop()
