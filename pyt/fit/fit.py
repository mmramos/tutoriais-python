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
        put = t.get()
        l2 = Label(a,text=put).pack()
        
        return
        
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


#M = [[np.sum(x**(i+j))for i in range (put)]for j in range (put)]
#N = [np.sum(y*(x**(i)))for i in range (put)]

#MI = np.linalg.inv(M)
#p = (np.dot(MI,N)

#X = [(x**i)for i in range (put)]
#XP=np.array([X[i]*p[i]for i in range (put)])
#Y = XP.sum(axis=0)
