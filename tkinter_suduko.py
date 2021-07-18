
from tkinter import *
from tkinter import messagebox
from tkinter import font

window = Tk()
window.title("Small Suduko")
window.geometry('400x470')
window.resizable(width=0,height=0)

def reset():
    b_1 = Button(window,text=" ",command=lambda:click(1),bg="black",height=5,width=10)
    b_2 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
    b_3 = Button(window,text=" ",command=lambda:click(3),bg="black",height=5,width=10)
    b_4 = Button(window,text=" ",command=lambda:click(4),bg="black",height=5,width=10)
    b_5 = Button(window,text=" ",command=lambda:click(5),bg="black",height=5,width=10)

    b_6 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
    b_7 = Button(window,text=" ",command=lambda:click(7),bg="black",height=5,width=10)
    b_8 = Button(window,text=" ",command=lambda:click(8),bg="black",height=5,width=10)
    b_9 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)
    b_10 = Button(window,text="",command=lambda:click(10),bg="black",height=5,width=10)

    b_11 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)
    b_12 = Button(window,text=" ",command=lambda:click(12),bg="black",height=5,width=10)
    b_13 = Button(window,text=" ",command=lambda:click(13),bg="black",height=5,width=10)
    b_14 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
    b_15 = Button(window,text=" ",command=lambda:click(15),bg="black",height=5,width=10)

    b_16 = Button(window,text=" ",command=lambda:click(16),bg="black",height=5,width=10)
    b_17 = Button(window,text=" ",command=lambda:click(17),bg="black",height=5,width=10)
    b_18 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)
    b_19 = Button(window,text="",command=lambda:click(19),bg="black",height=5,width=10)
    b_20 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)

    b_21 = Button(window,text=" ",command=lambda:click(21),bg="black",height=5,width=10)
    b_22 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
    b_23 = Button(window,text=" ",command=lambda:click(23),bg="black",height=5,width=10)
    b_24 = Button(window,text=" ",command=lambda:click(24),bg="black",height=5,width=10)
    b_25 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)

    b_1.grid(row=0,column=0)
    b_2.grid(row=0,column=1)
    b_3.grid(row=0,column=2)
    b_4.grid(row=0,column=3)
    b_5.grid(row=0,column=4)

    b_6.grid(row=1,column=0)
    b_7.grid(row=1,column=1)
    b_8.grid(row=1,column=2)
    b_9.grid(row=1,column=3)
    b_10.grid(row=1,column=4)

    b_11.grid(row=2,column=0)
    b_12.grid(row=2,column=1)
    b_13.grid(row=2,column=2)
    b_14.grid(row=2,column=3)
    b_15.grid(row=2,column=4)

    b_16.grid(row=3,column=0)
    b_17.grid(row=3,column=1)
    b_18.grid(row=3,column=2)
    b_19.grid(row=3,column=3)
    b_20.grid(row=3,column=4)

    b_21.grid(row=4,column=0)
    b_22.grid(row=4,column=1)
    b_23.grid(row=4,column=2)
    b_24.grid(row=4,column=3)
    b_25.grid(row=4,column=4)

def revel():
    b_1 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)
    b_2 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
    b_3 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)
    b_4 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)
    b_5 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)

    b_6 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
    b_7 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)
    b_8 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
    b_9 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)
    b_10 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)

    b_11 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)
    b_12 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)
    b_13 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
    b_14 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
    b_15 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)

    b_16 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
    b_17 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)
    b_18 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)
    b_19 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
    b_20 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)

    b_21 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)
    b_22 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
    b_23 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)
    b_24 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)
    b_25 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)

    b_1.grid(row=0,column=0)
    b_2.grid(row=0,column=1)
    b_3.grid(row=0,column=2)
    b_4.grid(row=0,column=3)
    b_5.grid(row=0,column=4)

    b_6.grid(row=1,column=0)
    b_7.grid(row=1,column=1)
    b_8.grid(row=1,column=2)
    b_9.grid(row=1,column=3)
    b_10.grid(row=1,column=4)

    b_11.grid(row=2,column=0)
    b_12.grid(row=2,column=1)
    b_13.grid(row=2,column=2)
    b_14.grid(row=2,column=3)
    b_15.grid(row=2,column=4)

    b_16.grid(row=3,column=0)
    b_17.grid(row=3,column=1)
    b_18.grid(row=3,column=2)
    b_19.grid(row=3,column=3)
    b_20.grid(row=3,column=4)

    b_21.grid(row=4,column=0)
    b_22.grid(row=4,column=1)
    b_23.grid(row=4,column=2)
    b_24.grid(row=4,column=3)
    b_25.grid(row=4,column=4)




