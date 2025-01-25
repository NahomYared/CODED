# Importerar numpy-biblioteket och namnger det 'np' för enkel åtkomst.

import numpy as np



# Importerar 'stats'-modulen från scipy-biblioteket för statistiska beräkningar.

from scipy import stats



# Importerar 'pyplot'-modulen från matplotlib-biblioteket och namnger det 'plt' för att rita diagram.

import matplotlib.pyplot as plt



# Importerar ett anpassat bibliotek eller verktyg, namnet 'tools' specificerar inte vad det innehåller.

import tools


# Definierar parametrar för simuleringen.

n = 25          # Antal observationer per konfidensintervall.

mu = 2          # Det sanna värdet (medelvärdet) för den normalfördelade populationen.

sigma = 1       # Standardavvikelsen för den normalfördelade populationen.

alpha = 0.05    # 1 minus konfidensnivån (här 95% konfidensnivå).

m = 100         # Antal konfidensintervall som ska simuleras.



# Genererar 'm' st set med 'n' normalfördelade slumpmässiga variabler för varje set.

x = stats.norm.rvs(loc=mu, scale=sigma, size=(m, n))



# Beräknar medelvärdet av varje set av observationer.

xbar = np.mean(x, axis=-1) #Varje medelvärde för varje individuella konfidensintervall



# Beräknar kritiska värden och standardfel.

lambda_alpha_2 = stats.norm.ppf(1 - alpha / 2)

D = sigma / np.sqrt(n)



# Beräknar nedre och övre gränser för varje konfidensintervall.

undre = xbar - lambda_alpha_2 * D

övre = xbar + lambda_alpha_2 * D



# Skapar en figur för visualisering med specifika dimensioner.

plt.figure(figsize=(4, 8))



# Ritar upp varje konfidensintervall och färgkodar de som inte innehåller det sanna värdet 'mu'.

for k in range(m):

    color = 'r' if övre[k] < mu or undre[k] > mu else 'b'

    plt.plot([undre[k], övre[k]], [k, k], color)



# Justerar axlarnas gränser för att förbättra diagrammets utseende.

b_min = np.min(undre)

b_max = np.max(övre)

plt.axis([b_min, b_max, -1, m])



# Ritar ut en linje som representerar det sanna värdet 'mu'.

plt.plot([mu, mu], [-1, m], 'g')



# Räknar och skriver ut antalet intervall som inte innehåller 'mu'.

antal_roda_streck = np.sum((övre < mu) | (undre > mu))

print(f"Antal röda streck: {antal_roda_streck}")



# Visar plotten.

plt.show()





# Här följer en serie frågor och svar som baseras på koden och dess output.



# Frågor

#1.Hur många av dessa intervall kan förväntas innehålla det sanna värdet på μ?

#2.Vad visar de horisontella strecken och det vertikala strecket?

#3.Hur många av de 100 intervallen innehåller det sanna värdet på μ?

#4.Stämmer resultatet med dina förväntningar?

#5.Variera nu μ, σ, n och α (en i taget) och ser hur de olika parametrarna påverkar resultatet.



#Svar:

#1. 95 stycken ty med 95% säkerhet är paramtern i intervallet.

#2. Det stående visar MU, det liggande är individuella KI, röd om parametern inte ligger i intervallet.

#3. m minus antalet röda intervall.

#4. Beror lite på den enskilda simuleringen, Större M gör att den blir mer träffsäker mot mina förväntningar.

#5.