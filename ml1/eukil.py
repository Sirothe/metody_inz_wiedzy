def plik_na_liste(file):
    lista = []
    with open(file, "r") as file:
        for line in file:
            lista.append(list(map(lambda x: float(x), line.replace("\n", "").split())))
    return lista

def odl_eukalidesowa(list1, list2):
    sum = 0
    for x in range(len(list1)-1):
        sum += pow(list2[x] - list1[x], 2)
    return pow(sum, 1/2)

def odleglosci(macierz):
    dictonary = {0: [], 1: []}
    for x in range(1, len(macierz), 1):
        dictonary[macierz[x][len(macierz[x])-1]].append(odl_eukalidesowa(macierz[0], macierz[x]))
    return dictonary


macierz = plik_na_liste("australian.dat")
lista_odleglosci = odleglosci(macierz)
print(lista_odleglosci)