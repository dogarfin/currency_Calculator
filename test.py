#! /usr/bin/env python3

import tkinter as tk
import urllib.request
from urllib import *
import base64

root = tk.Tk()
URL = "http://www.laboiteverte.fr/wp-content/uploads/2010/10/gif-psychedelique-hypnose-animation-01.gif"
u = urllib.request.urlopen(URL)
raw_data = u.read()
u.close()

b64_data = base64.encodestring(raw_data)
image = tk.PhotoImage(data=b64_data)
label = tk.Label(image=image,bg='white')
label.grid(row=3,column=2)
button = tk.Label(root,text="calculate")
button.grid(column=0,row=0)

root.mainloop()




