print "hello bobo"

import sys
import Tkinter
import pylab
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import AtomicMassTable
import copy
import math
import matplotlib.pylab as plt
import functools
from mpl_toolkits.mplot3d import Axes3D

def _quit():
    global root
    root.quit()
    root.destroy()

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlim([-0.5,0.5])
ax.set_ylim([-0.5,0.5])
ax.axhline(0, color='black')
ax.axvline(0, color='black')

root  = Tkinter.Tk()
root.minsize(width=1000,height=600)
root.protocol("WM_DELETE_WINDOW",_quit)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().place(relwidth=0.6, relheight=0.9,relx=0.05,rely=0.05)

#fig2 = plt.figure(1)
#ax2 = fig2.add_subplot(111)
#canvas2 = FigureCanvasTkAgg(fig2, master=root)
#canvas2.show()
#canvas2.get_tk_widget().place(relwidth=0.4, relheight=0.3,relx=0.5,rely=0.55)

import Constants
from TrajectoryManager  import TrajectoryManager

initialpos = 0.05

TM = TrajectoryManager()
TM.OpenFile('StartCondition5.json')
TM.CalculateTrajectories()
TM.CreateInterpolation()

print TM.GetPosition(0.05)
pos = TM.GetPosition(0.05)
line = ax.plot( pos[0],pos[1],'o')

TM2 = TrajectoryManager()
TM2.OpenFile('StartCondition4.json')
TM2.CalculateTrajectories()
TM2.CreateInterpolation()

print TM2.GetPosition(0.05)
pos2 = TM2.GetPosition(0.05)
line2 = ax.plot( pos2[0],pos2[1],'o')

#TM3 = TrajectoryManager()
#TM3.OpenFile('StartCondition3.json')
#TM3.CalculateTrajectories()
#TM3.CreateInterpolation()

#print TM3.GetPosition(0.05)
#pos3 = TM3.GetPosition(0.05)
#line3 = ax.plot( pos3[0],pos3[1],'o')

#for OneTr in TM.Trajectories:
#    ax.plot(OneTr[0],OneTr[1],OneTr[2])

H1 =  AtomicMassTable.GetElement(1,1)
H2 =  AtomicMassTable.GetElement(1,2)
He4 =  AtomicMassTable.GetElement(2,4)

MagneticFieldB =2.
K0=90

toolbar = NavigationToolbar2TkAgg( canvas, root )
def ScaleChanged(*args):
    print args
    pos = TM.GetPosition(float(args[0]))
    #pos2 = TM2.GetPosition(float(args[0]))
    #pos3 = TM3.GetPosition(float(args[0]))
    #print "pp:",pos
    line[0].set_data( pos[0],pos[1])
    line2[0].set_data( pos2[0],pos2[1])
    line3[0].set_data( pos3[0],pos3[1])

    canvas.draw()
scale = Tkinter.Scale(root, from_=0, to=0.5, resolution=0.01, command = ScaleChanged, orient = Tkinter.HORIZONTAL)
scale.place(relx = 0.7, rely = 0.3)
scale.set(initialpos)

############# NavigationToolBar #####################
#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
#canvas._tkcanvas.place(relx = 0, rely = 0.95)

Tkinter.mainloop()
