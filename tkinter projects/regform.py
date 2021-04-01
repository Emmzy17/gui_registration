from tkinter import  *
import sqlite3
from PIL import Image, ImageTk
import tkinter.messagebox
window = Tk()
window.geometry("500x600")

window.title("Registration")

img  = Image.open("python_icon.png")
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo)
lab.pack()

menu=Menu(window)
window.config(menu=menu)

subm=Menu(menu)
menu.add_cascade(label="File", menu=subm)
subm.add_command(label="Exit")


fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
var_c1 = "Python"
var_c2 = "C#"
var_r1 = StringVar()

def printt():
    first = fn.get()
    sec = ln.get()
    dob1 = dob.get()
    var1 = var.get()
    var_2 = var_c1
    var_2 = var_c2
    var_3 = var_r1.get()

    print(f"Your fullname is {first}{sec}")
    print(f"Your Date of birth is {dob1}")
    print(f"Your country is {var1}")
    print(f"Your programming language is {var_2} ")
    print(f"You are a {var_3}")
    tkinter.messagebox.showinfo("Welcome", "{} is successsfully signed up".format(first))
def exitt():
    exit()

def sec_window():
    root = Tk()
    root.geometry("250x200")

def database():
    first_name = fn.get()
    sec_name = ln.get()
    date = dob.get()
    country = var.get()
    programming = var_c2
    gender = var_r1.get()
    conn = sqlite3.connect("form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS student (Name TEXT, Last TEXT, DOB TEXT, Country TEXT,Programming TEXT, Gender TEXT)")
    cursor.execute('INSERT INTO  student(Name, Last, DOB, Country, Programming, Gender) VALUES(?,?,?,?,?,?)', (first_name, sec_name, date,country, programming, gender) )
    conn.commit
menu = Menu(window)
window.config(menu=menu)

subm = Menu(menu)
subm.add_cascade(label="File")
subm.add_command(label = "Exit")

label1 = Label(window, text = "Registration Form", relief = "solid",width = 20, font=("arial", 19, "bold"))
label1.place(x = 90, y=153)

label2 = Label(window, text = "First name:",width = 20, font=( "bold", 10))
label2.place(x = 80, y=230)

entry_1 = Entry(window, textvar = fn)
entry_1.place(x = 250, y = 230)

label3 = Label(window, text = "Last name:", width = 20, font=( "bold", 10))
label3.place(x = 80, y=270)

entry_2 = Entry(window, textvar = ln)
entry_2.place(x = 250, y = 270)

label4 = Label(window, text = "DOB:", width = 20, font=("bold", 10))
label4.place(x = 65, y=310)

entry_3 = Entry(window, textvar = dob)
entry_3.place(x = 250, y = 310)

label5 = Label(window, text = "Country :", width=20, font =("bold", 10))
label5.place(x = 75, y = 340)

list1 = ['Nigeria', 'U.S.A', 'Canada', 'India']
dropList = OptionMenu(window, var, *list1)
var.set("Select Country")
dropList.config(width = 15)
dropList.place(x = 245, y = 340 )

label6 = Label(window, text = "Prog Lang :", width=20, font =("bold", 10))
label6.place(x = 80, y = 380)

c1 = Checkbutton(window, text = "Python", variable=var_c1)
c1.place(x = 250, y = 380)

c2 = Checkbutton(window, text = "C#", variable=var_c2)
c2.place(x = 320, y = 380)

r1 = Radiobutton(window, text = "Male", variable=var_r1, value = "Male").place(x = 250, y =420)
r2 = Radiobutton(window, text = "Female", variable=var_r1, value = "Female").place(x = 320, y =420)

label7 = Label(window, text = "Gender:", width=20, font =("bold", 10))
label7.place(x = 64, y = 420)

but_signup = Button(window, text = "Sign Up", width=12, relief = "groove",bg = "brown", fg = "black", font=("arial", 10, "bold"), command=database).place(x = 100, y = 500)
window.bind("<Return>", database)

but_quit = Button(window, text = "Quit", width=12, relief = "groove",bg = "brown", fg = "black", font=("arial", 10, "bold"), command = exitt).place(x = 280, y = 500)

#but_login= Button(window, text = "Login", width=12, relief = "groove",bg = "brown", fg = "black", font=("arial", 10, "bold"), command = exitt)
#but_login.place(x = 195, y = 560)


window.mainloop()
#to be completed asd
