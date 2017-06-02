import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *
import sys
import tkMessageBox
import tkColorChooser
import tkFileDialog



#----------------------------------#


def mOpen():
    def num():
        g = t.get()
        l2 = Label(a,text=g).pack()
    
    op = tkFileDialog.askopenfile()
    data=np.genfromtxt(op,delimiter='	')
    x0=data[:,0]
    y0=data[:,1]
    x=np.array(x0)
    y=np.array(y0)
    m0=len(x)
    t=StringVar()
    spx=Spinbox(a,from_=0,to=m0,command=num,textvariable=t).pack()

    return

#----------------------------------#

a = Tk()
a.title('Fit')
a.geometry('450x450+600+100')


menubar=Menu(a)


file=Menu(menubar,tearoff=0)
file.add_command(label='Open',command = mOpen)

help=Menu(menubar,tearoff=0)
help.add_command(label='About')

menubar.add_cascade(label='File',menu=file)
menubar.add_cascade(label='Help',menu=help)
a.config(menu=menubar)


a.mainloop()
