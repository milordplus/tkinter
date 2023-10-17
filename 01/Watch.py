from tkinter import *
import time

root = Tk()
root.title("Часы")
root.resizable(width=False, height=False)


def tick():
    watch.after(1000, tick)
    watch['text'] = time.strftime("%H:%M:%S")


watch = Label(root, font="Arial 100")
watch.pack()
tick()

root.mainloop()
