from math import sqrt
n = int(input("Enter n: "))

r = sqrt(5)
nth = (((1+r)/2)**n-((1-r)/2)**n)//r

print(nth)