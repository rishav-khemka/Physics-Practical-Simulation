from tkinter import *
from tkinter import filedialog
import os

root = Tk(); root.withdraw()
current_directory = ''
current_directory = filedialog.askdirectory()

if current_directory == '': exit()


submit_root = Tk(); submit_root.title('Tortional Pendulum Submission Page'); submit_root.geometry('600x300')
submit_root.iconbitmap(os.getcwd() + '\\AEC_logo.ico')
#Create a canvas
submit_canvas = Canvas(submit_root, bg='lemon chiffon')
submit_canvas.pack(fill = 'both', expand = YES)
def moved(event):  submit_canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
submit_canvas.bind("<Motion>", moved); tag = submit_canvas.create_text(10, 10, text="", anchor="nw")


x = [ 100, 100, 400, 100, 250, 400]
y = [  50,  95,  95, 140, 140, 140]
strings = ['Name: ', 'Roll: ', 'Batch: ', 'Sem:  ', 'Year: ', 'Dept:  ']
for i in range(len(strings)):
    label = Label(submit_canvas,font=("Courier",14,'bold'),text=strings[i],bg='Navajo White',fg='black')
    label.pack(); label.place(x=x[i], y=y[i])

x =     [180, 180, 490, 180, 335, 490]
y =     [ 55, 100, 100, 145, 145, 145]
width = [ 20,  20,   5,   5,   5,  5]
index = ['Richik Majumder', '052', 'A12', '7th', '4th', 'CSE']
creds = []
for i in range(len(width)):
    ent = Entry(submit_canvas, font=("Courier",12,'bold'),bg='White',fg='black', width=width[i])
    creds.append(ent); creds[i].pack(); creds[i].place(x=x[i], y=y[i]); 
    #creds[i].insert(0, '');

#f= open(file_path, "w+")#f.close()
all_entries = []
#============================================================================================================
def submit_page1(): 
    root = Tk(); root.title('Tortional Pendulum Submission Page 1'); root.geometry('1000x550')
    #Create a canvas
    canvas = Canvas(root, bg='lemon chiffon'); canvas.pack(fill = 'both', expand = YES)
    def moved(event):  canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas.bind("<Motion>", moved); tag = canvas.create_text(10, 10, text="", anchor="nw")
    #     0  1   2   3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
    x = [30,70,220,410,  30,  70,  70,  70,  70,  30,  70, 150, 230, 310, 390, 450, 570, 710]
    y = [30,60, 60, 60, 150, 190, 230, 270, 310, 360, 390, 390, 390, 390, 390, 390, 390, 390]
    strings = ['1. Table for least count screw gauge:',                           # 0-3
               'Pitch of the \nscrew(p)(cm)', 'No. of circular \nscale division(n)', 'Least count=p/n(cm)\n',
               '2. Determination of vernier constant of vernier callipers:',      #4-8
               'Smallest division in the main scale(x)(cm):', 'No. of division in the venire scale (n):   ',
               'No of coincident main scale division (m):  ',   'Vernire constant: x * (1- m / n) cm =      ',
               '3. To determine the radius of wire using Screw Gauge',            #9-17
               'No. of\n  obs', 'M.S.R\n(cm)', 'C.S.R\n(cm)', 'Total\n(cm)', 'Mean\n(cm)', 
               'Amount of \nerror(cm)', 'Actual\ndiameter(cm)', 'Actual\nRadius(cm)',
              ]
    for i in range(len(y)):                             #justify=LEFT,
        label = Label(canvas,font=("Courier",12,'bold'),text=strings[i],bg='Navajo White',fg='black') 
        label.pack(); label.place(x=x[i], y=y[i])
    
    #          0   1   2   3   4   5   6     7   8   9  10  11  12  13  14  15  16  17  18
    x =     [ 70,220,410,530,530,530,530,   70,150,230,310,390,450, 70,150,230,310,390,450]
    y =     [110,110,110,190,230,270,310,  440,440,440,440,440,440,470,470,470,470,470,470]
    width = [ 13, 17, 19, 15, 15, 15, 15,    6,  5,  5,  5,  4, 10,  6,  5,  5,  5,  4, 10]
    #             19   20   21   22   23   24 
    x.extend(   [ 70, 150, 230, 310, 390, 450, 570, 710])
    y.extend(   [500, 500, 500, 500, 500, 500, 470, 470])
    width.extend([ 6,   5,   5,   5,   4,  10,  12,  10])
    entries = []
    
    for i in range(len(y)):                             
        ent = Entry(canvas, font=("Courier",12,'bold'),bg='White',fg='black', width=width[i])
        entries.append(ent); entries[i].pack(); entries[i].place(x=x[i], y=y[i])  
        #entries[i].insert(0, str(i))
    #submit button.
    def submit(entries): 
        #f=open(file_path, "a+") #for i in entries: f.write(i.get() + '\n') #for i in range(len(entries)): f.write(entries[i].get() + '\n') #f.close()
        all_entries.extend(entries)
        root.destroy()  
    subm_curr_page = Button(canvas, text="Submit and\nClose", bg='peach puff3', command=lambda: submit(entries))
    subm_curr_page.config(font=("Courier", 14, 'bold'));subm_curr_page.pack();subm_curr_page.place(x=850, y=460)

