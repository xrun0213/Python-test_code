#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, pyttsx3, sys, threading
# import pyttsx as pyttsx3

# msg = 'PUBLISH TOPIC 目標點'
# engine = pyttsx3.init()
# engine.say(msg)
# engine.runAndWait()
# engine.startLoop()
# engine.endLoop()
# engine.stop()
# engine = pyttsx3.speak(msg)



def init_engine():
	engine = pyttsx3.init()
	return engine

def say(s):
	engine.say(s)
	engine.runAndWait() #blocks

engine = init_engine()
say(str(sys.argv[1]))