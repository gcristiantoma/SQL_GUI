from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

cursor=sqlite3.connect("my_db.db")
root=Tk()
root.title("My Application")
root.geometry("1024x800")
# root.configure(background="cornflowerblue")
root.state("zoomed")


label_welcome = Label(root, text="Welcome to my App")
label_start = Label(root, text="Start")

label_welcome.grid(row=0,column=0,ipadx=10,ipady=10)
label_start.grid(row=0,column=0)








root.mainloop()
