from tkinter import *
from tkinter import messagebox

def submit():
    def is_integer(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    if snume.get()=="":
        messagebox.showinfo("info","student no. is empty") 
    elif sname.get()=="":
        messagebox.showinfo("info","student name is empty")
    elif saddr.get(1.0,END).strip()=="":
        messagebox.showinfo("info","student address is empty")
    elif s1.get().strip()=="" or not is_integer(s1.get().strip()):
        messagebox.showinfo("info","student marks for subject 1 is empty or not an integer")
    elif s2.get().strip()=="" or not is_integer(s2.get().strip()):
        messagebox.showinfo("info","student marks for subject 2 is empty or not an integer")
    elif s3.get().strip()=="" or not is_integer(s3.get().strip()):
        messagebox.showinfo("info","student marks for subject 3 is empty or not an integer")
    else:
        calculate()

def calculate():
    sub1=int(s1.get().strip())
    sub2=int(s2.get().strip())
    sub3=int(s3.get().strip())
    total = sub1 + sub2 + sub3
    avg = total / 3
    
    result = "pass" if avg >= 35 else "fail"

    ot1.config(text="total marks : "+str(total))
    ot2.config(text="average marks : "+str(avg))
    ot3.config(text="result : "+str(result))
    show_details(total, avg, result)

def show_details(total, avg, result):
    gender = "male" if gen.get() == 1 else "female"
    
    print("student no.:", snume.get())
    print("student name:", sname.get())
    print("student address:", saddr.get(1.0, END).strip())
    print("student gender:", gender)
    print("student marks:", s1.get().strip(), s2.get().strip(), s3.get().strip())
    print("total marks:", total)
    print("average marks:", avg)
    print("result:", result)

def on_enter(e):
    btn.config(background='#7AFC00', foreground='white')

def on_leave(e):
    btn.config(background='#94FF30', foreground='black')
    # btn.config(background='SystemButtonFace', foreground='black')

root = Tk()
root.title("Student marks list")
root.configure(bg="purple1")
root.geometry("600x600")
root.minsize(550,500)

snuml = Label(root, text="enter student no.:", font=("arial", 18, "bold"), bg="purple1")
snuml.place(x=10, y=10)
snume = Entry(root, width=40)
snume.place(x=280, y=20)

snaml = Label(root, text="enter student name:", font=("arial", 18, "bold"), bg="purple1")
snaml.place(x=10, y=40)
sname = Entry(root, width=40)
sname.place(x=280, y=50)

saddrl = Label(root, text="enter student address:", font=("arial", 18, "bold"), bg="purple1")
saddrl.place(x=10, y=70)
saddr = Text(root, height=6, width=30, bg="white")
saddr.place(x=280, y=80)

m4 = Label(root, text="enter gender type:", font=("arial", 18, "bold"), bg="purple1")
m4.place(x=10, y=200)
gen = IntVar()
Radiobutton(root, text="male", value=1, variable=gen, bg="thistle3", font=("arial", 18, "bold")).place(x=280, y=200)
Radiobutton(root, text="female", value=2, variable=gen, bg="thistle3", font=("arial", 18, "bold")).place(x=390, y=200)

m5 = Label(root, text="enter student marks:", font=("arial", 18, "bold"), bg="purple1")
m5.place(x=10, y=250)
s1 = Entry(root, width=8)
s1.place(x=280, y=260)
s2 = Entry(root, width=8)
s2.place(x=340, y=260)
s3 = Entry(root, width=8)
s3.place(x=400, y=260)

btn=Button(root, text="Get result",font=("arial", 15, "bold"), command=submit)
btn.place(x=220, y=300)
btn.bind('<Enter>', on_enter)
btn.bind('<Leave>', on_leave)

f = Frame(root, height=5, width=400, bg="#D3C5E5")
f.place(x=80, y=350)

ot1 = Label(root, text="total marks:", font=("arial", 18, "bold"), bg="purple1")
ot1.place(x=10, y=365)
ot2 = Label(root, text="average marks:", font=("arial", 18, "bold"), bg="purple1")
ot2.place(x=10, y=395)
ot3 = Label(root, text="result:", font=("arial", 18, "bold"), bg="purple1")
ot3.place(x=10, y=428)

ot4 = Label(root, text="grade:", font=("arial", 18, "bold"), bg="purple1")
ot4.place(x=10, y=460)

ot5 = Label(root, text="remarks:", font=("arial", 18, "bold"), bg="purple1")
ot5.place(x=10, y=500)

root.mainloop()
