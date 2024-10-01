import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter


np.random.seed(10)

def GBM(mu, sigma, T, s0):
    t = np.linspace(0, T, 100) 
    step = T / len(t)  
    stock_prices = [s0]  
    stock = s0  
    for i in range(1, len(t)):
        z = np.random.normal(0, 1) 
        stock = stock * np.exp((mu - 0.5 * sigma**2) * step + sigma * np.sqrt(step) * z)
        stock_prices.append(stock)

    return t, stock_prices


mu = 0.1  
sigma = 0.2  
T = 1  
s0 = 100  

t, stock_prices = GBM(mu, sigma, T, s0)

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(0, T)
ax.set_ylim(min(stock_prices) * 0.9, max(stock_prices) * 1.1)  # Adjust the y-limits for clarity
line, = ax.plot([], [], lw=2, color='#cc241d')


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
ani.save('C:/Users/ziskk/projects/paco/images/gbm.gif', writer=writer,dpi=300, savefig_kwargs={'transparent': True})
