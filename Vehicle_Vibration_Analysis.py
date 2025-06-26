import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate vehicle accelerometer data (time, acceleration)
np.random.seed(42)
time = np.linspace(0, 10, 1000)  # 10 seconds, 1000 samples
freq = 5  # Vibration frequency (Hz)
amplitude = 0.5  # Vibration amplitude
noise = np.random.normal(0, 0.1, 1000)  # Add noise
acceleration = amplitude * np.sin(2 * np.pi * freq * time) + noise

# Create DataFrame
data = pd.DataFrame({'Time_s': time, 'Acceleration_m_s2': acceleration})

# Calculate frequency spectrum using FFT
fft_vals = np.fft.fft(data['Acceleration_m_s2'])
fft_freq = np.fft.fftfreq(len(fft_vals), d=time[1]-time[0])
positive_freq = fft_freq[:len(fft_freq)//2]
positive_fft = np.abs(fft_vals[:len(fft_vals)//2])

# Identify dominant frequency and amplitude
dominant_freq = positive_freq[np.argmax(positive_fft)]
dominant_amplitude = np.max(positive_fft) / len(time)

# Save results to CSV for reporting
results = pd.DataFrame({
    'Metric': ['Dominant Frequency (Hz)', 'Dominant Amplitude'],
    'Value': [dominant_freq, dominant_amplitude]
})
results.to_csv('vibration_results.csv', index=False)

# Plot acceleration data
plt.figure(figsize=(10, 6))
plt.plot(data['Time_s'], data['Acceleration_m_s2'], label='Acceleration')
plt.title('Vehicle Vibration Data')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.legend()
plt.grid(True)
plt.savefig('vibration_plot.png')
plt.close()

# Plot frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(positive_freq, positive_fft, label='Frequency Spectrum')
plt.title('Vibration Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('frequency_spectrum.png')
plt.close()