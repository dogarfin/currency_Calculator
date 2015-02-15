#! /usr/bin/env python3

import tkinter as tk
import urllib.request
from urllib import *
import base64

root = tk.Tk()
URL = "http://www.crwflags.com/art/miscflags/eu.gif"
u = urllib.request.urlopen(URL)
raw_data = u.read()
u.close()

b64_data = base64.encodestring(raw_data)
image = tk.PhotoImage(data=b64_data)
label = tk.Label(image=image)
label.pack()

root.mainloop()




