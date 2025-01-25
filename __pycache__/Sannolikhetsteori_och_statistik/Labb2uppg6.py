import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Ladda data från birth.dat
birth = np.loadtxt('birth.dat')

# Filtrera födelsevikter baserat på moderns rökvanor
# Kolumn 19: 1 och 2 = icke-rökare, 3 = rökare
non_smokers = (birth[:, 19] < 3)  # Mask för icke-rökande mammor
smokers = (birth[:, 19] == 3)     # Mask för rökande mammor

# Födelsevikter (kolumn 2) för varje grupp
x = birth[non_smokers, 2]  # Icke-rökare
y = birth[smokers, 2]      # Rökare

# Rensa bort NaN-värden
x = x[~np.isnan(x)]
y = y[~np.isnan(y)]

# Beräkna medelvärden
mean_x = np.mean(x)
mean_y = np.mean(y)

# Beräkna stickprovsvarians
var_x = np.var(x, ddof=1)
var_y = np.var(y, ddof=1)

# Antal observationer
n_x = len(x)
n_y = len(y)

# Standardfel för skillnaden mellan medelvärden
SE = np.sqrt(var_x / n_x + var_y / n_y)

# Kritiskt värde för 95% konfidensgrad
lambda_alpha_2 = norm.ppf(0.975)

# Skattning av skillnaden mellan väntevärden
diff_means = mean_x - mean_y

# Konfidensintervall
lower_bound = diff_means - lambda_alpha_2 * SE
upper_bound = diff_means + lambda_alpha_2 * SE

# Skriv ut resultat
print(f"Skillnad mellan medelvärden: {diff_means:.2f}")
print(f"95% konfidensintervall: [{lower_bound:.2f}, {upper_bound:.2f}]")

# Plotta histogram och konfidensintervall
plt.figure()
plt.hist(x, alpha=0.5, label="Icke-rökare", density=True)
plt.hist(y, alpha=0.5, label="Rökare", density=True)
plt.axvline(diff_means, color='k', linestyle='--', label="Skillnad mellan medelvärden")
plt.axvline(lower_bound, color='g', linestyle='--', label="Konfidensintervall (nedre)")
plt.axvline(upper_bound, color='g', linestyle='--', label="Konfidensintervall (övre)")
plt.legend()
plt.title("Födelsevikter och konfidensintervall")
plt.show()
