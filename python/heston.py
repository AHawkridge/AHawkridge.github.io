import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
np.random.seed(0)

def Heston(mu,sig0,T,s0,delta,theta,k):
    sigma = sig0
    t= np.linspace(0,T,100)
    step=T/len(t)
    stock = s0
    rho=0.6
    s=[s0]
    sigs=[sig0]
    for i in range(len(t)):
      Z = np.random.multivariate_normal(np.array([0,0]), cov = np.array([[1,rho],[rho,1]]))
      stock = stock * np.exp((mu- 0.5 * sigma**2)*step + sigma*np.sqrt(step)*Z[0])
      sigma = sigma - delta*(sigma - theta)*step +k*np.sqrt(step) *Z[1]
      sigma = np.abs(sigma)
      s.append(stock)
      sigs.append(sigma)

    return s, sigs





T = 1
t= np.linspace(0,T,100)

s0 = 350
r = 0.1 
mu=r

sig0=0.5
T=1

delta =1#the rate it gets to sigma
theta = 0.5 #value it averages around
k=0.5 #volatility of volatility


stock_prices , sigs = Heston(mu,sig0,T,s0,delta,theta,k)

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
ani.save('C:/Users/ziskk/projects/paco/images/heston.gif', writer=writer,dpi=100, savefig_kwargs={'transparent': True})

#################################################################################################

def update_sig(frame):
    line.set_data(t[:frame], sigs[:frame])
    return line,



fig, ax = plt.subplots()
ax.set_xlim(0, T)
ax.set_ylim(min(sigs) * 0.9, max(sigs) * 1.1)  # Adjust the y-limits for clarity
line, = ax.plot([], [], lw=2, color='#689d6a')

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
sig_ani.save('C:/Users/ziskk/projects/paco/images/heston_sig.gif', writer=writer,dpi=100, savefig_kwargs={'transparent': True})