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
    Minima = 999999
    Maxima = 0
    Media = 0
    i = 0
    for nota in df['Notas']:
        i += 1
        if(nota > Maxima):
            Maxima = nota
        if(nota < Minima):
            Minima = nota
        Media += nota
    Desviacion= st.stdev(df['Notas'])
    print("Nota Minima: ",Minima)
    print("Nota Maxima: ",Maxima)
    print("Nota Media: ",Media/i)
    print("Desviacion tipica: ",Desviacion)
    
    
    
#ejercicio1_1()

#ejercicio1_2()

#ejercicio1_3(3)

#ejercicio1_4(3)
data = {
    'Nombre': ['Ana', 'Luis', 'Juan'],
    'Notas': [4.3, 2.9, 3.7]
}
ejercicio2_1(data)
