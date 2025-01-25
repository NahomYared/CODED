import numpy as np

from scipy import stats

import tools

import matplotlib.pyplot as plt



#oklart vad som plottas



# Ladda data från moore.dat

moore = np.loadtxt('moore.dat')

x = moore[:, 0]  # Extrahera den första kolumnen (oberoende variabel)

X = np.column_stack((np.ones(len(x)), x))  # Skapa en designmatris X med en kolumn av ettor (för intercept) och x



Y = moore[:, 1]  # Extrahera den andra kolumnen (beroende variabel)

w = np.log(Y)  # Log-transformera den beroende variabeln



# Använd 'tools.regress' för att utföra linjär regression och få ut regressionskoefficienterna

beta_hat = tools.regress(X, w)[0] #beta_hat är båda två



# Beräkna prediktion för år 2025 med hjälp av de beräknade regressionskoefficienterna

prediction = beta_hat[0] + beta_hat[1] * 2025 #x = 2025 i detta fall

print(f'estimat 2025: {prediction}')  # Skriv ut prediktionen för 2025



# Plotta originaldatan och den beräknade linjen

plt.scatter(x, w)  # Scatter plot av den log-transformerade datan

plt.plot(x, X @ beta_hat, color='red')  # Plotta regressionslinjen

plt.xlabel('Oberoende variabel (X)')  # Märk x-axeln

plt.ylabel('Beroende variabel (y)')  # Märk y-axeln


plt.show()  # Visa plotten



## Problem 7: Regression

# Bilda residualerna.

res = X @ beta_hat - w

# Skapa figur.

plt.figure(figsize=(4, 8))

# Plotta kvantil-kvantil-plot för residualerna.

plt.subplot(2, 1, 1)

_ = stats.probplot(res, plot=plt)

# Plotta histogram för residualerna.

plt.subplot(2, 1, 2)

plt.hist(res, density=True)

plt.show()