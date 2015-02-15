#! /usr/bin/env python3

import urllib.request,urllib,json,base64,io,datetime
from datetime import *
from urllib import *
import tkinter as tk

def runAll():
    # List of country exchange rates
    countries = [
    "AUD","CAD","CHF","DKK","EUR",
    "GBP","HKD","JPY","MXN","NZD",
    "PHP","SEK","SGD","THB","USD","ZAR"
    ]

    # Numbers for the calculator
    calculatorNumbers = [
    "1","2","3",
    "4","5","6",
    "7","8","9",
    "0",".","C"
    ]

    # Building of the GUI
    gui = tk.Tk()
    gui.title("Currenct Exchange")

    # TextBoxes and Labels (Must keep in the proper scope)
    entry = tk.Entry(gui,width=25,bg='purple')
    final = tk.Entry(gui,width=25,bg='red')

    infoVar = tk.StringVar()
    infoVar.set("no status yet")
    infoLabel = tk.Label(gui,textvariable=infoVar,bg='pink')
    infoLabel.grid(row=13,column=0,columnspan=3)

    dateVar = tk.StringVar()
    dateVar.set("no update yet")
    dateLabel = tk.Label(gui,textvariable=dateVar,bg='pink')
    dateLabel.grid(row=14,column=0,columnspan=3)

    # Print the flags using internet connection
    def printFlag(countryIndex,location):
        flagurl = ""
        flags = ["australia","canada","switzerland","denmark","eu",
                "england","hongkong","japan","mexico","newzealand",
                "philippines","sweden","singapore","thailand","us","southafrica"]
        if countryIndex != 4 and countryIndex != 14:
            flagurl = "http://www.crwflags.com/art/countries/%s.gif" % flags[countryIndex]
        else:
            if countryIndex == 4:
                flagurl = "http://www.crwflags.com/art/miscflags/eu.gif"
            else:
                flagurl = "http://newstreaming.com/files/2010/11/US-flag.gif"
        u = urllib.request.urlopen(flagurl)
        raw_data = u.read()
        u.close()
        b64_data = base64.encodestring(raw_data)
        image = tk.PhotoImage(data=b64_data)
        image = image.subsample(2,2)
        flag = tk.Label(image=image,bg='blue',height=120,width=260)
        flag.image = image
        if location == 0:
            flag.grid(row=2,column=0,columnspan=3)
        elif location == 1: 
            flag.grid(row=3,column=0,columnspan=3)

    currencies = open("currencies.txt","r")
    text = currencies.readlines()
    text2 = []
    fullList = []
    for i in text:
        x = i.split("\t")
        exch = x[1]
        x[1] = exch[0:3]
        text2 = text2 + x[0:1]
        fullList += x

    # Get the exchange rate for the given country
    def getExch(country):
        i = fullList.index(country) + 1
        return fullList[i]
    
    # First option menu
    variable = tk.StringVar(gui)
    variable.set(text2[4])
    menu = tk.OptionMenu(gui,variable,*text2)
    printFlag(countries.index(getExch(variable.get())),0)
    # Second option menu
    variable2 = tk.StringVar(gui)
    variable2.set(text2[8])
    menu2 = tk.OptionMenu(gui,variable2,*text2)
    printFlag(countries.index(getExch(variable2.get())),1)

    # For the addition of numbers to the calculator entry
    def key_pressed(key):
        if ("." in entry.get() and key == "."):
            pass
        elif (key == "C"):
            entry.delete(0,tk.END)
        else:
            entry.insert(tk.END, key)

    # Packs into the gui all of the variables
    def addToGUI():
        entry.grid(column=0,row=0,columnspan=3)
        entry.focus_set()
        menu.grid(column=0,row=1,columnspan=2,sticky='w')
        menu2.grid(column=1,row=1,columnspan=2,sticky='e')
        # Add in the two row-takers with country names and flags
        r = 4
        c = 0
        y = 0
        for i in calculatorNumbers:
            cmd = lambda x=i: key_pressed(x)
            if (y % 2) == 0:
                tk.Button(gui,text=i,width=7,height=1,relief='ridge',command=cmd,bg='purple').grid(row=r,column=c)
            else:
                tk.Button(gui,text=i,width=7,height=1,relief='ridge',command=cmd,bg='pink').grid(row=r,column=c)
            y += 1
            c += 1
            if c > 2:
                c = 0
                r += 1
    addToGUI()

    # Take text from textboxes and pass to converter
    def calculate():
        final.delete(0,len(final.get()))
        final.insert(0,"$")
        printFlag(countries.index(getExch(variable.get())),0)
        printFlag(countries.index(getExch(variable2.get())),1)
        if entry.get() == "":
            final.delete(0,tk.END)
            final.insert(0,"Please enter a number")
        else:
            final.insert(len(final.get()),converter(entry.get(),getExch(variable.get()),getExch(variable2.get())))
        infoVar.set("Exchange for %s and %s at $%s" % (variable.get(),variable2.get(),entry.get()))
        # Last updated variable
        currentDate = datetime.now()
        currentDay = str(currentDate.month) + "/" + str(currentDate.day) + "/" + str(currentDate.year)
        dateVar.set("Last updated " + str(currentDate.hour) + ":" +str(currentDate.minute) +":" + str(currentDate.second) + " on " + currentDay)

    # Does the conversion calculation
    def converter(amount, country1, country2):
        urlString = "http://rate-exchange.appspot.com/currency?from=%s&to=%s" % (country1,country2)
        url = urllib.request.Request(url=urlString)
        f = urllib.request.urlopen(url)
        result = f.read().decode("utf-8")
        result = json.loads(result)
        if "rate" in result:
            value = result["rate"]
            value = value * float(amount)
            value = round(value,2)
            return (value)
        else:
            final.delete(0,len(final.get()))
            final.insert(0,"Error!! Please enter a proper Country Code")

    # Adding the final buttons
    b = tk.Button(gui,text="calculate!!",width=18,relief='ridge',command=calculate,bg='purple')
    
    # More packing
    b.grid(row=12,column=0,columnspan=3)
    final.grid(row=15,column=0,columnspan=3)

    # Run the tkinter main loop
    gui.mainloop()

runAll()


