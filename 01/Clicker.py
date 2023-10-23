from random import *
from tkinter import *

clicks = 0


def randomize():
    global clicks
    btn_click.place(x=randint(70, 1000), y=randint(70, 650))
    clicks += 1
    label_click['text'] = str(clicks)
    label_click.pack()


root = Tk()
root.title('Кликер')
root.geometry('1280x720')
root.resizable(width=False, height=False)
root['bg'] = 'black'

label_click = Label(root, text=0, font=('Comic Sans MS', 30, 'bold'), bg='black', fg='white')
label_click.pack()

btn_click = Button(root,
                   text='Click',
                   bg='lime',
                   fg='black',
                   padx='20',
                   pady='8',
                   font=('Comic Sans MS', 13, 'bold'),
                   command=randomize
                   )
btn_click.place(x=randint(70, 1000), y=randint(70, 650))

root.mainloop()
