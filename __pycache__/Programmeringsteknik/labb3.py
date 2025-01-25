
#Importing module "modul_till_labb3"

import modul_till_labb3
#Defines the functions for geometric and arithmetic number sequences

def beräkna_aritmetisk_summa(a1, d, n):
    sa = n*(a1 + (a1 + d*(n-1)))//2
    return sa

def beräkna_geometrisk_summa(g1, q, n):
    sg = g1*((g1*q**(n-1)-1))//(q-1)
    return sg

def main():
#asking user to enter values for calculating arithmetic and geometric sum
#Using imported module to verify input tupe for all inputs
    print("Skriv in värden för den aritmetiska summan nedan: ")
strartvalue_a = modul_till_labb3.float_control("Ange startvärdet a1: ")
difference = modul_till_labb3.float_control("Ange differensen d: ")

print()

print("Skriv in värden för den geometriska summan nedan: ")
startvalue_b = modul_till_labb3.float_control("Ange startvärdet g1: ")
quota = modul_till_labb3.float_control("Ange kvoten q: ")

while quota == 1:
    print("Division med noll, pröva ett annat värde")

quota = modul_till_labb3.float_control("Ange kvoten q: ")
#asks user to reinput "q" in the geometric sum function if q = 1. (division by zero)

print()

print ("Skriv in den gemensamma element för den aritmetiska och geometriska summan nedan: ")

element = modul_till_labb3.int_control("ange element i följden n: ")
#asking user to enter the mutual elemnts for both artithmetic and geometric sums.

while element <= 0:
    print("Du måste ha minst ett element, pröva igen.")
element = modul_till_labb3.int_control("ange element i följden n: ")

print()

#Calling on functions
#Catching overflowerror
try:
    Summaaritmetisk = beräkna_aritmetisk_summa(strartvalue_a, difference, element) 
    print(f"den aritmetiska summan är:", str(Summaaritmetisk))
    
    summageometrisk = beräkna_geometrisk_summa(startvalue_b, quota, element)
    print(f"den geometriska summan är:", str(summageometrisk))
    
    if(summageometrisk>Summaaritmetisk):
        print(f"Den geometriska summan är störst")
    elif(Summaaritmetisk>summageometrisk):
        print(f"Den aritmetiska summan är störst")
    else:
        print(f"Summorna är lika")
except OverflowError:
    print("Du har för stora tal, starta om programmet!")
    exit(0)
main()
