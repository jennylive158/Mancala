from tkinter import *


def doNothing():
    return


win = Tk()

win.title("Mancala Game")

# main menu
menu = Menu(win)
win.config(menu=menu)

# toolbar
toolbar = Frame(win, bg="blue")

rulesButt = Button(toolbar, text="Game Rules", command=doNothing)
rulesButt.pack(side=LEFT, padx=2, pady=2)
newGameButt = Button(toolbar, text="New Game", command=doNothing)
newGameButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# status bar
status = Label(win, text="doing something...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

win.mainloop()