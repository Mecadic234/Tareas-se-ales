import numpy as np
from scipy.signal import sawtooth, square
from utils.grapher import graficar  

# Parámetros
f = 2             
Ts = 0.05        
t_cont = np.linspace(-1, 5, 1000)  
t_disc = np.arange(-1, 5, Ts)      
n = np.arange(len(t_disc))        

# Señales
x1_c = np.sin(2 * np.pi * f * t_cont)
x1_d = np.sin(2 * np.pi * f * t_disc)

u_c = (t_cont >= 0).astype(int)
u_d = (t_disc >= 0).astype(int)
x2_c = np.exp(-2 * t_cont) * u_c
x2_d = np.exp(-2 * t_disc) * u_d

x3_c = sawtooth(2 * np.pi * f * t_cont, width=0.5)
x3_d = sawtooth(2 * np.pi * f * t_disc, width=0.5)

x4_c = square(2 * np.pi * f * t_cont)
x4_d = square(2 * np.pi * f * t_disc)

#Graficas
graficar(t_cont, t_disc, n, "Señal Senoidal x₁(t) = sin(2π·f·t)", x1_c, x1_d)
graficar(t_cont, t_disc, n, "Señal Exponencial x₂(t) = e^(–2t) · u(t)*", x2_c, x2_d)
graficar(t_cont, t_disc, n, "Señal Triangular x₃(t) = tri(t, f) ", x3_c, x3_d)
graficar(t_cont, t_disc, n, "Señal Cuadrada x₄(t) = sq(t, f)", x4_c, x4_d)

