import numpy as np

from scipy import stats

import matplotlib.pyplot as plt

from scipy.optimize import minimize



# Laddar in data från en fil som heter 'wave_data.dat'.

y = np.loadtxt('wave_data.dat')



# Funktionen för log-likelihood

def neg_log_likelihood(sigma):

    return -np.sum(np.log(y) - 2 * np.log(sigma) - (y**2 / (2 * sigma**2)))



# Använda scipy.optimize.minimize för att hitta det värde på sigma som minimerar neg_log_likelihood

result = minimize(neg_log_likelihood, x0=1) # x0 är startvärdet

est_sigma = result.x[0] # Detta är det uppskattade värdet av sigma



# Skapar en figur för att visualisera två delar: en del av signalen och ett histogram.

plt.figure(figsize=(4, 8))



# Plottar en del av vågsignalen (första 100 datapunkterna).

plt.subplot(2, 1, 1)

plt.plot(y[:100])

plt.title('Del av vågen, första 100 datapunkterna')



# Plottar ett histogram över datan för att visa dess fördelning.

plt.subplot(2, 1, 2)

plt.hist(y, density=True)

plt.title('Fördelningen')



# Visar de skapade plotterna.

plt.show()



# Beräknar nedre och övre gränser för konfidensintervallet med den uppskattade sigma.

alpha = 0.05

lambda_alpha_2 = stats.norm.ppf(1 - alpha / 2)

n = len(y) # Antalet datapunkter

D = est_sigma / np.sqrt(n)

lower_bound = est_sigma - lambda_alpha_2 * D

upper_bound = est_sigma + lambda_alpha_2 * D



# Plottar histogrammet igen och markerar konfidensintervallens gränser.

plt.figure()

plt.hist(y, density=True)

plt.plot(lower_bound, 0.6, 'ro', markersize=2, label='Nedre gräns på KI')

plt.plot(upper_bound, 0.6, 'go', markersize=2, label='Övre gräns på KI')



# Plottar täthetsfunktionen för Rayleighfördelningen med den skattade parametern.

x_grid = np.linspace(np.min(y), np.max(y), 60)

pdf = stats.rayleigh.pdf(x_grid, scale=est_sigma)

plt.plot(x_grid, pdf, 'r')

plt.title('Fördelningen med täthetsfunktion och Konfidensintervall')

plt.show()
