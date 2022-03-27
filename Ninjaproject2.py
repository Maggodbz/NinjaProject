# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:27:01 2020

@author: marco
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import tkinter as tk
import numpy as np
from numpy import sin,cos,exp,sqrt,sinh,cosh,pi,tan,log,arccos
import time
import threading
from tkinter import ttk

root = tk.Tk()
root.geometry('1100x500')
root.title('Approximation is fun')
root.config(bg='#212946')






#Cyperpunk Theme
plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey

        




#Entry Button
e = tk.Entry(root)
e.place(x=50,y=100,width=350,height=30)

miss=tk.Label(root)
miss.configure(bg='#212946')

#Intervallgrenzen
a = -10
b = 10

def f(x):
    x = x
    return eval(e.get())

def Tf(x):
    x=1/2*(b-a)*x+1/2*(b+a)
    return eval(e.get())





#Plot Button

p1 = tk.Button(root,text='Plot',command=lambda :Plot())
p1.configure(bg='#F69602')
p1.place(x=410,y=90,width=130,height=50) 





                
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=550,y=0,width=550,heigh=525)
         
def Plot():
    n = 1000
    knots=np.linspace(-1,1,n)
    
    if len(e.get())==0:
        miss.configure(text='NO FUNCTiON FOUND',fg='#F69602')
        miss.place(x=50,y=70)    
    else:
        miss.configure(fg='#212946')
        fig.clf()
        ax = fig.add_subplot(111)
        ax.plot(knots,[Tf(x) for x in knots],'#F69602')
        fig.canvas.draw()




###Buttons general




#Loadbarfunktion

#Schieberegler für Loadbar
b2 = tk.Scale(root,from_=1,to=100, orient='horizontal',showvalue='0',command= lambda x: load(b2.get()))
b2.config(bg ='#212946',troughcolor='#212946')
b2.place(x=230,y=230,width=170)


#Knotenanzeige
b3 = tk.Label(root,text=str(b2.get()),bg='#212946',fg='#F69602')
b3.place(x=405,y=230,width=20,heigh=20)


L = 100
fig1 = plt.Figure()
fig1.clf()
maxload = range(1,L+1)
ax = fig1.add_subplot(111)
ax.set_ylim([0,L])

#color of the loading bar
col=[]
col.append('#F69602')
for i in range(1,L):
    col.append('#212945')
ax.bar(maxload,maxload,color=col,edgecolor='#F69602')
ax.axis('off')

canvas = FigureCanvasTkAgg(fig1, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=230,y=130,width=170,height=100)
    
    
def load(n):
    global L,maxload,col
    for i in range(L):
        if i <= n-1:
            col[i]='#F69602'
        else:
            col[i]='#212946'
    ax.bar(maxload,maxload,color=col)
    fig1.canvas.draw()
    b3.configure(text=str(b2.get()))   


    
    
    
#Buttons_Approximation



r = 0
def apu1():
    global r,b3
    if r == 0:
        r +=1
        ap1.config(bg='#F69602')
    else:
        r = 0
        ap1.config(bg='white')

ap1 = tk.Button(root,text='NewtonInterpolation',command= lambda: apu1())
ap1.place(x=20,y=250,width=200,height=50)



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



#Expand Figure
def expand_():
    if root.winfo_height()>550:
        app.configure(text='Approximation')
        for i in range(1,100):
            time.sleep(1/100)
            width=1700-6*i
            height=800-3*i
            root.geometry(str(width)+'x'+str(height))
    else:
        app.configure(text='Close Approximation')
        for i in range(1,100):
            time.sleep(1/100)
            width=1100+6*i
            height=500+3*i
            root.geometry(str(width)+'x'+str(height))


app = tk.Button(root,text='Approximation',command = lambda:AppPlot())
app.place(x=450,y=400) 

applabel = tk.Label(root)
applabel.configure(bg='#212946')
applabel.place(x=200,y=400)


#Plot Approximationsfunktion (upper right corner)
fig2 = plt.Figure()
canvas = FigureCanvasTkAgg(fig2, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=1110,y=25,width=530,heigh=500)

#Plot Error  (lower middle)
fig3 = plt.Figure()
canvas = FigureCanvasTkAgg(fig3, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=500,y=500,width=400,heigh=150)

#Plot Error (upper middle)
fig6 = plt.Figure()
canvas = FigureCanvasTkAgg(fig6, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=500,y=650,width=400,heigh=150)


#Plot all Knots < n  (lower left corner)
fig4 = plt.Figure()
canvas = FigureCanvasTkAgg(fig4, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=0,y=500,width=400,heigh=300)

#Plot Knots on Unit Circle
fig5 = plt.Figure()
canvas = FigureCanvasTkAgg(fig5,master=root)
canvas.get_tk_widget().place(x=1100,y=500,width=400,heigh=300)


def AppPlot():
    global r
    #If entry is empty
    if len(e.get())==0:
        miss.configure(text='NO FUNCTiON FOUND',fg='#F69602')
        miss.place(x=50,y=70)
    else:
        if r==1:
            applabel.configure(fg='#212946')
            miss.configure(fg='#212946')
            #No idea what the fuck threading is doing, somethingn with sleep and for loop
            t1 = threading.Thread(target=expand_)  
            t1.start()
            #Close Approximation
            if root.winfo_height()>550:
                return
            else:
                #Plot fig2-5 if Approximation Method is choosen and Entry is none Empty
                fig2.clf()
                fig3.clf()
                fig4.clf()
                fig5.clf()
                
                n = 1000
                knots=np.linspace(-1,1,n)
                
                #fig2
                approxim=[Newton1(x,b2.get()) for x in knots]
                ax1 = fig2.add_subplot(111)
                ax1.plot(knots,approxim)
                fig2.canvas.draw()
                ax2 = fig3.add_subplot(111)
                
                #fig3
                Error = []
                for i in range(n):
                    Error.append(abs(approxim[i]-Tf(knots[i])))
                maxError = max(Error)
                xpos= Error.index(maxError)
                xmax=knots[xpos]
                ax2.annotate('Max '+str(maxError),xy=(xmax,maxError))
                ax2.plot(knots,Error)
                fig3.canvas.draw()
                
                #fig6 und fig 6
                Errorverlauf = []
                ax6 = fig6.add_subplot(111)
                ax4 = fig4.add_subplot(111)
                for i in range(1,b2.get()):
                    multiapproxim=[Newton1(x,i) for x in knots]
                    ax4.plot(knots,multiapproxim)
                    fig4.canvas.draw()
                    multiError = []
                    
                    for j in range(n):
                        multiError.append(abs(multiapproxim[j]-Tf(knots[j])))
                    multimaxError = max(multiError)
                    Errorverlauf.append(multimaxError)
                ax6.plot(range(1,b2.get()),Errorverlauf,'ro')
                fig6.canvas.draw()
                
                
                
                #fig 5
                fig5
                ax5 = fig5.add_subplot(111,projection='polar')
                unitx = np.linspace(-1,1,b2.get())
                anglex = [arccos(x) for x in unitx]
                rad = np.zeros(len(unitx))
                for i in range(len(unitx)):
                    rad[i]=1
                ax5.plot(anglex,rad,'ro')
                fig5.canvas.draw()
                
                
                
                    
        else:
            if root.winfo_height()>550:
                expand_()
                fig2.clf()
                fig3.clf()
                fig4.clf()
            else:
                applabel.configure(text='Choose Approximation Method',fg='#F69602')
                
            
root.mainloop()