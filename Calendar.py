from tkinter import *
from tkinter import messagebox
import calendar


root = Tk()
root.title("Calendar")
root.geometry("800x650")
root.configure(bg='black')
root.iconbitmap('calendar.ico')
root.resizable(False, False)
Label(root, text="Enter The Year You Want", bg='black', fg='white', font=("times", 15)).pack(pady=10)
i = Entry(root, width=4, bg='black', fg='white', bd=3)
i.pack(pady=0)
c = Text(root, height=40, width=75, bg='black', fg='white')
c.pack(pady=8)



def cal():
    y = i.get()
    if len(y) == 0:
        messagebox.showerror('Error', 'Year Not Entered')
    elif len(y) <4:
        messagebox.showerror('Error', 'Enter The Year Properly!')
    else:
        year = int(y)
        cal_print = calendar.calendar(year)
        c.insert(0.0, cal_print)
        messagebox.showinfo("Calendar", f"Calendar Is Displayed For The Year [{year}]")


def exit():
    d = messagebox.askquestion('Exit Application', "Do You Want Exit Calendar?")
    if d =="yes":
        root.destroy()
    else:
        return None


def clear():
        i.delete(0, END)
        c.delete(0.0, END)


Button(root, text="Create!", command=cal, bg='black', fg='gray', activebackground='black', activeforeground='#00FF00', bd=0).place(x=430, y=50)
Button(root, text="Clear", command=clear, bg='black', fg='gray', activebackground='black', activeforeground='#0000FF', bd=0).place(x=480, y=50)
Button(root, text='Exit', command=exit, bd=0, bg='black', fg='gray', activebackground='black', activeforeground='#ff0000').place(x=520, y=50)

root.mainloop()