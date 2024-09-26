from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Тестовое окно')
root.geometry('800x800')
root.resizable(True, True)
root['bg'] = 'pink'


def click():
    print('Привет')


btn = Button(root,
             text='Привет!',
             command=click,
             relief=RAISED,
             fg='black',
             bg='pink',
             width=10,
             height=2,
             activebackground='Deep pink',
             activeforeground='white',
             )
btn.pack(side=BOTTOM)
btn.place(x=350, y=700)

label = Label(root)
label.pack()

img = PhotoImage(file='pic/logo.png')
l_logo = Label(root, image=img)
l_logo.place(x=400, y=800)
l_logo.pack()


root.mainloop()
