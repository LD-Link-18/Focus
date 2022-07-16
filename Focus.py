import os
import ctypes
from tkinter import *
import time

global r_num
r_num = 5
font_ = ("Arial",25)
running = False
break_switch = False

li1 = []

def main():

    l =  list(os.popen('tasklist').readlines())

    for i in l:
        for k in li1:
            try:
                if k in i:
                    os.system('taskkill /f /im {}'.format(k))
                    ctypes.windll.user32.MessageBoxW(0, 'Get back to work!', 'Alert!', 0)
                else:
                    pass
            except:
                pass

def scanning():
    global break_switch
    if break_switch:
        b = time.time()
        c = b - a
        if c >= 60:
            break_switch = False
            global running
            running = True       
    if running:
        on_off.config(text="ON")
        main()
    elif not running:
        on_off.config(text="OFF")
    root.after(500,scanning)            

def start():
    global running
    running = True

def stop():
    global running
    running = False

def break_():
    global running
    running = False
    global break_switch
    break_switch = True
    global a
    a = time.time()

class labels:
    def adding_label(self):
        global r_num
        r_num += 1
        la = Label(root,text=q,font=font_)
        la.grid(row=r_num,column=0)

def add_program():
    nw = Toplevel(root)
    e = Entry(nw,font=font_)
    e.pack()
    def actually_adding_the_program():
        global q
        q = e.get()
        li1.append(q)
        x = labels()
        x.adding_label()
    b = Button(nw,text="Add program",font=font_,command=actually_adding_the_program)
    b.pack()

root = Tk()
root.title("Focus")

on_off = Label(root,text="OFF",font=font_)
b_start = Button(root,text="Start",font=font_,command=start)
b_stop = Button(root,text="Stop",font=font_,command=stop)
b_break = Button(root,text="Take a break for 1 munite",font=font_,command=break_)
b_add_program = Button(root,text="Add program",font=font_,command=add_program)

on_off.grid(row=0, columnspan=3)
b_start.grid(row=1, columnspan=3)
b_stop.grid(row=2, columnspan=3)
b_break.grid(row=3, columnspan=3)
b_add_program.grid(row=4, columnspan=3)

root.after(1000,scanning)
root.mainloop()