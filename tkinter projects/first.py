from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")
labell = Label(window, text = "Weclcome To tkinter",fg="blue",relief = "solid", bg ="yellow", font=("arial", 16, "bold"))
labell.pack(fill=BOTH, padx=2, pady =2)
button = Button(window, text= "Demo", fg = "white", bg="red", relief="raised")
button.place(x=110, y =110)
window.mainloop()
#git
#len
