import tkinter as tk; from tkinter import *; import os
from PIL import ImageTk, Image
#Main code=====================================================================================================
#==============================================================================================================
main_root = Tk();main_root.geometry('1000x450');
main_root.title("Practical Homies"); main_root.resizable(0, 0)  
main_root.iconbitmap(os.getcwd() + '\\AEC_logo.ico')
frame = Frame(main_root); frame.pack(fill='both', expand = True)

#Creating the canvas1 to take inputs.
canvas1 = Canvas(frame, bg = 'gray90') ; canvas1.pack(side='left', fill = 'both')
def moved(event): canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
canvas1.bind("<Motion>", moved); tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west
#Creating the canvas for animation
canvas = Canvas(frame, bg = 'gray90', height=700); canvas.pack(side='left', fill = 'both', expand = YES) 
def moved(event):  canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
canvas.bind("<Motion>", moved); tag = canvas.create_text(10, 10, text="", anchor="nw")


img = ImageTk.PhotoImage(Image.open('White_Canvas.jpg'))
panel = Label(canvas, image = img); panel.pack(side = "bottom", fill = "both", expand = "yes"); panel.pack(); panel.place(x=10, y=10)

img1 = ImageTk.PhotoImage(Image.open('Black_Canvas.jpg'))
panel1 = Label(canvas1, image = img1); panel1.pack(side = "bottom", fill = "both", expand = "yes"); panel1.pack(); panel1.place(x=10, y=10)

buttons = []

def first_semester(buttons): 
    if len(buttons)>0:
        #print(buttons)
        def af(): os.system('python Tortional_Pendulum_Simulation.py')
        def bf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        def cf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        def df(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        def ef(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        buttons[0]['text'] =  "1. Determination of modulus of rigidity by dynamic method"
        buttons[1]['text'] =  "2. Determination of modulus of rigidity by static method"
        buttons[2]['text'] =  "3. Determination of Young's modulus by Flexure method"
        buttons[3]['text'] =  "4. Determine unknown resistence using Carry Fosters Bridge"
        buttons[4]['text'] =  "5. Determination of wavelength of light by by Newton's \n   ring method"
        #buttons[0]['text'] =  "1. Determination of modulus of rigidity by dynamic method"
    else:
        def af(): os.system('python Tortional_Pendulum_Simulation.py')
        a = Button(canvas, text="1. Determination of modulus of rigidity by dynamic method", bg='black', fg='white', command=af)
        a.config(font=("Courier", 12, 'bold'));a.pack();a.place(x=20, y=60)

        def bf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        b = Button(canvas, text="2. Determination of modulus of rigidity by static method", bg='black',  fg='white', command=bf)
        b.config(font=("Courier", 12, 'bold'));b.pack();b.place(x=20, y=120)

        def cf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        c = Button(canvas, text="3. Determination of Young's modulus by Flexure method", bg='black',  fg='white', command=cf)
        c.config(font=("Courier", 12, 'bold'));c.pack();c.place(x=20, y=180)

        def df(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        d = Button(canvas, text="4. Determine unknown resistence using Carry Fosters Bridge", bg='black',  fg='white', command=df)
        d.config(font=("Courier", 12, 'bold'));d.pack();d.place(x=20, y=230)

        def ef(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        e = Button(canvas, text="5. Determination of wavelength of light by by Newton's \n   ring method", justify='left', bg='black', fg='white',command=ef)
        e.config(font=("Courier", 12, 'bold'));e.pack();e.place(x=20, y=280)

        #def ff(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        #f = Button(canvas, text="6. Determination of wavelength of light by by Newton's \n   ring method",justify='left',bg='black',fg='white',command=ef)
        #f.config(font=("Courier", 12, 'bold'));e.pack();e.place(x=20, y=340)
        
        buttons.extend([a, b, c, d, e])
first_sem = Button(canvas1, text="  First Semester  ", bg='light yellow2', command=lambda: first_semester(buttons))
first_sem.config(font=("Courier", 14, 'bold'));first_sem.pack(); first_sem.place(x=70, y=180)


def second_semester(buttons):
    if len(buttons)>0:
        #print(buttons)
        def af(): os.system('python Tortional_Pendulum_Simulation.py')
        def bf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        def cf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        def df(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        def ef(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        buttons[0]['text'] =  "1. Determination of wavelength of light by laser \ndiffraction method"
        buttons[1]['text'] =  "2. Determination of specific charge(e/m) by \nJ.J. Thomson's method"
        buttons[2]['text'] =  "3. Determination of band gap of semiconductor"
        buttons[3]['text'] =  "4. Determine Plank's constant using photocell"
        buttons[4]['text'] =  "5. Determination of Hall coeff. of a semiconductor \n   by four probe method"
    else:
        def af(): os.system('python Tortional_Pendulum_Simulation.py')
        a = Button(canvas, text="1. Determination of wavelength of light by laser \n   diffraction method", justify='left', bg='black', fg='white', command=af)
        a.config(font=("Courier", 12, 'bold'));a.pack();a.place(x=20, y=60)

        def bf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        b = Button(canvas, text="2. Determination of specific charge(e/m) by \n   J.J. Thomson's method", justify='left', bg='black',  fg='white', command=bf)
        b.config(font=("Courier", 12, 'bold'));b.pack();b.place(x=20, y=120)

        def cf(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        c = Button(canvas, text="3. Determination of band gap of semiconductor", justify='left', bg='black',  fg='white', command=cf)
        c.config(font=("Courier", 12, 'bold'));c.pack();c.place(x=20, y=180)

        def df(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        d = Button(canvas, text="4. Determine Plank's constant using photocell", justify='left', bg='black',  fg='white', command=df)
        d.config(font=("Courier", 12, 'bold'));d.pack();d.place(x=20, y=230)

        def ef(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        e = Button(canvas, text="5. Determination of Hall coeff. of a semiconductor \n   by four probe method", justify='left', bg='black', fg='white', command=ef)
        e.config(font=("Courier", 12, 'bold'));e.pack();e.place(x=20, y=280)

        #def ff(): pass #os.system('python Tortional_Pendulum_Simulation.py')
        #f = Button(canvas, text="6. Determination of wavelength of light by by Newton's \n   ring method",justify='left',bg='black',fg='white',command=ef)
        #f.config(font=("Courier", 12, 'bold'));e.pack();e.place(x=20, y=340)

        buttons.extend([a, b, c, d, e])

second_sem = Button(canvas1, text="  Second Semester  ", bg='light yellow2', command=lambda: second_semester(buttons))
second_sem.config(font=("Courier", 14, 'bold'));second_sem.pack(); second_sem.place(x=70, y=250)

main_root.mainloop()
