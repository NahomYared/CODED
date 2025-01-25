import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Ladda datafilen.
birth = np.loadtxt('birth.dat')

# Extrahera data för födelsevikt, moderns ålder, moderns längd och moderns vikt.
birth_weight = birth[:, 2]
mother_age = birth[:, 3]
mother_height = birth[:, 15]
mother_weight = birth[:, 14]

# Undersök normalitet med stats.probplot och plotta resultaten.
def plot_probplot(variable, title):
    # Filtrera ut NaN-värden.
    variable = variable[~np.isnan(variable)]
    
    # Använd stats.probplot för en visuell bedömning.
    _ = stats.probplot(variable, plot=plt)
    
    # Sätt titel och visa plotten.
    plt.title(f'Probability Plot för {title}')
    plt.show()

# Använd plot_probplot för varje variabel.
plot_probplot(birth_weight, 'Födelsevikt')
plot_probplot(mother_age, 'Moderns Ålder')
plot_probplot(mother_height, 'Moderns Längd')
plot_probplot(mother_weight, 'Moderns Vikt')

# Använd stats.jarque_bera för att göra ett statistiskt test av normalitet.
def perform_jarque_bera_test(variable, title):
    # Filtrera ut NaN-värden.
    variable = variable[~np.isnan(variable)]
    
    # Använd stats.jarque_bera för att utföra testet.
    p_value = stats.jarque_bera(variable)[1]
    
    # Skriv ut resultaten.
    #print(f"Jarque-Bera testresultat för {title}:\nJB-värde = {jb_value}\np-värde = {p_value}\n")
    # Check for normality based on the p-value
    #print(p_value)
    if p_value > 0.05:
        print(f" {title} : is normally distributed ")
        print(" ")
    else:
        print(f" {title}  : is not normally distributed")
        print(" ")

# Använd perform_jarque_bera_test för varje variabel.
perform_jarque_bera_test(birth_weight, 'Födelsevikt')
perform_jarque_bera_test(mother_age, 'Moderns Ålder')
perform_jarque_bera_test(mother_height, 'Moderns Längd')
perform_jarque_bera_test(mother_weight, 'Moderns Vikt')