import numpy as np


# ZAMIANA BAZ

wektor1 = np.array([1,1,1,1,1,1,1,1])
wektor2 = np.array([1,1,1,1,-1,-1,-1,-1])
wektor3 = np.array([1,1,-1,-1,0,0,0,0])
wektor4 = np.array([0,0,0,0,1,1,-1,-1])
wektor5 = np.array([1,-1,0,0,0,0,0,0])
wektor6 = np.array([0,0,1,-1,0,0,0,0])
wektor7 = np.array([0,0,0,0,1,-1,0,0])
wektor8 = np.array([0,0,0,0,0,0,1,-1])

macierz = np.array([wektor1,wektor2,wektor3,wektor4,wektor5,wektor6,wektor7,wektor8])

# print("----------------------------------------------")
# print("--------------MACIERZ-DIAGONALNA--------------")
# print("----------------------------------------------")
# print(np.dot(macierz,macierz.T))

xa = np.array([8,6,2,3,4,6,6,5])

def dlugosc_wektora(wektor):
    return pow(np.dot(wektor,wektor),1/2)

macierz_znormalizowana = np.array([wektor/dlugosc_wektora(wektor) for wektor in macierz],dtype=np.float64)

# macierz znormalizowana
print("----------------------------------------------")
print("------------MACIERZ-ZNORMALIZOWANA------------")
print("----------------------------------------------")
print(macierz_znormalizowana)

# macierz znormalizowana transponowana
print("----------------------------------------------")
print("-----MACIERZ-ZNORMALIZOWANA-TRANSPONOWANA-----")
print("----------------------------------------------")
print(macierz_znormalizowana.T)

# macierz znormalizowana (foo)
print("----------------------------------------------")
print("--------MACIERZ-ZNORMALIZOWANA-FUNKCJA--------")
print("----------------------------------------------")
print(np.linalg.inv(macierz))

xb = np.dot(macierz_znormalizowana,xa.T)
print("-------------------------------------")
print("------WEKTOR-W-ZMIENIONEJ-BAZIE------")
print("-------------------------------------")
print(xb)