def store_value():
    global g_value
    global store_number
    if g_value == 1:
     b_1 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_1.grid(row=0,column=0)
    elif g_value == 3:
     b_3 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_3.grid(row=0,column=2)
    elif g_value == 4:
     b_4 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_4.grid(row=0,column=3)
    elif g_value == 5:
     b_5 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_5.grid(row=0,column=4)
    elif g_value == 7:
     b_7 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_7.grid(row=1,column=1)
    elif g_value == 8:
     b_8 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_8.grid(row=1,column=2)
    elif g_value == 10:
     b_10 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_10.grid(row=1,column=4)
    elif g_value == 12:
     b_12 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_12.grid(row=2,column=1)
    elif g_value == 13:
     b_13 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_13.grid(row=2,column=2)
    elif g_value == 15:
     b_15 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_15.grid(row=2,column=4)
    elif g_value == 16:
     b_16 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_16.grid(row=3,column=0)
    elif g_value == 17:
     b_17 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_17.grid(row=3,column=1)
    elif g_value == 19:
     b_19 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_19.grid(row=3,column=3)
    elif g_value == 21:
     b_21 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_21.grid(row=4,column=0)
    elif g_value == 23:
     b_23 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_23.grid(row=4,column=2)
    elif g_value == 24:
     b_24 = Button(window,text=store_number,command=lambda:click(1),bg="black",fg="White",height=5,width=10)
     b_24.grid(row=4,column=3)




def clear():
    take.delete(0,END)

def take_value(x,y):
    global take
    take = Entry(window,width=2,font=2)
    take.grid(row=x,column=y)
    take.focus()



def enter():
    global store_number
    store_number = int(take.get())
    if store_number == 1 or store_number == 2 or store_number == 3 or store_number == 4 or store_number == 5:
        store_value()
    else:
        messagebox.showerror("Error","Enter The Number In Range 1 to 5")
    
    
    


def click(value):
    global g_value
    if value == 1:
     g_value = 1
     take_value(0,0)
    elif value == 3:
     g_value = 3
     take_value(0,2)
    elif value == 4:
     g_value = 4
     take_value(0,3)
    elif value == 5:
     g_value = 5
     take_value(0,4)
    elif value == 7:
     g_value = 7
     take_value(1,1)
    elif value == 8:
     g_value = 8
     take_value(1,2)
    elif value == 10:
     g_value = 10
     take_value(1,4)
    elif value == 12:
     g_value = 12
     take_value(2,1)
    elif value == 13:
     g_value = 13
     take_value(2,2)
    elif value == 15:
     g_value = 15
     take_value(2,4)
    elif value == 16:
     g_value = 16
     take_value(3,0)
    elif value == 17:
     g_value = 17
     take_value(3,1)
    elif value == 19:
     g_value = 19
     take_value(3,3)
    elif value == 21:
     g_value = 21
     take_value(4,0)
    elif value == 23:
     g_value = 23
     take_value(4,2)
    elif value == 24:
     g_value = 24
     take_value(4,3)

     


    
    

global b_1,b_2,b_3,b_4,b_5
global b_6,b_7,b_8,b_9,b_10
global b_11,b_12,b_13,b_14,b_15
global b_16,b_17,b_18,b_19,b_20
global b_21,b_22,b_23,b_24,b_25
global b_reset,b_revel,b_enter,b_check

