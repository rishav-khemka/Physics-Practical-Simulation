import tkinter as tk; from tkinter import *; import os;

instr_root = Tk(); instr_root.geometry('550x350'); instr_root.title("[Tortional Pendulum Instructions]"); 
instr_root.iconbitmap(os.getcwd() + '\\AEC_logo.ico')
tort_instr_canvas = Canvas(instr_root, bg = 'lemon chiffon', height=700); tort_instr_canvas.pack(side='left', fill = 'both', expand = YES) 
def moved(event):  tort_instr_canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y)) 
tort_instr_canvas.bind("<Motion>", moved); tag = tort_instr_canvas.create_text(10, 10, text="", anchor="nw") 
y = [30, 100, 190];
strings = ['1. All the inputs assumes CGS system. So L, r,\n R are in cm, M is in g',
           "2. If you enter a combination of values,then  \n   that set of values works only after you've\n "+
           '  pressed the okay button',
           "3. Once the start button is pressed, the n no.\n   of oscillations will always complete. "+
           "But \n   for that you needn't wait. If you've missed \n   any oscillation during observation,"+
           " you can \n   restart your observation by pressing the \n   start button each time you need.", 
          ]
for i in range(len(y)):
    tort_instr_label = Label(tort_instr_canvas,text=strings[i], justify = LEFT, bg='tan1',fg='black',borderwidth=10)
    tort_instr_label.config(font=("Courier", 12, 'bold')); tort_instr_label.pack(); tort_instr_label.place(x=30, y=y[i])
instr_root.mainloop()