import numpy as np
import matplotlib.pyplot as plt


g = 9.8  # percepatan gravitasi (m/s^2)
h0 = 10   # tinggi awal (m)
v0 = 0   # kecepatan awal (m/s)

# Hitung waktu untuk benda mencapai tanah
t_max = np.sqrt(2 * h0 / g)
print("Waktu benda mencapai tanah =", t_max, "s")

t = np.linspace(0, t_max, 1000)

# Menghitung kecepatan sebagai fungsi waktu
vt = g * t

# Menghitung posisi (tinggi) sebagai fungsi waktu
h = h0 - 0.5 * g * t**2

# Plotting kecepatan sebagai fungsi waktu
fig, ax1 = plt.subplots()
ax1.plot(t, vt, label="Kecepatan (m/s)")
ax1.set(xlabel='Waktu (s)', ylabel='Kecepatan (m/s)', title='Grafik Kecepatan terhadap Waktu')
ax1.grid()

# Plotting posisi (tinggi) sebagai fungsi waktu
fig, ax2 = plt.subplots()
ax2.plot(t, h, label="Tinggi (m)")
ax2.set(xlabel='Waktu (s)', ylabel='Tinggi (m)', title='Grafik posisi terhadap Waktu')
ax2.grid()

plt.show()
