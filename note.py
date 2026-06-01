from tkinter import *

root = Tk()

root.geometry("800x600")
root.title("Notepad")

widget = Label(root, text="Hello", font=("Arial", 24))

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text_box = Text(root, yscrollcommand=scroll.set)
text_box.pack(fill=BOTH, expand=True)

scroll.config(command=text_box.yview)

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")

file_menu.add_separator()

file_menu.add_command(label="Exit")

menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=0)

help_menu.add_command(label="About")

menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()