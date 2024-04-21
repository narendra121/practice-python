import tkinter

window=tkinter.Tk()

window.title("My Show")
window.maxsize(width=500,height=300)

#Label
mylabel=tkinter.Label(text="Iam label")
mylabel.pack()


window.mainloop()
