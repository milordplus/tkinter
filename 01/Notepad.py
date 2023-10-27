from tkinter import *

root = Tk()

root.title('Блокнот')
root.geometry('600x700')
root.iconbitmap('notepad.png')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть')
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Темная')
view_menu_sub.add_command(label='Светлая')
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial')
font_menu_sub.add_command(label='Comic Sans MS')
font_menu_sub.add_command(label='Times New Roman')
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)

root.config(menu=main_menu)

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
