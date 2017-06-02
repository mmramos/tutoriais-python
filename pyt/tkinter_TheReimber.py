import sys
from Tkinter import *
def hello():
    l1 = Label(a,text='hello world').pack()

    
# a = base
a = Tk()
a.geometry('450x450+500+300')
a.title('meu tkinter')


# l = label
l = Label(a,text='my label').pack()

# b = button
b = Button(a,text = 'Ok',command = hello,fg = 'red', bg='blue').pack()
a.mainloop()

# e = entry
e = Entry().pack()



