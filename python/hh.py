""""
Filename: action_potential.py    
Description: Creates a plot of the action potential by using 
solutions to the potassium, sodium and leakage conductances.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter


def AlphaM(Vm):
    return 0.1 * (25-(Vm+65)) / (np.exp((25-(Vm+65))/10)-1)

def BetaM(Vm):
    return 4.0 * np.exp(-(Vm+65)/18)

def AlphaH(Vm):
    return 0.07 * np.exp(-(Vm+65)/20)

def BetaH(Vm):
    return 1.0 / (np.exp((30-(Vm+65))/10)+1)

def AlphaN(Vm):
    return 0.01 * (10-(Vm+65)) / (np.exp((10-(Vm+65))/10)-1)

def BetaN(Vm):
    return 0.125 * np.exp(-((Vm+65)+65)/80)

def voltage():
    gbarNa = 120.0  
    gbarK = 36.0  
    gl = 0.3  

    Vna = 50.0  
    Vk = -77.0  
    Vm = -65.0  

    Cm =  1 

    Vrest = Vm


    EndTime = 15 
    TimeStep = .03
    EndStep = EndTime/TimeStep
    Minf = AlphaM(Vm)/(AlphaM(Vm) + BetaM(Vm))
    Hinf = AlphaH(Vm)/(AlphaH(Vm) + BetaH(Vm))
    Ninf = AlphaN(Vm)/(AlphaN(Vm) + BetaN(Vm))

    TauM = 1/(AlphaM(Vm) + BetaM(Vm))
    TauH = 1/(AlphaH(Vm) + BetaH(Vm))
    TauN = 1/(AlphaN(Vm) + BetaN(Vm))

    m = 0.0
    n = 0.0
    h = 1.0

    lstVm = []
    lstt = []
    for count in range(0,int(EndStep)):
        t = count * TimeStep

        m += TimeStep * (AlphaM(Vm) * (1.0 - m) - BetaM(Vm) * m)
        n += TimeStep * (AlphaN(Vm) * (1.0 - n) - BetaN(Vm) * n)
        h += TimeStep * (AlphaH(Vm) * (1.0 - h) - BetaH(Vm) * h)
        
        Itotal = (gl * (Vm-Vrest)) + (gbarK * n**4 * (Vm - Vk)) + (gbarNa * m**3 * h * (Vm - Vna))
        Vm += TimeStep / Cm * (-Itotal)
        
        lstVm.append(float(Vm))
        lstt.append(t)
    return lstVm, lstt

lstVm, lstt = voltage()

print(len(lstVm))


num_frames = 100
indices = np.linspace(0, len(lstVm) - 1, num_frames, dtype=int)
lstVm_resampled = [lstVm[i] for i in indices]
lstt_resampled = [lstt[i] for i in indices]

lstvm = lstVm_resampled
lst = lstt_resampled



fig, ax = plt.subplots()
ax.set_xlim(0, 15)
ax.set_ylim(-80, 50)  # Adjust the y-limits for clarity
line, = ax.plot([], [], lw=2, color='#458588')

for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False)
ax.set_xticks([]) 
ax.set_yticks([])  

fig.patch.set_alpha(0)  # Make the figure background transparent
ax.patch.set_alpha(0)  

def init():
    line.set_data([], [])
    return line,


def update(frame):
    line.set_data(lst[:frame], lstvm[:frame])
    return line,


ani = FuncAnimation(fig, update, frames=len(lstvm), init_func=init, blit=True, interval=50)

plt.show()
writer = PillowWriter(fps=50)
ani.save('C:/Users/ziskk/projects/paco/images/hh.gif', writer=writer, dpi=100, savefig_kwargs={'transparent': True})

