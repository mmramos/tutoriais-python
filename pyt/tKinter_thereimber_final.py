from Tkinter import *
a = Tk()

a.geometry('450x600+300+100')
a.title('Canvas_tuto_15_final')


#Canvas

canvas_1 = Canvas(a,height=300,width=300,bg='red')
canvas_1.create_line(0,0,200,300)
canvas_1.create_oval(0,0,300,300,fill='blue')

canvas_1.pack()

a.mainloop()
