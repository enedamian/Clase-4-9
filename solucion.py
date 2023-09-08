import os #libreria operative sistem

def existe_archivo (ruta):
    """devuelve true si el archivo exite y false en caso contrario"""
    if os.path.isfile(ruta): 
        return True
    else:
        return False
    

def generar_lista_sin_signos (lista):
    """Quita los signos a cada palabra"""
    lista_limpia = []
    for palabra in lista:
            lista_limpia.append (palabra.strip (" ,.¡!¿? \n").lower())
    return lista_limpia

def generar_lista_palabras (nombre_archivo):

    if existe_archivo (nombre_archivo):
        archivo = open (nombre_archivo, 'r', encoding= "utf-8")#encodign para solucionar la deteccion de acentos
        lista_palabras = []

        for linea in archivo:
            lista_aux = linea.split()
            lista_palabras += generar_lista_sin_signos (lista_aux)
        archivo.close()
        return lista_palabras
    else:
        return[]

def contar_frecuencia (lista):
    """devuelve un diccionario con la cantidad de veces que se repite la palabra"""
    dic_palabras = {} # es lo mismo que = dict ()
    for palabra in lista:

        if palabra in dic_palabras:#si la palabra existe suma uno a la cantidad
            dic_palabras [palabra] += 1
        else:#sino existe todavia declara la palabra en 1
            dic_palabras[palabra] = 1

    return dic_palabras


def buscar_palabra_mas_frecuente (diccionario):
    """devuelve la llave de la palabra mas frecuente"""
    frecuencia_mayor = 0
    llave_mayor = ""
    for llave in diccionario:
        if diccionario [llave] > frecuencia_mayor and len(llave)>2:
            frecuencia_mayor = diccionario [llave]
            llave_mayor = llave
    return llave_mayor


def calcular_longitud_promedio_palabras (lista):
    suma = 0
    for palabra in lista :
        suma += len(palabra)
    return int (suma / len(lista))

def buscar_palabra_menos_frecuente (diccionario):
    """devuelve la llave de la palabra mas frecuente"""
    frecuencia_menor = 150
    llave_menor = ""
    for llave in diccionario:
        if diccionario [llave] < frecuencia_menor and len(llave)>2:
            frecuencia_menor = diccionario [llave]
            llave_menor = llave
    return llave_menor


def generar_lista_palabras_menos_frecuentes(diccionario):
    lista_palabras_menos_frecuentes = []
    
    # Encuentra la frecuencia mínima
    frec_menor = min(diccionario.values())

    # Encuentra las palabras que tienen la frecuencia mínima
    for llave, frecuencia in diccionario.items():
        if frecuencia == frec_menor and len(llave) > 2:
            lista_palabras_menos_frecuentes.append(llave)

    return lista_palabras_menos_frecuentes


nombre_archivo = input ("Ingrese la ruta del archivo = ")
lista_palabras = generar_lista_palabras (nombre_archivo)
dic_frecuencia_palabras = contar_frecuencia (lista_palabras)
palabra_mas_frecuente = buscar_palabra_mas_frecuente(dic_frecuencia_palabras)
palabra_menos_frecuente = buscar_palabra_menos_frecuente(dic_frecuencia_palabras)
promedio_longitud_palabras = calcular_longitud_promedio_palabras (lista_palabras)
lista_menos_frecuentes = generar_lista_palabras_menos_frecuentes (dic_frecuencia_palabras)


print ("La palabra mas frecuente es : ", palabra_mas_frecuente, " con ", dic_frecuencia_palabras[palabra_mas_frecuente], " apariciones ")
print ("La palabra menos frecuente es : ", palabra_menos_frecuente, " con ", dic_frecuencia_palabras[palabra_menos_frecuente], " apariciones ")
print ("Las palabras menos frecuentes son = ", lista_menos_frecuentes)
print ("El promedio de longitud de las palabras es ", promedio_longitud_palabras)
