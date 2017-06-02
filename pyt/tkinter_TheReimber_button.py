import sys
from Tkinter import *
import tkMessageBox
import tkColorChooser
import tkFileDialog



def p():
    t = m.get()
    l2 = Label(a,text=t).pack()
    return
def mOpen():
    myopen = tkFileDialog.askopenfile()
    return
def mNew():
    l3 = Label(a,text='voce clicou em New').pack()
    return
   
def mAbout():
    tkMessageBox.showinfo(title='About',message='Lune 2014')
    return
def mColour():
    mycolour = tkColorChooser.askcolor()
    l4 = Label(a,text=mycolour).pack()
    return
def mQuit():
    mExit = tkMessageBox.askyesno(title='Exit',message='tem certeza?')
    if mExit >0:
        a.destroy()
        return
    
# a = base
a = Tk()
m = StringVar()
mvar = IntVar()
a.title('meu tkinter')


# l = label
l = Label(a,text='my label').pack()

# b = button
b = Button(a,command = p).pack()

# e = entry
#e = Entry().pack()
e = Entry(a,textvariable=m).pack()

#Construcao Menu

menubar=Menu(a)
file = Menu(menubar)
file.add_command(label='New',command = mNew)
file.add_command(label='Open',command = mOpen)
file.add_command(label='Save As...')
file.add_command(label='Colour',command = mColour)
file.add_command(label='Close',command = mQuit)

menubar.add_cascade(label='File',menu=file)

help = Menu(menubar)
help.add_command(label='About',command = mAbout)

menubar.add_cascade(label='Help',menu=help)

Radio_1=Radiobutton(a,text='Option 1',value = 1).pack()
Radio_2=Radiobutton(a,text='Option 2',value = 2).pack()
Radio_3=Radiobutton(a,text='Option 3',value = 3).pack()
Radio_4=Radiobutton(a,text='Option 4',value = 4).pack()

setup = Menu(menubar,tearoff = 0)
setup.add_checkbutton(label = 'Auto')
menubar.add_cascade(label='Setup',menu=setup)

a.config(menu=menubar)

#Spinbox
spinbox1 = Spinbox(a,from_=0,to=10).pack()

#Listbox
List1 = Listbox(a)
List1.insert(4,'Python')
List1.insert(1,'PHP')
List1.insert(3,'C++')
List1.insert(2,'Java')
List1.insert(5,'Perl')
List1.pack()

#Slider
Slider_1=Scale(a,orient=HORIZONTAL,length=300,width=20,sliderlength=10,from_=0,to=50,tickinterval=10).pack()

#CheckButton
check1 = Checkbutton(a,state = ACTIVE,variable = mvar,command=mQuit).pack()
a.mainloop()
