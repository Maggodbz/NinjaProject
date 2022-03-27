# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:17:45 2020

@author: marco
"""


import tkinter as tk
import numpy as np
from numpy import sin,cos,exp,sqrt,sinh,cosh,pi,tan,log,arccos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from tkinter import ttk


####Size Main Window####
b = 1200
a = 600



root = tk.Tk()
root.geometry(str(b)+'x'+str(a))
root.title('Approximation is FUN')
root.config(bg='#212946')
root.resizable(height = None, width = None)

#Cyperpunk Theme
plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey
    
    
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=root )
canvas.draw()
canvas.get_tk_widget().place(x =400,y=80,width=880,height=520)


###########################################################################
# P0...Plot
# P1...Funktion Entry field
# P2...right border of the intervall (Default = 1)
# P3...left border of the intervall (Default = -1)
# P4...Label Intervallgrenzen
# Ps0...hidden Label (No function found)


#Default Intervallgrenzen
c = -1
d = 1
  
def Plot():
    global d, c, app1, knots
    if len(P2.get()) != 0:
        d = eval(P2.get())
    if len(P3.get()) !=0:
        c = eval(P3.get())
    n = 1000
    knots = np.linspace(c,d,n)
    
    if len(P1.get())==0:
        Ps0.configure(text='NO FUNCTiON FOUND',fg='#F69602')
        Ps0.place(x=b/2,y=10)    
    else:
        Ps0.configure(fg='#212946')
        fig.clf()
        ax = fig.add_subplot(111)
        ax.plot(knots,[f(x) for x in knots],'#F69602')
        if app1 ==1:
            N = Loadscale.get()
            if N != 1:
                intknots = [c+i*(d-c)/(N-1) for i in range(N)]
                func = [f(x) for x in intknots]
                zero = np.zeros(N)
                ax.plot(intknots,zero,'ro')
                
            elif N == 1:
                ax.plot(0,0,'ro')
        fig.canvas.draw()


def f(x):
    x = x
    return eval(P1.get())

def Tf(x):
    x=1/2*(d-c)*x+1/2*(d+c)
    return eval(P1.get())

    
##Plot Button

P0 = tk.Button(root,text='Plot',command=lambda :Plot())
P0.configure(bg='#F69602')
P0.place(x=b*8/10, y=20, width=130, height=50) 


##Entry Button

#Function
P1 = tk.Entry(root)
P1.place(x=b/2, y=30, width=350, height=30)


#right border
P2 = tk.Entry(root)
P2.place(x=b/2-80, y=35, height=20)
P2.config(width=8)

#left border
P3 = tk.Entry(root)
P3.place(x=b/2-160, y=35, height=20)
P3.config(width=8)

##Label Button

P4 = tk.Label(root, text='Intervallgrenzen')
P4.place(x=b/2-160, y=0, height=30, width=200)
P4.config(bg='#212946', anchor='w',fg='#F69602')

#No Function found Label
Ps0=tk.Label(root)
Ps0.configure(bg='#212946')



################################# Create Notebooks for Tabs


notebook = ttk.Notebook(root)

############ Tab 1 PolynomInterpolation 
# p0...Interpolation mit Äquidistanten Knoten

frame1 = tk.Frame(notebook, width=b/3, height=a-30)
frame1.config(bg ='#212946')


app1 = 0
app2 = 0

def Load():
    global color
    s = Loadscale.get()
    Loadbig = Loadbar.create_polygon(0,100,200,0,200,100,0,100)
    Loadbar.itemconfig(Loadbig,fill='white')
    
    #erzeugt kleines Dreieck und färbt es 
    Loadsmall = Loadbar.create_polygon (0,100,200*(s/100),100-100*(s/100),200*(s/100),100,0,100,fill='#F69602')
    Loadbar.itemconfig(Loadsmall,)
    
    Loadlabel.config(text=str(Loadscale.get()))
    if len(P1.get())!= 0:
        Plot()

def Butcolor():
    global app1
    if app1 ==0:
        p0.config(bg ='#F69602')
        app1 = 1
    else:
        p0.config(bg = 'white')
        app1 = 0
    

#Dividierte Differenzen
def divdiv(X,Y):
    n = len(Y)
    for k in range(1,n):
        for i in range(k,n)[::-1]:
            Y[i]=(Y[i]-Y[i-1])/(X[i]-X[i-k])
    return Y

#Auswertung durch HornerSchema
def Horner(X,Y,x):
    b = Y[-1]
    for i in range(len(Y)-1)[::-1]:
        b = b*(x-X[i])+Y[i]
    return b

def Newton1(x,c):
    if c == 1:
        return Tf(10**(-16))
    else:
        X = np.linspace(-1,1,c)
        Y = [Tf(x) for x in X]
        coef = divdiv(X,Y)
        return Horner(X,coef,x)









#Loadbar für Knoten  
Loadbar = tk.Canvas(frame1,height=100,width=200,bg = '#212946',highlightthickness=0)
Loadbar.place(x=b/7, y=300)
Loadbig = Loadbar.create_polygon(0,100,200,0,200,100,0,100)

#Schieberegler für Loadbar
Loadscale = tk.Scale(frame1)
Loadscale.place(x = b/7, y=410)
Loadscale.config(bg = '#212946',showvalue=0,orient='horizontal',command=lambda x:Load(),length=200,from_=1,to=100)

#Label Scale Wert
Loadlabel = tk.Label(frame1,text=str(Loadscale.get()))
Loadlabel.place(x=b/7-40, y=410)


### Äquidistante Knoten

p0 = tk.Button(frame1)
p0.place(x=100, y=30)
p0.config(width=30,height=2,text='Äquidistante Knoten',command = lambda :Butcolor())





########### Tab 2 FourierInterpolation
frame2 = tk.Frame(notebook, width=100, height=200)

notebook.add(frame1, text="Polynominterpolation" )
notebook.add(frame2, text="frame 2" )

notebook.grid(row=0, column=0, sticky="nw")




    
    





root.mainloop()