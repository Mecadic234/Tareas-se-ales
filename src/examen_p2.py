import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def ejecutar_examen_p2():

    fs = 256          
    T = 6              
    N = int(T * fs)    
    t = np.arange(N) / fs   

    f1, f2 = 8, 20    
     
    x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

    
    ruido = 0.3 * np.random.randn(N)
    x_ruido = x + ruido

    
    X = np.fft.fft(x)
    X_ruido = np.fft.fft(x_ruido)

    freqs = np.fft.fftfreq(N, d=1/fs)
     
    X_mag = np.abs(X)[:N//2]/N
    Xr_mag = np.abs(X_ruido)[:N//2]/N
    f_pos = freqs[:N//2]

     
    continuous_plotter(t, x, titulo="Señal original (limpia)")
    continuous_plotter(t, x_ruido, titulo="Señal con ruido")

   
    discrete_plotter(f_pos, X_mag, titulo="DFT de señal original")
    discrete_plotter(f_pos, Xr_mag, titulo="DFT de señal con ruido")
    
    
    delta_f = fs / N
    print(f"Resolución en frecuencia: Δf = {delta_f:.3f} Hz")
