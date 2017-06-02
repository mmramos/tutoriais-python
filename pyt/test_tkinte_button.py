import sys
import numpy as np
from Tkinter import *
x = 1
y = 2
def z():
    l0 = Label(x+y).pack
    print(l0)

# a = base
a = Tk()
a.geometry('450x450+500+300')
a.title('meu tkinter')


# l = label
l2 = Label(a,text='y = 2').pack()

# b = button
b = Button(a,text = 'Ok',command = z).pack()

a.mainloop()
