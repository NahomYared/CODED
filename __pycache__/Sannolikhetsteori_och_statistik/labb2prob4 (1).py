import numpy as np

from scipy import stats

import matplotlib.pyplot as plt

import os

## lägg till np.shape/ %whos

# kika på vad boxplotsen betyder



# Problem 4: Fördelningar av givna data

# Ladda datafilen.

birth = np.loadtxt('birth.dat')

# Definiera filter beroende på om modern röker (kolonn 20

# är 3) eller inte (kolonn 20 är 1 eller 2). Notera att

# eftersom indexering i Python börjar med noll så betecknas

# kolonn 20 med indexet 19.

non_smokers = (birth[:, 19] < 3) 

smokers = (birth[:, 19] == 3)

# Extrahera födelsevikten (kolonn 3) för de två kategorierna.

x = birth[non_smokers, 2] 

y = birth[smokers, 2]

längdx=np.shape(x)

längdy=np.shape(y)



print(f"dimension X:  {längdx}")

print(f"dimension Y:  {längdy}")



sober = (birth[:, 25] < 2)

Alcoholics = (birth[:, 25] == 2)

# Extrahera födelsevikten (kolonn 3) för de två kategorierna.

z = birth[sober, 2]

w = birth[Alcoholics, 2]

z[~np.isnan(z)]

# Skapa en stor figur.



längdz=np.shape(z)

längdw=np.shape(w)



print(f"dimension Z:  {längdz}")

print(f"dimension W:  {längdw}")


plt.figure(figsize=(12, 8))


# Plotta ett låddiagram över x.

plt.subplot(2, 2, 1)

plt.boxplot(x)

plt.axis([0, 2, 500, 5000])

plt.title('Boxplot för icke-rökare')



# Plotta ett låddiagram över x.

plt.subplot(2, 2, 2)

plt.boxplot(z)

plt.axis([0, 2, 500, 5000])

plt.title('Boxplot för nykterister')





# Plotta ett låddiagram över y.

plt.subplot(2, 2, 3)

plt.boxplot(y)

plt.axis([0, 2, 500, 5000])

plt.title('Boxplot för rökare')



# Plotta ett låddiagram över y.

plt.subplot(2, 2, 4)

plt.boxplot(w)

plt.axis([0, 2, 500, 5000])

plt.title('Boxplot för alkoholister')



# Beräkna kärnestimator för x och y. Funktionen

# gaussian_kde returnerar ett funktionsobjekt som sedan

# kan evalueras i godtyckliga punkter.

kde_x = stats.gaussian_kde(x)

kde_y = stats.gaussian_kde(y)

kde_z = stats.gaussian_kde(z)

kde_w = stats.gaussian_kde(w)



# Skapa ett rutnät för vikterna som vi kan använda för att

# beräkna kärnestimatorernas värden.

min_val = np.min(birth[:, 2])

max_val = np.max(birth[:, 2])

grid = np.linspace(min_val, max_val, 60)



# Plotta kärnestimatorerna.

#plt.subplot(2, 2, (5, 6))



# Plotta kärnestimatorerna.

plt.figure(figsize=(8, 6))

plt.plot(grid, kde_x(grid), 'b', label='Icke-rökare')

plt.plot(grid, kde_y(grid), 'r', label='Rökare')

plt.plot(grid, kde_z(grid), 'g', label='nykterist')

plt.plot(grid, kde_w(grid), 'y', label='alkoholist')

plt.legend()

plt.title('Kärnestimatorer för födelsevikt')

plt.suptitle('Fördelning av födelsevikt beroende på rökning')







# Extrahera data för födelsevikt, moderns ålder, moderns längd och moderns vikt.

birth_weight = birth[:, 2]

mother_age = birth[:, 3]

mother_height = birth[:, 15]

mother_weight = birth[:, 14]



# Skapa en figur med fyra subplots för varje histogram.

fig, axs = plt.subplots(2, 2, figsize=(12, 8))



# Histogram för födelsevikt.

axs[0, 0].hist(birth_weight, bins=20, color='blue', alpha=0.7)

axs[0, 0].set_title('Fördelning av födelsevikt')

axs[0, 0].set_xlabel('Födelsevikt')

axs[0, 0].set_ylabel('Antal födslar')



# Histogram för moderns ålder.

axs[0, 1].hist(mother_age, bins=20, color='green', alpha=0.7)

axs[0, 1].set_title('Fördelning av moderns ålder')

axs[0, 1].set_xlabel('Ålder')

axs[0, 1].set_ylabel('Antal födslar')



# Histogram för moderns längd.

axs[1, 0].hist(mother_height, bins=20, color='orange', alpha=0.7)

axs[1, 0].set_title('Fördelning av moderns längd')

axs[1, 0].set_xlabel('Längd')

axs[1, 0].set_ylabel('Antal födslar')



# Histogram för moderns vikt.

axs[1, 1].hist(mother_weight, bins=20, color='red', alpha=0.7)

axs[1, 1].set_title('Fördelning av moderns vikt')

axs[1, 1].set_xlabel('Vikt')

axs[1, 1].set_ylabel('Antal födslar')



# Justera layouten för att undvika överlappande subplots.

plt.tight_layout()



# Visa figuren.

plt.show()







'''Använd informationen i birth.txt och funktionen plt.hist 

för att generera en figur med fyra olika histogram som visar 

fördningarna för barnets födelsevikt, moderns ålder, moderns längd 

respektive moderns vikt.'''



'''Välj nu ut en annan av de kategoriska variablerna i datat som du misstänker 

kan påverka födelsevikten och undersök med samma metod om det 

förefaller föreligga ett samband mellan variabeln och födelsevikten. '''