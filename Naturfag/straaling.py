import numpy as np
import matplotlib.pyplot as plt

effekt = 100 #Effekt i W, 1m fra mast
x = np.linspace(1,15) #Lager x verdier fra 1 til 15
y = 1/x**2 * effekt #Regner ut y-verdier

plt.plot(x,y)
plt.xlabel("Avstand fra kilden (m)")
plt.ylabel("Intensitet (W/m^2)")
plt.grid()
plt.show()
