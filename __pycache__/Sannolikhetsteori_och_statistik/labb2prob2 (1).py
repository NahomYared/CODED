import numpy as np
import matplotlib.pyplot as plt

# Parameters for the two distributions
theta_H0 = 1  # Parameter under H0
theta_H1 = 5  # Parameter under H1

# Define the range for X values
x = np.linspace(0, 1, 1000)

# Calculate the PDF for exponential distributions under H0 and H1
pdf_H0 = theta_H0 * np.exp(-theta_H0 * x)
pdf_H1 = theta_H1 * np.exp(-theta_H1 * x)

# Threshold for rejecting H0
threshold = 0.05

# Plot the distributions
plt.figure(figsize=(12, 8))
plt.plot(x, pdf_H0, label='H0: θ=1 (Exponential)', color='blue', linewidth=2)
plt.plot(x, pdf_H1, label='H1: θ=5 (Exponential)', color='orange', linewidth=2)

# Highlight the regions of interest
plt.fill_between(x, pdf_H1, 0, where=(x < threshold), color='orange', alpha=0.3, label='Styrka (1-β)')
plt.fill_between(x, pdf_H1, 0, where=(x >= threshold), color='green', alpha=0.3, label='Typ II-fel (β)')
plt.fill_between(x, pdf_H0, 0, where=(x < threshold), color='blue', alpha=0.3, label='Typ I-fel (α)')

# Add threshold line
plt.axvline(threshold, color='red', linestyle='--', label='Threshold: X = 0.05')

# Add labels, legend, and grid
plt.title("Visualisering av Styrka, Typ I-fel och Typ II-fel", fontsize=16)
plt.xlabel("X (Observationsvärde)", fontsize=14)
plt.ylabel("Sannolikhetstäthet", fontsize=14)
plt.legend(fontsize=12)
plt.grid(alpha=0.5)
plt.show()