b_1 = Button(window,text=" ",command=lambda:click(1),bg="black",height=5,width=10)
b_2 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
b_3 = Button(window,text=" ",command=lambda:click(3),bg="black",height=5,width=10)
b_4 = Button(window,text=" ",command=lambda:click(4),bg="black",height=5,width=10)
b_5 = Button(window,text=" ",command=lambda:click(5),bg="black",height=5,width=10)

b_6 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
b_7 = Button(window,text=" ",command=lambda:click(7),bg="black",height=5,width=10)
b_8 = Button(window,text=" ",command=lambda:click(8),bg="black",height=5,width=10)
b_9 = Button(window,text="2",state=DISABLED,bg="black",height=5,width=10)
b_10 = Button(window,text=" ",command=lambda:click(10),bg="black",height=5,width=10)

b_11 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)
b_12 = Button(window,text=" ",command=lambda:click(12),bg="black",height=5,width=10)
b_13 = Button(window,text=" ",command=lambda:click(13),bg="black",height=5,width=10)
b_14 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)
b_15 = Button(window,text=" ",command=lambda:click(15),bg="black",height=5,width=10)

b_16 = Button(window,text=" ",command=lambda:click(16),bg="black",height=5,width=10)
b_17 = Button(window,text=" ",command=lambda:click(17),bg="black",height=5,width=10)
b_18 = Button(window,text="3",state=DISABLED,bg="black",height=5,width=10)
b_19 = Button(window,text=" ",command=lambda:click(19),bg="black",height=5,width=10)
b_20 = Button(window,text="5",state=DISABLED,bg="black",height=5,width=10)

b_21 = Button(window,text=" ",command=lambda:click(21),bg="black",height=5,width=10)
b_22 = Button(window,text="1",state=DISABLED,bg="black",height=5,width=10)
b_23 = Button(window,text=" ",command=lambda:click(23),bg="black",height=5,width=10)
b_24 = Button(window,text=" ",command=lambda:click(24),bg="black",height=5,width=10)
b_25 = Button(window,text="4",state=DISABLED,bg="black",height=5,width=10)

b_reset = Button(window,text="Reset",bg="Purple",width=10,height=2,command=reset)
b_clear = Button(window,text="Clear",bg="Red",width=10,height=2,command=clear)
b_revel = Button(window,text="Revel",bg="Pink",width=10,height=2,command=revel)

b_enter = Button(window,text="Enter",bg="Red",width=10,height=2,command=enter)

b_check = Button(window,text="Check",bg="Yellow",width=10,height=2)

b_1.grid(row=0,column=0)
b_2.grid(row=0,column=1)
b_3.grid(row=0,column=2)
b_4.grid(row=0,column=3)
b_5.grid(row=0,column=4)

b_6.grid(row=1,column=0)
b_7.grid(row=1,column=1)
b_8.grid(row=1,column=2)
b_9.grid(row=1,column=3)
b_10.grid(row=1,column=4)

b_11.grid(row=2,column=0)
b_12.grid(row=2,column=1)
b_13.grid(row=2,column=2)
b_14.grid(row=2,column=3)
b_15.grid(row=2,column=4)

b_16.grid(row=3,column=0)
b_17.grid(row=3,column=1)
b_18.grid(row=3,column=2)
b_19.grid(row=3,column=3)
b_20.grid(row=3,column=4)

b_21.grid(row=4,column=0)
b_22.grid(row=4,column=1)
b_23.grid(row=4,column=2)
b_24.grid(row=4,column=3)
b_25.grid(row=4,column=4)

b_reset.grid(row=5,column=0)
b_check.grid(row=5,column=1)
b_clear.grid(row=5,column=2)
b_enter.grid(row=5,column=3)
b_revel.grid(row=5,column=4)



window.mainloop()