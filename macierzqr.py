import numpy as np
import sys

def projekcja(u, v):
    return (np.dot(v,u) / np.dot(u,u)) * u

def dlugosc_wektora(v):
    return pow(np.dot(v,v), 1/2)

def qr(macierz):
    macierz = np.transpose(macierz)
    q, u_list = [], [macierz[0]]
    e = np.array(u_list[0]) / dlugosc_wektora(u_list[0])
    q.append(e)

    for x in range(1, len(macierz)):
        u = macierz[x]
        for y in range(len(u_list)):
            u = u - projekcja(u_list[y], macierz[x])
        u_list.append(u)
        e = u / dlugosc_wektora(u)
        q.append(e)

    r = np.dot(q, np.transpose(macierz))
    q = np.transpose(q)
    return (q, r)

def ak(macierz, k):
    for x in range(len(macierz)):
        if (macierz == np.transpose(macierz)).all():
            for x in range(k):
                q, r = qr(macierz)
                macierz = np.dot(r,q)
            return macierz
        else:
            print("Macierz nie jest symetryczna")
            return

def czy_trojkatna_gorna(macierz, sigma = 0.001):
    for x in range(len(macierz)):
        for y in range(len(macierz[x])):
            if y < x:
                if macierz[x][y] > sigma:
                    return False
    return True


def wartosci_wlasne(macierz):
    for x in range(len(macierz)):
        if (macierz == np.transpose(macierz)).all():
            while not czy_trojkatna_gorna(macierz):
                q, r = qr(macierz)
                macierz = np.dot(r,q)
            return macierz
        else:
            print("Macierz nie jest symetryczna")
            return
        

#--------TEST-DEKOMPOZYCJI---------
macierz = np.array([[2,0], [0,1], [1,2]])
print(qr(macierz))
#-----------------------------------

#------------TEST-WARTOŚCI-WŁASNYCH-(k statyczne)-----------
macierz2 = np.array([[1,1,0], [1,0,1], [0,1,1]])
print("k = 3 \n", ak(macierz2, 3))
print("k = 6 \n", ak(macierz2, 6))
print("k = 9 \n", ak(macierz2, 9))
#-----------------------------------------------------------

#-----------TEST-WARTOŚCI-WŁASNYCH-(k statyczne)-----------
macierz2 = np.array([[1,1,0], [1,0,1], [0,1,1]])
print(wartosci_wlasne(macierz2))
#----------------------------------------------------------

#------------METODA-ELIMINACJI-GAUSSA---------------------

def gauss_elimination(matrix):
    matrix = np.array(matrix, dtype=np.float64)
    matrix.dtype = np.float64
    for x in range(len(matrix)):
        if matrix[x][x] == 0.0:
            sys.exit("dzielenie przez 0")
        for y in range (x+1, len(matrix)):
            ratio = matrix[y][x]/matrix[x][x]
            for z in range(len(matrix)+1):
                matrix[y][z] = matrix[y][z] - ratio * matrix[x][z]
    return matrix

def back_substitution(matrix):
    ans = np.zeros(len(matrix))
    ans[len(matrix)-1] = matrix[len(matrix)-1][len(matrix)]/matrix[len(matrix)-1][len(matrix)-1]
    for x in range(len(matrix)-2, -1, -1):
        ans[x] = matrix[x][len(matrix)]
        for y in range(x+1, len(matrix)):
            ans[x] = ans[x] - matrix[x][y]*ans[y]
        ans[x] = ans[x]/matrix[x][x]
    return ans

def gauss_equation_solving(matrix):
    return back_substitution(gauss_elimination(matrix))