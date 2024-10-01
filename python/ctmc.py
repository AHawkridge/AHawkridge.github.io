import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
np.random.seed(0)
def GBM_WS(mu,sigmas,T,s0,Q):
    t = np.linspace(0, T, 100) 
    step = T/len(t)
    stock = s0
    states = list(range(len(Q)))
    current = np.random.choice(states,p=[1,0]) 
    sigma = sigmas[current]
    z = np.random.exponential(1 / abs(Q[current][current]))
    length = 0
    sigs=[sigmas[current]]
    s=[s0]
    for i in range(len(t)):
        length += step*3
        if length >= z:
            length = 0
            p = Q[current] / abs(Q[current][current]) 
            probs = [pr if pr >= 0 else 0 for pr in p]
            current = np.random.choice(states, p=probs)
            sigma = sigmas[current]
            z = np.random.exponential(1 / abs(Q[current][current]))
        eta = np.random.normal(0, 1)
        stock = stock * np.exp((mu- 0.5 * sigma**2)*step + sigma*np.sqrt(step)*eta)
        s.append(stock)
        sigs.append(sigma)
    return s , sigs




T = 1
t= np.linspace(0,T,100)

s0 = 350
r = 0.1 
mu=r
Q = np.array([[-2, 2], [4, -4]])

sigmas=[0.1,1]


stock_prices , sigs = GBM_WS(mu,sigmas,T,s0,Q)

fig, ax = plt.subplots()
ax.set_xlim(0, T)
ax.set_ylim(min(stock_prices) * 0.9, max(stock_prices) * 1.1)  # Adjust the y-limits for clarity
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
    line.set_data(t[:frame], stock_prices[:frame])
    return line,


ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=50)

plt.show()
writer = PillowWriter(fps=20)
ani.save('C:/Users/ziskk/projects/paco/images/ctmc.gif', writer=writer,dpi=100, savefig_kwargs={'transparent': True})

#################################################################################################

def update_sig(frame):
    line.set_data(t[:frame], sigs[:frame])
    return line,



fig, ax = plt.subplots()
ax.set_xlim(0, T)
ax.set_ylim(min(sigs) * 0.9, max(sigs) * 1.1)  # Adjust the y-limits for clarity
line, = ax.step([], [], lw=2, color='#689d6a')

for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False)
ax.set_xticks([]) 
ax.set_yticks([])  

fig.patch.set_alpha(0)  # Make the figure background transparent
ax.patch.set_alpha(0)  


sig_ani = FuncAnimation(fig, update_sig, frames=len(t), init_func=init, blit=True, interval=50)

plt.show()
writer = PillowWriter(fps=20)
sig_ani.save('C:/Users/ziskk/projects/paco/images/ctmc_sig.gif', writer=writer,dpi=100, savefig_kwargs={'transparent': True})

