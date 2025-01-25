#Sätt in värden för variablerna:

print("Först lägger vi in värden för den aritmetiska summan") #Förklaring för vad användaren ska göra
a=int(input("Ge ett värde åt a1: ")) 
b=int(input("Ge ett värde åt d: "))
print("Dags för värdena åt den geometriska summan") #Förklaring för vad användaren ska göra
d=int(input("Ge ett värde åt g1: "))
e=int(input("Ge ett värde åt q: "))
print ("Dags för den gemensamma variabeln som båda summorna behöver till dess formler")
c=int(input("Ge ett värde åt n: "))

#Detta är för aritmetiska summan:

def sum(a1,d,n):
    sa = n*(a1 + (a1 + d*(n-1)))//2
    return sa

summaaritmetisk = sum(a, b, c)
print(f"den aritmetiska summan är:", str(summaaritmetisk))


#Detta är för geometriska summan:
def sum2(g1, q, n):
    sg = g1*((g1*q**(n-1)-1))//(q-1)
    return sg

summageometrisk = sum2(d, e, c) 
#Baserat på vilka tal som som läggs in av användaren i d, e och c så kommmer olika summor från geometriska funktionen komma ut.

print (f"den geometriska summan:", str (summageometrisk))


    
if summageometrisk>summaaritmetisk:
     print ("Den geometriska summan är större än den aritmetiska summan")
elif summaaritmetisk>summageometrisk:
    print("Den aritmetiska summan är större än den geometriska summan")
else: 
    print("De är lika stora")