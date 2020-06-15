"""
        KWRANKING
        Emilio Tébar 

        Reto semanal --> https://j2logo.com/#retoSemanal
"""

import requests
from bs4 import BeautifulSoup
import db
from models import Keyword

keywords = []
dominio = "https://cookpad.com/"
dominio_google_search = "https://www.google.com/search?q={kw}&start={start}"

def mostrar_menu():
    print("------------Kwranking------------")
    print("\n\n[1] Importar palabras clave")
    print("[2] Mostrar palabras clave")
    print("[3] Comprobar palabras clave")
    print("[0] Salir")
    print("\n\n")

def carga_keywords():
    try:
        with open('fichero.txt','r') as fichero:
            for linea in fichero:
                linea = linea.strip('\n')
                objKeyword = Keyword(linea)
                objKeyword.save()

        print("Importación correcta")
        return Keyword.get_all()

    except FileNotFoundError:
        print("No se encuentra el fichero fichero.txt")
    except:
        print("Error en la importación.\nContacte con el departamento de informática.")

def listar_keywords(keywords):
    contador = 0
    try:
        if keywords:
            print("LISTADO DE PALABRAS CLAVE")
            for key in keywords:
                #print("{}. {}".format(contador+1 ,key))
                print(f'{contador+1}. KW: {key.keywords} > {key.posicion}')
                contador += 1
                if contador % 20 == 0:
                    input("Presione enter para mostrar más palabras clave")
        else:
            print("SIN PALABRAS")
    except:
        print("Error en la importación.\nContacte con el departamento de informática.")

def aparece_el_dominio(link, dominio):
    encontrado = False

    fin = link.find('&')
    pagina = link[:fin]
    if dominio in pagina:
        encontrado = True
    return encontrado

def comprueba_keywords(kw, dominio):
    posicion = 1
    continuar = True
    start = 0
    encontrado = False

    while continuar and not encontrado:
        parametros = {'q': kw, 'start': start}
        resp = requests.get(f'https://www.google.com/search', params= parametros)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            div_principal = soup.find('div', {'id': 'main'})
            resultados = div_principal.find_all('div', class_ = 'ZINbbc xpd O9g5cc uUPGi')

            for res in resultados:
                if res.div and res.div.a:
                    if aparece_el_dominio(res.div.a['href'], dominio):
                        encontrado = True
                        break
                    else:
                        posicion += 1
            
            if not encontrado:
                footer = div_principal.find('footer')
                siguiente = footer.find('a', {'aria-label': 'Página siguiente'})
                if siguiente:
                    start += 10
                    if start == 100:
                        continuar = False
                else:
                    continuar = False
        else:
            continuar = False

    if not encontrado:
        posicion = 100

    return posicion 

def actualiza_posicion(keywords):
    for key in keywords:
        posicion = comprueba_keywords(key.keywords, dominio)
        key.posicion = posicion if posicion < 100 else None 
        key.save()

def keywords_como_lista_de_valores(keywords):
    lista_valores = [(key.keywords, key.posicion) for key in keywords]
    return lista_valores

def run():

    keywords = Keyword.get_all()

    while True:
        mostrar_menu()
        opcion = input("Introduce una opción:")
        if opcion == "1":
            keywords = carga_keywords()
        elif opcion == "2":
            listar_keywords(keywords)
        elif opcion == "3":
            actualiza_posicion(keywords)
        elif opcion == "0":
            print("Nos vemos!")
            break
        else:
            print("Opción incorrecta")

### INICIO DEL PROGRAMA
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()