# def recursion_power(x,y):
#     if y==0:
#         return 1
#     return x*recursion_power(x,y-1) #5*recursion(2,4),
#
#
# x=int(input())
# y=int(input())

# Zad1) Da se napise rekurzija, koja kje presmetuva zbir od lista = [10, 20, 30, 40, 50]


# Zad2) Da se napise rekurzija, koja kje pronaogja site fibonaci broevi do N (N moze da e bilo koj int)


# Zad3) Da se napise rekurzija, koja kje presmetuva suma od fibonaci broevi do N (N moze da e bilo koj int)


# Zad4) Da se napise rekurzija, koja kje ja presmeta sumata od cifrite na eden pozitiven broj


# Zad5) nCr = n! / r! (n-r)!
# def niza_fibonaci(n):
#     if n in {0,1}:
#         return n
#     return niza_fibonaci(n - 1) + niza_fibonaci(n - 2)
# lista=[]
# def clenovi(n):
#     if n>1:
#         return lista.append(niza_fibonaci(n - 1) + niza_fibonaci(n - 2))
#     return 1
#
#
# n=int(input())
# print(niza_fibonaci(n))
# print(lista)
#
# def fibonacci_of(n):
#      if n in {0, 1}:  # Base case
#          return n
#      return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
# [fibonacci_of(k) for k in range(n)]
# print(fibonacci_of(k))
n=int(input())

def niza_fibonaci(n):
    if n in {0,1}:
        return n
    return niza_fibonaci(n - 1) + niza_fibonaci(n - 2)
lista=[]
for i in range(n):
    lista.append(niza_fibonaci(i))

print(lista)