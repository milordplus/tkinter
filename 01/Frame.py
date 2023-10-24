from tkinter import *

root = Tk()
root.title('')
root.geometry('500x500')
root.resizable(False, False)

# root['bg'] = 'black'

frame_top = LabelFrame(root, text='Верх')
frame_top.pack(side=RIGHT)

label_1 = Label(frame_top, width=7, height=4, bg='brown', text='1')
label_1.pack(side=LEFT)
label_2 = Label(frame_top, width=7, height=4, bg='blue', text='2')
label_2.pack(side=LEFT)

frame_bottom = LabelFrame(root, text='Низ')
frame_bottom.pack(side=LEFT)

label_3 = Label(frame_bottom, width=7, height=4, bg='yellow', text='3')
label_3.pack(side=LEFT)
label_4 = Label(frame_bottom, width=7, height=4, bg='green', text='4')
label_4.pack(side=LEFT)

root.mainloop()
