from tkinter import *
from random import *

root = Tk()

root.title('Камень ножницы бумага')
root.geometry('600x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'


def why_knb():
    knb = ['Камень', 'Ножницы', 'Бумага']
    value = choice(knb)
    labelText.configure(text=value)


labelText = Label(root, text='', fg='white', font=('Comic Sans MS', 20), bg='black')
labelText.place(y=200, x=260)

stone = Button(root,
               text='Камень',
               font=('Comic Sans MS', 20),
               bg='white',
               command=why_knb
               )

scissors = Button(root,
                  text='Ножницы',
                  font=('Comic Sans MS', 20),
                  bg='white',
                  command=why_knb
                  )

paper = Button(root,
               text='Бумага',
               font=('Comic Sans MS', 20),
               bg='white',
               command=why_knb
               )

stone.place(x=50, y=300)
scissors.place(x=240, y=300)
paper.place(x=440, y=300)

root.mainloop()
