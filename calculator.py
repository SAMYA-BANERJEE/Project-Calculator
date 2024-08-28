from tkinter import *
import os
root=Tk()
root.geometry("350x470")   # Adjust size
root.minsize(350, 470)     # set minimum window size value.
root.maxsize(350, 470)     # set maximum window size value.
root.title("Samya's  Calculator")  # add a title in the top of the window.
root.wm_iconbitmap(os.path.join(os.path.dirname(__file__), 'calculator.ico'))
root.configure(bg="#E0E0E0")
#defining function for buttons funtionality:
def click(event):
    global cal_value   # make the cal_value a global variable for getting and setting its value as we want.
    text = event.widget.cget("text")

    if text in "0123456789+-*/%=.!XC":  # allow only valid characters
        if text == "=":   # for '=' command's functionality   
            try:
                cal_value.set(eval(cal_value.get()))
            except Exception as e:
                cal_value.set("Error")
            screen.update()
        elif text == "C":   # for 'C' command's functionality (means clearing the screen)
            cal_value.set("")
            screen.update()
        elif text == "!X":  # for '!X' command's functionality (means clearing the screen one by one element from the left)
            cal_value.set(cal_value.get()[0:-1])
        else:
            cal_value.set(cal_value.get() + text)  # for updating the screen by the inputted text values and expressions.
            screen.update()

   
#the 1st frame where the calculator's screen is alocated and make the screen by a Entry widget.
cal_value=StringVar()
f0=Frame(root,bg="#E0E0E0")
screen=Entry(f0,textvariable=cal_value,relief="solid",highlightthickness=0.5,font=('Courier New', 22,'bold'))
screen.pack(fill="x",padx=10,ipady=5)
f0.pack(fill="x",pady=15)
#The 2nd frame where the functional buttons were alocated and also make them by the Button widget.
# And also bind them with 'click' event.
f=Frame(root)
b=Button(f,text="C",padx=18,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="%",padx=18,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="/",padx=22,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="!X",padx=17,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x")
#The 3rd frame where the functional and non-functional(digits) buttons were alocated and also make them by the Button widget.
# And also bind them with 'click' event.
f=Frame(root)
b=Button(f,text="9",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="8",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="7",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="*",padx=22,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x")
#The 4th frame where the functional and non-functional(digits) buttons were alocated and also make them by the Button widget.
# And also bind them with 'click' event.
f=Frame(root)
b=Button(f,text="6",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="5",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="4",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="-",padx=20,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10,ipadx=2)
b.bind("<Button-1>", click)
f.pack(fill="x")
#The 5th frame where the functional and non-functional(digits) buttons were alocated and also make them by the Button widget.
# And also bind them with 'click' event.
f=Frame(root)
b=Button(f,text="3",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="2",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="1",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="+",padx=20,pady=8,font="Arial 15 bold",bg="grey86")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x")
#The 6th frame where the functional and non-functional(digits) buttons were alocated and also make them by the Button widget.
# And also bind them with 'click' event.
f=Frame(root)
b=Button(f,text="00",padx=18,pady=8,font="Arial 13 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10,ipady=5)
b.bind("<Button-1>", click)
b=Button(f,text="0",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text=".",padx=20,pady=8,font="Arial 15 bold",bg="ghost white")
b.pack(side="left",pady=11,padx=10,ipadx=2)
b.bind("<Button-1>", click)
b=Button(f,text="=",padx=20,pady=8,font="Arial 15 bold",bg="orange red")
b.pack(side="left",pady=11,padx=10)
b.bind("<Button-1>", click)
f.pack(fill="x")
root.mainloop()