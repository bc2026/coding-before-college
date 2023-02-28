from tkinter import Tk
import tkinter

n = int(input("How many buttons? "))
center = 500
OFF = 1000
rt = Tk()


vals = []
for p in range(0, n+1):
    vals.append(p)

ops = []

def buttons(num=0, off=0):
    for i in range(3):    
        for j in range(3):
            locals()[str(num)] = tkinter.Button(rt, text=str(vals[num]))
            locals()[str(num)].pack()
        locals()[str(num+1)] = tkinter.Button(rt, text="button")
        locals()[str(num+1)].pack()
        
             
buttons()

rt.mainloop()