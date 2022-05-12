from asyncio.windows_events import NULL
from cmath import inf
import math
from random import random
import re
from turtle import pu
from xmlrpc.client import MAXINT
# from pyparsing import line_end
import numpy as np
import random

def plik_na_liste(file):
    lista = []
    with open(file, "r") as file:
        for line in file:
            lista.append(list(map(lambda x: float(x), line.replace("\n", "").split())))
    return lista

def odl_eukalidesowa(list1, list2):
    sum = 0
    for x in range(max(len(list1),len(list2))-1):
        sum += pow(list2[x] - list1[x], 2)
    return pow(sum, 1/2)

def odleglosci(macierz):
    dictonary = {0: [], 1: []}
    for x in range(1,len(macierz),1):
        dictonary[macierz[x][len(macierz[x])-1]].append(odl_eukalidesowa(macierz[0], macierz[x]))
    return dictonary

def mierzymy(x,lista):
    dicto = {}
    for line in lista:
        if (line[len(line)-1] not in dicto.keys()):
            dicto[int(line[len(line)-1])] = [odl_eukalidesowa(x,line)]
        else:
            dicto[int(line[len(line)-1])].append(odl_eukalidesowa(x,line))
    return dicto
    
def mierzymy1(x,lista):
    returnlista = []
    for line in lista:
        returnlista.append((int(line[len(line)-1]),odl_eukalidesowa(x,line)))
    return returnlista

def grupujemy(listaTupli,k):
    dicto = {}
    for record in listaTupli:
        if (record[0] not in dicto.keys()):
            dicto[record[0]] = [record[1]]
        else:
            dicto[record[0]].append(record[1])
    for key in dicto.keys():
        dicto[key].sort()
    for key in dicto.keys():
        sum = 0
        for element in dicto[key][:k]:
            sum = sum + element
        dicto[key] = sum
    return dicto

def decyzja(lista_zgrupowana):
    dec_klucz = MAXINT
    dec_value = MAXINT
    for key in lista_zgrupowana.keys():
        if (lista_zgrupowana[key]<dec_value):
            dec_klucz = key
            dec_value = lista_zgrupowana[key]
        elif (lista_zgrupowana[key]==dec_value):
            return NULL
    return f"decyzja to: {dec_klucz}"
        

macierz = plik_na_liste("australian.dat")
lista_odleglosci = odleglosci(macierz)
# print(lista_odleglosci)

x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# print(mierzymy1(x,macierz))
# print(grupujemy(mierzymy1(x,macierz),20))
# print(decyzja(grupujemy(mierzymy1(x,macierz),20)))
# print(decyzja({0:5,1:5}))

def metryka_euklidesowa2(lista_wspolrzednych):
    sum = 0
    for liczba in lista_wspolrzednych:
        sum = sum + liczba*liczba
    return sum

# print(metryka_euklidesowa2([1,2,3]))

def metryka_euklidesowa3(wektor1,wektor2):
    v1 = np.array(wektor1)
    v2 = np.array(wektor2)
    a = v2-v1
    return pow(np.dot(a,a),1/2)

# print(metryka_euklidesowa3([1,0,0],[1,0,0]))

# usuwamy klasy decyzyjne i dajey randomową klasę decyzyjną
# liczymy wage każdego z punktów do pozostałych (suma)
# sprawdzamy przy dwóch źródłach do którego jest bliżej i zmieniamy mu klase decyzyjną
# porównujemy do australian.dat

# wykład 1:10 28 luty

# -----------------------------------------------
# CALCULATE SQUARE OF NUMBER WITHOUT SQRT FUNCTION
# -----------------------------------------------
def sqrt(wartosc, epsilon):
    a, b = wartosc, 1
    while abs(a-b) > epsilon:
        a, b = (a+b)/2, wartosc/((a+b)/2)
    return a

# -------------
# PRACA DOMOWA
# -------------

def get_from_file(file):
    lista = []
    with open(file, "r") as file:
        for line in file:
            lista.append(list(map(lambda x: float(x), line.replace("\n", "").split())))
    return lista

def change_decisive_class_to_random(lista):
    for value_list in lista:
        value_list[-1] = float(random.randint(0,1))
    return lista

