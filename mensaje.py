import data.plantas as plantas
import funciones as fun

def intro (z):
    if z ==1:
        print('\n Total de megavatios de consumos de una ciudad en Una Planta [1]')
        print('Total de megavatios que cada Planta entrego a una ciudad [2]')
        print('Generado por Region [3]')
        print('Generado por planta en un mes determinado [4]')
        print()
        return('Para salir [0] \n ' )

def validar_plan (nombre) :
    if nombre != 'Sopladora' and nombre != 'Coca Codo Sinclair':
        
        return('ERROR DE DIGITALIZACIÓN') 
    

def meses_anho (mes):
    if mes == 0:
        return ('Enero')
    elif mes == 1:
        return ('Febrero')
    elif mes == 2:
        return ('Marzo')
    elif mes == 3:
        return('Abril')
    elif mes == 4:
        return('Mayo')
    elif mes == 5:
        return('Junio')
    elif mes == 6:
        return('Julio')
    elif mes ==7:
        return('Agosto')
    elif mes ==8:
        return('Septiembre')
    elif mes == 9:
        return('Octubre')
    elif mes == 10:
        return('Noviembre')
    elif mes == 11:
        return('Diciembre')
    else:
        return('MES NO EXISTE')

def mostrar_plantas(q):
    if q ==1:
        print ('\n Las Plantas Existentes son: \n')
        for i in plantas.consumo_energia:
            print( i)
    return('----------------------------------------')
    