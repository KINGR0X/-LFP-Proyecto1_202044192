import graphviz
from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstract.lexema import *
from Abstract.numero import *
import os


# palabras reservadas (lexemas)

#  token | lexema
reserved = {
    "Reser_operacion": "Operacion",
    "reser_valor1": "Valor1",
    "reser_valor2": "Valor2",
    "reser_suma": "Suma",
    "reser_resta": "Resta",
    "reser_multiplicacion": "Multiplicacion",
    "reser_division": "Division",
    "reser_potencia": "Potencia",
    "reser_raiz": "Raiz",
    "reser_inverso": "Inverso",
    "reser_seno": "Seno",
    "reser_coseno": "Coseno",
    "reser_tangente": "Tangente",
    "reser_modulo": "Modulo",
    "reser_texto": "Texto",
    "reser_colorFondoNodo": "Color_Fondo_Nodo",
    "reser_colorFuenteNodo": "Color_Fuente_Nodo",
    "reser_formaNodo": "Forma_Nodo",
    "coma": ",",
    "punto": ".",
    "dosPuntos": ":",
    "corc_izquierdo": "[",
    "corc_derecho": "]",
    "llave_izquierda": "{",
    "llave_derecha": "}",

}

# pasar los valores del diccionario a lista
lexemas = list(reserved.values())

global n_linea
global n_columna
global instrucciones
global lista_lexemas

n_linea = 1
n_columna = 0
lista_lexemas = []
instrucciones = []


def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ""
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1
        # si se encuentra la comilla de apertura
        if char == '\"':
            # se envia al metodo la cadena sin la comilla inicial
            lexema, cadena = armar_lexema(cadena[puntero:])
            # si no es None ninguna de las dos condiciones entonces
            if lexema and cadena:
                # +1 por la comilla de inicio
                n_columna += 1

                # Armado de lexema como clase
                l = Lexema(lexema, n_linea, n_columna)

                # se guarda el lexema en la lista
                lista_lexemas.append(l)
                # +1 por la comilla final
                n_columna += len(lexema)+1
                puntero = 0

        elif char.isdigit():
            # no se recorta porque se estaria eliminando el primer numero
            token, cadena = armar_numero(cadena)

            if token and cadena:
                # n_columna += 1

                # Armado de lexema como clase
                n = Numero(token, n_linea, n_columna)

                # se guarda el lexema en la lista
                lista_lexemas.append(n)
                # +1 por la comilla final
                n_columna += len(str(token))
                puntero = 0

        elif char == "[" or char == "]":
            # Armado de lexema como clase
            c = Lexema(char, n_linea, n_columna)

            n_columna += 1
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0

        elif char == "\t":
            cadena = cadena[4:]
            n_columna += 4
            puntero = 0

        elif char == "\n":
            cadena = cadena[1:]
            n_columna = 1
            n_linea += 1
            puntero = 0
        else:  # Este else sirve para sumar los espacios en blanco, por eso se reinicia el puntero
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

    # for lexema in lista_lexemas:
    #     print(lexema)

    return lista_lexemas


def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ""
    puntero = ""
    # se recorre toda lacadena con el puntero hasta encontrar ["]
    for char in cadena:
        puntero += char
        if char == '\"':
            # en cadena el slicing devuelce desde el puntero hasta el final
            return lexema, cadena[len(puntero):]
        else:
            # se va agregando letra por letra al lexema
            lexema += char
    # para evitar que se detenga el problema en caso de un error
    return None, None


def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False

    for char in cadena:
        puntero += char

        if char == ".":
            is_decimal = True

        # se comprueba cuando es que termino de leer el numero
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ']':
            if is_decimal:
                # el -1 se agrega para que la cadena devuelta tenga el salto de linea (\n), para asi sumarle la fila
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]

        # si aun no se a terminado de leer el numero se sigue armando
        else:
            numero += char
    return None, None


def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    # mientras exista una losta de lexemas se opera el while
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)

        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()  # se llama a el mismo hasta que devuelva un numero
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        # se arma la operacion segun sea aritmetico o trigonometrica

        if operacion and n1 and n2:

            # print("Operacion===>", operacion.lexema)
            # print("N1===>", n1.operar(None))
            # print("N2===>", n2.operar(None))
            # graficar(operacion.lexema, n1.operar(None), n2.operar(None))

            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')

        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):

            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')

    return None


def operar_():
    global instrucciones
    while True:

        operacion = operar()
        # se agregan los objetos que son operaciones a instrucciones
        if operacion:
            instrucciones.append(operacion)
        else:
            break

    for instruccion in instrucciones:

        # print(type(instruccion) )
        # de momento solo imprime la operacion superior
        print("Tipo===>", instruccion.tipo.operar(None))
        print("N1===>", instruccion.left.operar(None))

        if (type(instruccion) is Aritmetica):

            try:
                print("==== in the deep ====")
                print("Tipo===>", instruccion.right.tipo.operar(None))
                print("N1===>", instruccion.right.left.operar(None))
                print("N1===>", instruccion.right.right.operar(None))

            except:
                pass

        try:
            print("N2===>", instruccion.right.operar(None))

        except:
            pass

        print("Resultado===>", instruccion.operar(None))

        # print("Operacion===>", operacion.lexema)
        # print("N1===>", n1.operar(None))
        # print("N2===>", n2.operar(None))

    # for i in range(len(instrucciones)):
    #     print("Valor1:", instrucciones[i].left.operar(None))
    # try:
    #     print("Valor2:", instrucciones[i].right.operar(None))
    #     print("tipo===>", instrucciones[i].tipo.lexema)
    #     print("resutado===>", instrucciones[i].operar(None))
    # except:
    #     pass

    return instrucciones


# graficar
def graficar(tipo, left, right):
    tipo = str(tipo)
    left = str(left)
    right = str(right)

    d = graphviz.Digraph(filename='prueba.gv')

    # cabecera
    with d.subgraph() as s:
        s.attr(rank='same')
        s.node(tipo)

    # Nodo , union
    d.edges([(tipo, left), (tipo, right)])

    d.view()


entrada = '''{
    {
        "Operacion":"Resta"
        "Valor1":650
        "Valor2":[
                "Operacion":"Suma"
                "Valor1":2.11
                "Valor2":1.5329
                ]
    },
    {
        "Operacion":"Multiplicacion"
        "Valor1":4
        "Valor2": [
            "Operacion":"Potencia"
            "Valor1":2
            "Valor2":[
                "Operacion":"Raiz"
                "Valor1":9
                "Valor2":2 
                ]
        ]
    },
    {
        "Operacion":"Suma"
        "Valor1":[
        "Operacion":"Seno"
        "Valor1":90
        ]
        "Valor2":5.32
    }
    "Texto":"Realizacion de Operaciones"
    "Color-Fondo-Nodo":"Amarillo"
    "Color-Fuente-Nodo":"Rojo"
    "Forma-Nodo":"Circulo"
}'''


instruccion(entrada)
operar_()
