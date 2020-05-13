#!/usr/local/bin/python3.8
import pyttsx3
import os
import bs4
import requests
from termcolor import colored
import sys
import time
while True:
	a = requests.get("https://www.worldometers.info/coronavirus/")
	b = requests.get("https://www.worldometers.info/coronavirus/country/iran/")
	c = bs4.BeautifulSoup(a.text,"html.parser")
	d = bs4.BeautifulSoup(b.text,"html.parser")
	e = c.find_all('div',attrs={'class':'maincounter-number'})
	f = d.find_all('div',attrs={'class':'maincounter-number'})
	print(colored(""" the world is green

 the iran is red:


cases
deaths
recovered

""",'blue'))
	for i in e:
            print(colored(i.text+"😥"+"\n","green"))
            s = pyttsx3.init()
            s.setProperty('rate',110)
            s.say(i.text)
            s.runAndWait()
	for j in f:
            print(colored(j.text+"🤒"+"\n","red"))
            b = pyttsx3.init()
            b.setProperty('rate',100)
            b.say(j.text)
            b.runAndWait()
	time.sleep(300)
