import _thread
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import requests
import json
import ast as ast
import os, fnmatch


root = Tk()
root.title("Tk dropdown example")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 5)
mainframe.rowconfigure(0, weight = 5)
mainframe.pack(pady = 100, padx = 100)


# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary request METHOD with options
choices = { 'POST','GET','PUT','DELETE','UPDATE'}
tkvar.set('methods') # set the default option

#Implement method options
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="METHOD", width=30).grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

#Schema Label and Textbox

Label(mainframe, text=" SCHEME :// HOST [ \":\" PORT ] [ PATH [ \"?\" QUERY ]] ").grid(row = 1, column = 2)
textbox = Text(mainframe, height=1, font=('Arial',16))
textbox.grid(row=2, column=2)

# Submit Request Label
MyButton1 = Button(mainframe, text="Submit", width=10, command="You clicked the")
MyButton1.grid(row=2, column=3)

# request headers
Label(mainframe, text="Request Headers").grid(row = 3, column = 1)
requestHeadersBox = Text(mainframe, height=3, font=('Arial',16))
requestHeadersBox.grid(row=4, column=1)

# request  body
Label(mainframe, text="Request Body").grid(row = 3, column = 2)
requestBodyBox = Text(mainframe, height=3, font=('Arial',16))
requestBodyBox.grid(row=4, column=2)

# Response Message
Label(mainframe, text="Request Body").grid(row = 5, column = 1)


# response headers
Label(mainframe, text="Response Headers").grid(row = 6, column = 1)
responseHeadersBox = Text(mainframe, height=3, font=('Arial',16))
responseHeadersBox.grid(row=7, column=1)

# response Body
Label(mainframe, text="Response Body").grid(row = 6, column = 2)
responseBodyBox = Text(mainframe, height=3, font=('Arial',16))
responseBodyBox.grid(row=7, column=2)


def callback():
    print('You clicked the button!') 

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
