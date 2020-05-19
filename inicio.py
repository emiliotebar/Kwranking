"""
        KWRANKING
        Emilio Tébar 

        Reto semanal --> https://j2logo.com/#retoSemanal
"""


keywords = []

def carga_keywords():
    global keywords
    try:
        with open('fichero.txt','r') as fichero:
            for linea in fichero:
                keywords.append(linea.rstrip('\n'))
        print("Importación correcta")
        return
    except:
        print("Error en la importación.\nContacte con el departamento de informática.")

def listar_keywords():
    i = 0
    try:
        if keywords:
            print("LISTADO DE PALABRAS CLAVE")
            for key in keywords:
                print("{}. {}".format(i+1,key))
                i+=1
                if i % 20 == 0:
                    print("Presione enter para mostrar más palabras clave")
                    input()
        else:
            print("SIN PALABRAS")
    except:
        print("Error en la importación.\nContacte con el departamento de informática.")

    
def crear_fichero():
    ficher = open('fichero.txt','w')
    ficher.write("hola")
    ficher.close

# Menú de opciones del programa
while True:
    print("\nBienvenido a Kwranking!")
    opcion = input("\nIntroduce una opción:\n[1] Importar palabras clave\n[2] Mostrar palabras clave\n[0] Salir\n\n> ")

    if opcion == "1":
        carga_keywords()
    elif opcion == "2":
        listar_keywords()
    elif opcion == "0":
        print("Nos vemos!")
        break
    else:
        print("Opción incorrecta")