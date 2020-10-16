import tkinter as tk; from tkinter import *; import numpy as np; import webbrowser; import time; from time import sleep; import os

class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0;          self.nextTime = 0.0;    self.onRunning = 0; self.timestr = StringVar();    self.MakeWidget()
    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("Courier", 12), fg="pale turquoise", bg="black")
        self.SetTime(self.nextTime);    timeText.pack(fill=X, expand=NO, pady=2, padx=2)
    def Updater(self):
        self.nextTime = time.time() - self.startTime; self.SetTime(self.nextTime); self.timer = self.after(50, self.Updater)
    def SetTime(self, nextElap):
        minutes = int(nextElap / 60); seconds = int(nextElap - minutes * 60.0); miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100); 
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime; self.Updater(); self.onRunning = 1; draw_on_next_canvas()
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer);    self.nextTime = time.time() - self.startTime; self.SetTime(self.nextTime);      self.onRunning = 0
    def Exit(self):  tort_pendulum_root.destroy(); exit()
    def Reset(self): self.startTime = time.time(); self.nextTime = 0.0; self.SetTime(self.nextTime)


#Utility functions========================================================================================================================
#=========================================================================================================================================
def circle_of_the_arc(*args):
    start_of_string_x, start_of_string_y, radius_of_bob = args
    t = np.linspace(-10, 10, 200); x = start_of_string_x + radius_of_bob * np.cos(t); 
    y = start_of_string_y+radius_of_bob*np.sin(t); return x, y
def filter_arc_points(*args):
    li, start_of_string_y = args; se = set(); x = []; y = []
    for i in li:
        if i[0] in se or i[1] in se  : continue
        elif i[1] < start_of_string_y: continue
        else: se.add(i[0]); x.append(i[0]); y.append(i[1])
    del(se); return x, y
def select_arc_points(*args): 
    x, y, start_of_string_x, start_of_string_y, end_of_string_x, end_of_string_y, length, theta = args
    li = sorted( [[i, j] for i, j in zip(x, y)], key = lambda x : [x[0], x[1]])  
    left_limit_x  = start_of_string_x-length*np.sin(theta/64); left_limit_y=start_of_string_y+length*np.cos(theta/8)
    right_limit_x = start_of_string_x+length*np.sin(theta/64); right_limit_y=start_of_string_y + length*np.cos(theta/8)
    left_index  = 0; right_index = 0; min_dist_for_left_coord = 10000; min_dist_for_right_coord = 10000
    for curr_index, i in enumerate(li):    #linear search being done on sorted array. Should implement binary search.
        dist_left = np.sqrt(  (i[0] - left_limit_x)**2 + (i[1] - left_limit_y)**2  )
        if dist_left < min_dist_for_left_coord: min_dist_for_left_coord = dist_left; left_index = curr_index
        dist_right = np.sqrt(  (i[0] - right_limit_x)**2 + (i[1] - right_limit_y)**2  )
        if dist_right < min_dist_for_right_coord: min_dist_for_right_coord = dist_right; right_index = curr_index
    if left_index > right_index: left_index, right_index = right_index, left_index 
    li= li[left_index : right_index + 1]; return filter_arc_points(li, start_of_string_y)




#Main code================================================================================================================================
#=========================================================================================================================================
tort_pendulum_root = Tk();tort_pendulum_root.geometry('1000x600');
tort_pendulum_root.title("[Pendulum Practical]"); tort_pendulum_root.iconbitmap(os.getcwd() + '\\AEC_logo.ico')
frame = Frame(tort_pendulum_root); frame.pack(fill='both', expand = True)

#Creating the canvas1 to take inputs.
canvas1 = Canvas(frame, bg = 'peach puff3') ; canvas1.pack(side='left', fill = 'both')
def moved(event): canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
canvas1.bind("<Motion>", moved); tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west
#Creating the canvas for animation
canvas = Canvas(frame, bg = 'lemon chiffon', height=700); canvas.pack(side='left', fill = 'both', expand = YES) 
def moved(event):  canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
canvas.bind("<Motion>", moved); tag = canvas.create_text(10, 10, text="", anchor="nw")


#yt link button.
def YT_Click(): webbrowser.open("https://www.youtube.com/watch?v=07d2dXHYb94", new=1)
youtube_link = Button(canvas1, text="Click here to go to the tutorial", bg='peach puff3', command=lambda: YT_Click())
youtube_link.config(font=("Courier", 12, 'bold')); youtube_link.pack(); youtube_link.place(x=30, y=30)    
#instruction window button.
def tort_instr_window(): os.system('python Tortional_Pendulum_Instruction.py')
instr_tortional_butt = Button(canvas1, text="Instructions", bg='peach puff3', command=tort_instr_window)
instr_tortional_butt.config(font=("Courier", 12, 'bold'));instr_tortional_butt.pack();instr_tortional_butt.place(x=30, y=70)
canvas1.create_line(0, 115, 400, 115, width=2)

