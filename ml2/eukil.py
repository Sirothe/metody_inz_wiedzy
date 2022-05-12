from asyncio.windows_events import NULL
from xmlrpc.client import MAXINT
from pyparsing import line_end


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

print(mierzymy1(x,macierz))
print(grupujemy(mierzymy1(x,macierz),20))
print(decyzja(grupujemy(mierzymy1(x,macierz),20)))
print(decyzja({0:5,1:5}))