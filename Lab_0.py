import numpy as np
import pandas as pd
from scipy.io.wavfile import read # Libreria para archivos de audio en formato wav.
from IPython.display import Audio # Libreria para escuchar un audio
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
    Desviacion = df['Notas'].std()  # 
    
    # Retornar una serie con los resultados
    return pd.Series({
        "Nota Minima": Minima,
        "Nota Maxima": Maxima,
        "Nota Media": Media,
        "Desviacion tipica": Desviacion
    })
    
def ejercicio2_2(directorio):
    df_from_xlsx = pd.read_excel(directorio)
    df_return=[]
    for i in range(df_from_xlsx.shape[1]):
        if((i)%2):
            df_return.append(df_from_xlsx.iloc[:, i])
    return df_return
            
def ejercicio_3(directorio, t1, t2):
    fs, x = read(directorio)
    inicio = int(t1*fs)
    final = int(t2*fs)
    audio_salida
    Audio(x, rate=fs)

    
#ejercicio1_1()

#ejercicio1_2()

#ejercicio1_3(3)

#ejercicio1_4(3)


#data = {
#    'Nombre': ['Ana', 'Luis', 'Juan'],
#    'Notas': [4.3, 2.9, 3.7]
#}
#print(ejercicio2_1(data))

#print(ejercicio2_2("dataframe_lab0.xlsx"))

ejercicio_3("audio.wav",2, 3)