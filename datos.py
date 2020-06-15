import openpyxl



def exportar_resultados_a_xlsx(keywords):
    wb = openpyxl.Workbook()
    hoja = wb.active
    hoja.title = "Valores"

    # Fila del encabezado con los títulos
    hoja.append(('Keywords','Posición'))

    for key in keywords:
        hoja.append(key)

    wb.save('keywords.xlsx')