from tkinter import *

root = Tk()

root.geometry("800x600")
root.title("Notepad")

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text_box = Text(root, yscrollcommand=scroll.set)
text_box.pack(side=LEFT, fill=BOTH, expand=True)

scroll.config(command=text_box.yview)

root.mainloop()