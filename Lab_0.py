import numpy as np
import pandas as pd
import statistics as st
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
        
def ejercicio2_1(data):
    df= pd.DataFrame(data)
    Minima = df['Notas'].min()
    Maxima = df['Notas'].max()
    Media = df['Notas'].mean()
    Desviacion = df['Notas'].std()  # `std()` usa n-1 (muestra)
    
    # Retornar una serie con los resultados
    return pd.Series({
        "Nota Minima": Minima,
        "Nota Maxima": Maxima,
        "Nota Media": Media,
        "Desviacion tipica": Desviacion
    })
    
    
#ejercicio1_1()

#ejercicio1_2()

#ejercicio1_3(3)

#ejercicio1_4(3)
data = {
    'Nombre': ['Ana', 'Luis', 'Juan'],
    'Notas': [4.3, 2.9, 3.7]
}
ejercicio2_1(data)
