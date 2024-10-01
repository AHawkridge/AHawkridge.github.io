import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
np.random.seed(8)
def GBM_MJD(mu,sigma,T,s0,lambda_jump,mu_jump,sigma_jump):
    t= np.linspace(0,T,100)
    step=T/len(t)
    stock = s0
    s=[s0]
    #m = lambda_jump * (np.exp(mu_jump + (sigma_jump**2) / 2) - 1) 
    m = -lambda_jump * sigma_jump
    for i in range(len(t)-1):
        #sign = np.random.choice([-1,1])
        z = np.random.normal(0, 1)  
        y = np.random.normal(mu_jump, sigma_jump)  
        Nt = np.random.poisson(lambda_jump * step) 
        stock = stock * np.exp((mu - 0.5 * sigma**2 - m) * step + sigma * np.sqrt(step) * z) * np.exp(Nt * y)
        s.append(stock)
    
    return s




T = 1
t= np.linspace(0,T,100)

s0 = 350
r = 0.1 
mu=r

lambda_jump = 1 
mu_jump = 0.  
sigma_jump = 0.3  
sigma=0.3
Q = np.array([[-2, 2], [4, -4]])
stock_prices = GBM_MJD(mu,sigma,T,s0,lambda_jump,mu_jump,sigma_jump)

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
ani.save('C:/Users/ziskk/projects/paco/images/mjd.gif', writer=writer,dpi=100, savefig_kwargs={'transparent': True})