button1 = Button(submit_canvas, text="Submit observations page 1", bg='peach puff3', command= submit_page1)
button1.config(font=("Courier", 12, 'bold')); button1.pack(); button1.place(x=100, y=200)
 

#============================================================================================================ 
def submit_page2(): 
    root = Tk(); root.title('Tortional Pendulum Submission Page 1'); root.geometry('1000x620')
    #Create a canvas
    canvas = Canvas(root, bg='lemon chiffon'); canvas.pack(fill = 'both', expand = YES)
    def moved(event):  canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas.bind("<Motion>", moved); tag = canvas.create_text(10, 10, text="", anchor="nw")

    #      0    1    2    3    4    5    6    7    8    9   10   11   12
    x = [ 30,  70, 150, 220, 290, 360, 420,  30,  70, 160, 310, 490, 620,  30,  30,  30,  30,  30,  30]
    y = [ 30,  60,  60,  60,  60,  60,  60, 230, 260, 260, 260, 260, 260, 420, 450, 480, 510, 540, 570]
    strings = ['4. To Determine the Radius of Cylinder Using Vernier Callipers ', #0-5
               'No. of\n obs', 'M.S.R\n(cm)', 'C.S.R\n(cm)', 'Total\n(cm)', 'Mean\n(cm)', 'Actual radius\n(cm)',
               '5. Determination of time period of cylinder', 
               'No. of \n obs\n', 'No. of \noscillations \nobserved(n)', 
               'Time taken\nfor oscillations\n(Tn)(s)', "Time period\n T'=Tn/n(s)\n", 'Mean \nTime period(T)\n',
               
               'Length of the experimental wire = (l1+l2+l3) / 3 cm =        (cm)        ',
               'Radius of the experimental wire = (r1+r2+r3) / 3 cm =        (cm)        ',
               'Radius of the cylinder = (r1+r2+r3) / 3 cm          =        (cm)        ',
               'Time period of the cylinder = (t1+t2+t3) / 3 s      =        (s)         ',
               'Mass of the cylinder(g)                             =        (g)         ',
               'Result : Modulus of rigidity of the given material  =        (dyne / cm2)'
              ]
    labels = []
    for i in range(len(strings)):
        labels.append( Label(canvas, text=strings[i], font=("Courier",12,'bold'), bg = 'Navajo White', fg='black') )
        labels[i].pack(); labels[i].place(x=x[i], y=y[i])

    #          0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
    x =     [ 70, 150, 220, 290,  70, 150, 220, 290,  70, 150, 220, 290, 360, 420]#,  70]
    y =     [110, 110, 110, 110, 140, 140, 140, 140, 170, 170, 170, 170, 140, 140]#, 330]
    width = [  6,   5,   5,   5,   6,   5,   5,   5,   6,   5,   5,   5,   4,  13]#,   7]
    entries = []
    index = 0
    for i in range(len(width)):
        ent = Entry(canvas, font=("Courier",12,'bold'),bg='White',fg='black', width=width[i])
        entries.append(ent); entries[i].pack(); entries[i].place(x=x[i], y=y[i]); 
        entries[i].insert(0, ''); index +=1
    #          0    1    2    3      4    5    6    7      8    9   10   11     12
    x =     [ 70, 160, 310, 490,    70, 160, 310, 490,    70, 160, 310, 490,   620]
    y =     [330, 330, 330, 330,   360, 360, 360, 360,   390, 390, 390, 390,   360]
    width = [  7,  13,  16,  11,   7,  13,  16,  11,   7,  13,  16,  11,  14]
    entries1 = []
    for i in range(len(width)):
        ent = Entry(canvas, font=("Courier",12,'bold'),bg='White',fg='black', width=width[i])
        entries1.append(ent); entries1[i].pack(); entries1[i].place(x=x[i], y=y[i]); 
        #entries1[i].insert(0, ''); index+=1
        #entries1[i].insert(0, str(index)); index+=1

    entries.extend( entries1 )

    x =     [570, 570, 570, 570, 570, 570]
    y=      [420, 450, 480, 510, 540, 570]
    width = [  6,   6,   6,   6,   6,   6]
    entries1 = []
    for i in range(len(y)):
        ent = Entry(canvas, font=("Courier",12,'bold'),bg='White',fg='black', width=width[i])
        entries1.append(ent); entries1[i].pack(); entries1[i].place(x=x[i], y=y[i]); 
        #entries1[i].insert(0, ''); index+=1
        #entries1[i].insert(0, str(index)); index+=1
    entries.extend(entries1)


    def submit(strings, entries):
        #f=open(file_path, "a+") for i in range(len(entries)): f.write(entries[i].get() + '\n') f.close()
        all_entries.extend(entries)
        root.destroy()  
    subm_curr_page = Button(canvas, text="Submit and\nClose", bg='peach puff3', command=lambda: submit(strings, entries))
    subm_curr_page.config(font=("Courier", 14, 'bold'));subm_curr_page.pack();subm_curr_page.place(x=850, y=530)


    root.mainloop()
    
