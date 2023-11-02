from tkinter import *

from googletrans import Translator


def translate():
    text1 = t1.get('1.0', END)
    text2 = translator.translate(text1, dest='ru')
    t2.delete('1.0', END)
    t2.insert('1.0', text2.text)


root = Tk()
root.geometry('500x350')
root.title('Переводчик')
root.resizable(False, False)
root['bg'] = 'black'
translator = Translator()

label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст на английском')
label.place(relx=0.5, y=30, anchor=CENTER)
t1 = Text(root, width=35, height=5, font='Arial 12 bold')
t1.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Перевести', command=translate)
btn.place(relx=0.5, y=180, anchor=CENTER)

t2 = Text(root, width=35, height=5, font='Arial 12 bold')
t2.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()