y = [130, 200, 270, 340, 410]; labels = []
strings = ['Enter length of the wire(L)(cm):','Enter radius of the wire(r)(cm):','Enter radius of the bob(R):(cm) ', 
           'Enter mass of the bob(M)(g):    ', 'Enter no. of oscillations:      ']
for i in range(len(y)):
    labels.append( Label(canvas1,text=strings[i], justify = LEFT, bg='lemon chiffon', fg='black') )
    labels[i].config(font=("Courier", 12, 'bold')); labels[i].pack(); labels[i].place(x=30, y=y[i])

y = [160, 230, 300, 370, 440]; entries = []
for i in range(len(y)):
    entries.append( Entry(canvas1, relief=tk.FLAT, width = 32) )
    entries[i].pack(padx=20, pady=20); entries[i].place(x=30, y=y[i]); entries[i].config(font=("Courier", 12, 'bold'))

#submit button.
def create_submission_window(): os.system('python Tortional_Pendulum_Submit.py')
submit_tort_butt = Button(canvas1, text="Submit", bg='peach puff3', command=create_submission_window)
submit_tort_butt.config(font=("Courier", 12, 'bold')); submit_tort_butt.pack(); submit_tort_butt.place(x=275, y=545)

def ok_clicked():
    try:    canvas.delete('all'); 
    except: pass  
    stopWatch = StopWatch(canvas1); stopWatch.pack(); stopWatch.place(x=30, y=520)
    Start=Button(canvas1,text='Start', command=stopWatch.Start, width=5); Start.pack(); Start.place(x=30, y=550)
    Stop= Button(canvas1, text='Stop',command=stopWatch.Stop,  width=5); Stop.pack(); Stop.place(x=80, y=550)
    Reset=Button(canvas1, text='Reset',command=stopWatch.Reset, width=5);Reset.pack();Reset.place(x=130, y=550)
    Exit=Button(canvas1,text='Close',command=stopWatch.Exit,  width=5); Exit.pack();  Exit.place(x=180, y=550)
    
ok_button = Button(canvas1, width=5, text = "ok", anchor = CENTER, command = ok_clicked)
ok_button.pack(padx=20, pady = 20); ok_button.place(x=290, y= 480); ok_button.config(font=("Courier", 12, 'bold'))



#Function for animation===================================================================================================================
#=========================================================================================================================================
def draw_on_next_canvas():
    try: 
        L = float(entries[0].get());     r = float(entries[1].get()) ; R = float(entries[2].get()) 
        M = float(entries[3].get());     ita = 8.9*10**11;             theta = 10

        start_of_string_x = 200; start_of_string_y = 330; end_of_string_x = 200; end_of_string_y = start_of_string_y + R
        x, y = circle_of_the_arc(start_of_string_x, start_of_string_y, R*25)
        x, y = select_arc_points(x, y, start_of_string_x, start_of_string_y, end_of_string_x, end_of_string_y, R*25, theta)

        T = ( (4*np.pi*L*M*R**2) / (ita*r**4) )**0.5; len_x = len(x); #print('time_period = ', T*25)
        factor = 0
        if T>=0.0 and T<0.1: factor = 8
        elif T>=0.1 and T<0.2: factor = 5.5
        elif T>=0.2 and T<0.4: factor = 3
        elif T>=0.4 and T<1.1: factor = 2.3
        elif T>=1.1 and T<1.3: factor = 2.2
        elif T>=1.3 and T<2.7: factor = 2.1
        elif T>=2.7 and T<4.0: factor = 2.05
        
        time_gap = T / (len_x * factor)
        rad = R * 25; loop = int( entries[4].get() )
        while loop>0: 
            rem_loop = Label(canvas, text='Remaining oscilations: '+str(loop), bg='lemon chiffon'); 
            rem_loop.config(font=("Courier", 12, 'bold')); rem_loop.pack(); rem_loop.place(x=30, y=40);
            for i in range(len_x):
                try:
                    top_view = canvas.create_oval((start_of_string_x-rad), (start_of_string_y-rad), 
                                                  (start_of_string_x+rad), (start_of_string_y+rad), fill = 'dark slate gray') 
                    indicator = canvas.create_line(start_of_string_x, start_of_string_y, x[i], y[i], fill='snow',width=3) 
                    canvas.update(); time.sleep(time_gap); canvas.delete('all') 
                except: continue
            for i in range(len_x):
                try:
                    top_view=canvas.create_oval((start_of_string_x-rad), (start_of_string_y-rad), 
                                                  (start_of_string_x+rad), (start_of_string_y+rad), fill = 'dark slate gray')
                    indicator=canvas.create_line(start_of_string_x,start_of_string_y,x[len_x-i],y[len_x-i],fill='snow',width=3)
                    canvas.update(); time.sleep(time_gap); canvas.delete('all') 
                except: continue
            loop-=1

        rem_loop = Label(canvas, text='Remaining ossilations: 0', bg='lemon chiffon'); 
        rem_loop.config(font=("Courier", 12, 'bold')); rem_loop.pack(); rem_loop.place(x=30, y=40);
        canvas.delete('all'); canvas.update()
    
    except: pass
    
tort_pendulum_root.mainloop()