button2 = Button(submit_canvas, text="Submit observations page 2", bg='peach puff3', command= submit_page2) 
button2.config(font=("Courier", 12, 'bold')); button2.pack(); button2.place(x=100, y=250) 

def submit_final(all_entries, current_directory):
    import os
    while True:
      try:
        name = creds[0].get().split()
        name = name[0] + '_' + name[1]
        name += '_' + creds[1].get() + '_' + creds[2].get() + '_' + creds[3].get() + '_' + creds[4].get() + '_' + creds[5].get()
        name += '_Tortional_Pendulum.pdf'                   #os.rename('tort.txt', name+'.txt')
        break
      except: continue
    file_path = os.path.join(current_directory, name)

    print(file_path)


    x = [ 50,  70,  50,  70,  70,  70,  70,  50,  70,  70,  50,  70,  70,  50,  70,  70,  50,  50,  50,  50,  50, 50]
    y = [745, 720, 680, 660, 640, 620, 600, 570, 545, 530, 440, 415, 400, 310, 285, 270, 180, 160, 140, 120, 100, 80]
    strings = ['1. Table for least count screw gauge:',                     
               'Pitch of the screw(p)(cm)      No. of circular scale division(n)      Least count=p/n(cm)',

               '2. Determination of vernier constant of vernier callipers:',      
               'Smallest division in the main scale(x)(cm):', 'No. of division in the venire scale (n):   ',
               'No of coincident main scale division (m):  ',   'Vernire constant: x * (1- m / n) cm =      ',

               '3. To determine the radius of wire using Screw Gauge',            
               'No. of obs    M.S.R.    C.S.R.    Total   Mean    Amt of error   Actual diameter  Actual Radius', 
               '                     (cm)         (cm)       (cm)     (cm)        (cm)               (cm)'+
               '                    (cm)',

               '4. To Determine the Radius of Cylinder Using Vernier Callipers ',
               'No. of obs    M.S.R.    C.S.R.    Total   Mean    Actual Radius',
               '                     (cm)         (cm)       (cm)     (cm)             (cm)',

               '5. Determination of time period of cylinder', 
               "No. of obs    No. of oscillations       Time taken for               Time period       Mean Time period(T)",
               "                        observed(n)              oscillations(Tn)(s)         T'=Tn/n(s) ",

               'Length of the experimental wire = (l1+l2+l3) / 3 cm  =        (cm)        ',
               'Radius of the experimental wire = (r1+r2+r3) / 3 cm  =        (cm)        ',
               'Radius of the cylinder = (r1+r2+r3) / 3 cm .................=        (cm)        ',
               'Time period of the cylinder = (t1+t2+t3) / 3 s.............=        (s)         ',
               'Mass of the cylinder(g)................................................=        (g)         ',
               'Result : Modulus of rigidity of the given material.......=        (dyne / cm2)'
              ]

    import os
    if os.path.exists(file_path): os.remove(file_path) 
    from reportlab.pdfgen.canvas import Canvas
    page = Canvas(file_path, pagesize=(612.0, 792.0)); page.setFont("Times-Roman", 12)
    
    for i in range(len(strings)): page.drawString(x[i], y[i], strings[i])
    
    page.save()
    submit_root.destroy()
    exit()
subm_final = Button(submit_canvas, text="Send", bg='peach puff3', command=lambda: submit_final(all_entries, current_directory))
subm_final.config(font=("Courier", 14, 'bold'));subm_final.pack();subm_final.place(x=460, y=240)


submit_root.mainloop() 