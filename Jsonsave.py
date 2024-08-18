# Import the required libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import requests
import json


api_url = "https://catfact.ninja/fact"

response = ""

def get_zen():
   global response 
   response = requests.get(api_url).text
   response_info = json.loads(response)
   Fact = response_info["fact"]
   print(Fact)

get_zen()

def writeFile():
    file = open('sh3rly.txt','a+')
    file.write(metinF.get() + '\n')
    file.close()

gui = Tk()

metinF = Entry(gui)
metinF.grid(row=9, column=1)

butonWrite = Button(gui)
butonWrite.config(text = 'Write To File', command = writeFile)
butonWrite.grid(row=8, column=1)

gui.mainloop()