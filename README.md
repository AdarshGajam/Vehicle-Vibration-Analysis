# Vehicle-Vibration-Analysis
Python-based project to analyze vehicle accelerometer data using FFT for frequency and amplitude detection.
Vehicle Vibration Data Analysis
Overview
This Python-based project simulates vehicle accelerometer data analysis to detect mechanical issues by calculating vibration frequency and amplitude using Fast Fourier Transform (FFT). It demonstrates skills in signal processing, Python programming (Pandas, NumPy, Matplotlib), and data visualization, relevant to automotive engineering and quality testing.
Features

Simulates accelerometer data with a 5 Hz vibration and noise.
Applies FFT to identify dominant frequency and amplitude.
Generates visualizations (time-domain and frequency-domain plots).
Saves results to a CSV file for reporting.

Prerequisites

Python 3.7+
Libraries: pandas, numpy, matplotlib (install via pip install -r requirements.txt)

Installation

Clone the repository:git clone https://github.com/adarshgajam/Vehicle-Vibration-Analysis.git


Install dependencies:pip install -r requirements.txt


Run the script:python Vehicle_Vibration_Analysis.py



Outputs

vibration_results.csv: Contains dominant frequency (5 Hz) and amplitude (0.25).
vibration_plot.png: Time-domain plot of acceleration vs. time.
frequency_spectrum.png: Frequency-domain plot showing amplitude vs. frequency.

How It Works

Data Simulation: Generates a 10-second dataset with a 5 Hz sinusoidal vibration and random noise.
FFT Analysis: Uses NumPy’s FFT to compute the frequency spectrum, identifying the dominant frequency.
Visualization: Creates plots with Matplotlib to visualize raw data and frequency spectrum.
Results: Saves key metrics (frequency, amplitude) to a CSV file.

Applications

Detects mechanical issues (e.g., wheel imbalance, engine faults) in automotive systems.
Applicable to quality testing, mechatronics, and sensor-based diagnostics.

Future Improvements

Integrate real accelerometer data from sensors.
Add machine learning (e.g., PyTorch) for predictive maintenance.
Enhance visualization with interactive plots (e.g., Plotly).

Author
Adarsh Gajam  

Master’s student in Analytical Instruments, Hochschule Coburg  
LinkedIn: linkedin.com/in/adarshgajam  
Email: adarshgajam@gmail.com

License
MIT License
