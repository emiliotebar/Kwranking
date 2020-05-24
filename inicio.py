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
    except FileNotFoundError:
        print("No se encuentra el fichero fichero.txt")
    except:
        print("Error en la importación.\nContacte con el departamento de informática.")

def listar_keywords():
    contador = 0
    try:
        if keywords:
            print("LISTADO DE PALABRAS CLAVE")
            for key in keywords:
                print("{}. {}".format(contador+1 ,key))
                contador += 1
                if contador % 20 == 0:
                    input("Presione enter para mostrar más palabras clave")
        else:
            print("SIN PALABRAS")
    except:
        print("Error en la importación.\nContacte con el departamento de informática.")

def mostrar_menu():
    print("\n------------Kwranking------------")
    print("\n\n[1] Importar palabras clave")
    print("\n[2] Mostrar palabras clave")
    print("\n[0] Salir")
    print("\n\n")

def run():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción:")
        if opcion == "1":
            carga_keywords()
        elif opcion == "2":
            listar_keywords()
        elif opcion == "0":
            print("Nos vemos!")
            break
        else:
            print("Opción incorrecta")

### INICIO DEL PROGRAMA
if __name__ == '__main__':
    run()