def separate_by_decisive_class(lista):
    ans = {}
    for point in lista:
        if point[-1] not in ans.keys():
            ans[point[-1]] = [point]
        else:
            ans[point[-1]].append(point)
    return ans

def get_central_points(dictionary):
    ans = {}
    sum = 0
    for key in dictionary.keys():
        for x in range(len(dictionary[key])):
            for y in range(len(dictionary[key])):
                sum = sum + metryka_euklidesowa3(dictionary[key][x],dictionary[key][y])
            if key not in ans.keys():
                ans[key] = dictionary[key][x]
            if sum < ans[key][1]:
                ans[key] = dictionary[key][x]
    return ans

def change_decisive_class_based_on_euk_metric(dict_of_central_points,point):
    ans = {}
    for key in dict_of_central_points.keys():
        ans[key] = metryka_euklidesowa3(dict_of_central_points[key],point)
    return min(ans, key=ans.get)

def check_diff(dataset1, dataset2):
    diff = 0
    for x in range(len(dataset1)):
        if (dataset1[x][-1] != dataset2[x][-1]):
            diff += 1
    return str((len(dataset1) - diff)/len(dataset1) * 100) + "%"

def ostateczna():
    goagain= 1
    while goagain==1:
        list_from_file = get_from_file("australian.dat")
        list_with_random_decisive_class = change_decisive_class_to_random(list_from_file)
        copy_list_with_random_decisive_class = list_with_random_decisive_class.copy()
        for x in range(len(list_with_random_decisive_class)):
            copy_list_with_random_decisive_class[x] = list_with_random_decisive_class[x].copy()
        list_of_separated_by_decisive_class = separate_by_decisive_class(list_with_random_decisive_class)
        dict_of_central_points = get_central_points(list_of_separated_by_decisive_class)
        for point in list_with_random_decisive_class:
            point[-1] = change_decisive_class_based_on_euk_metric(dict_of_central_points,point)
        if (list_with_random_decisive_class != copy_list_with_random_decisive_class):
            print(check_diff(get_from_file("australian.dat"),list_with_random_decisive_class))
            goagain = 1
        else:
            goagain = 0
            return list_with_random_decisive_class

# print(ostateczna())

# -------------------
# CAŁKA MONTE CARLO
# -------------------

def calka_metoda_monte_carlo(xp,xk,ilosc_punktow):
    suma = 0
    przedzial_x = xk-xp
    
    for i in range(ilosc_punktow):
        suma+= wzorek(xp + random.random() * przedzial_x)
    srednia_wartosc_w_przedziale = przedzial_x * suma / ilosc_punktow
    przyblizowa_wartosc_calki_oznaczonej = math.floor(srednia_wartosc_w_przedziale * 1000) / 1000
    return przyblizowa_wartosc_calki_oznaczonej

def wzorek(x):
    return x

# print(calka_metoda_monte_carlo(0,1,10000000))

#rectangle calka

# print("przyblizona wartosc calki:",calka_metoda_monte_carlo(4,7,1000000))


# --------------
# PRACA DOMOWA
# --------------

def srednia(list1):
    return sum(list1)/len(list1)

lista = [7,4,-2]

def wariancja(list1):
    temp = 0
    for element in list1:
        temp = temp + pow(element-srednia(list1),2)
    return temp/len(list1)

def odchylenie_standardowe(list1):
    return pow(wariancja(list1),1/2)

# -------------------
# funkcje z wykładu
# -------------------

def srednia_wektor(list1):
    return np.dot(np.array(list1),np.ones(len(list1))/len(list1))

def wariancja_wektor(list1): 
    a = np.array(list1) - srednia_wektor(list1)*np.ones(len(list1))
    return np.dot(a,a)/len(list1)

# -------------------

macierz_punkty = [
    [2,1],
    [5,2],
    [7,3],
    [8,3]
]

def obliczanie_beta(nazwa_pliku):
    return np.dot(x,x)

# wzór  ( (x[transponowane]*x)^-1*x[transponowane]*y    )
# wyniki 2/7 5/14
    
print(obliczanie_beta("punkty.txt"))
