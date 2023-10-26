from tkinter import *

root = Tk()

root.title('Блокнот')
root.geometry('600x700')
root.iconbitmap('notepad.png')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_field = Text(f_text,
                  bg='black',
                  fg='lime',
                  padx=10,
                  pady=10,
                  wrap=WORD,
                  insertbackground='white',
                  selectbackground='#8D917A',
                  spacing3='10',
                  width=30
                  )
text_field.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

root.mainloop()
