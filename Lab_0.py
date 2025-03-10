import numpy as np

def ejercicio1_1():
    arr_1d = np.linspace(3,12,4)  # (inicio, fin, numero de muestras)
    print("Arreglo usando linspace: ", arr_1d)

def ejercicio1_2():
    arr_1d = np.arange(9,2,-2)  # (inicio, fin, paso)
    print("Arreglo usando arange: ", arr_1d)
    
def ejercicio1_3(N):
    union = np.zeros((N,N)) #Crea matriz con ceros

    for i in range(N):
        union[i,i] = 1
         
    print("Matriz identidad de dimension : ", N )
    print(union)

def ejercicio1_4(N):
    union = np.zeros((N,N)) #Crea matriz con ceros

    for i in range(N):
        union[i,i] = i
         
    print("Matriz identidad de dimension : ", N )
    print(union)
        

ejercicio1_1()

ejercicio1_2()

ejercicio1_3(3)

ejercicio1_4(3)