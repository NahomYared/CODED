#här gör jag aritmetisk 
def nahom(a1, d, n):
    return a1 + d*(n-1)
  
a1 = 1
d = 2
n = 3

def sum(d, a1, n): 
    return n*(a1 + (a1 + d*(n-1)))//2

print (f"summan av den aritmetiska talföljden är:", int(sum(d, a1, n)))

   
    
#Här gör jag geometrisk
def christian(g1, q, m):
    return g1*q**(m-1)

g1=2
q=2
m=4

def summa(g1, q, m):
    return g1*(q**m-1)/(q-1)

print (f"summan av den geometriska talföljden är:", int (summa(g1, q, m) ))