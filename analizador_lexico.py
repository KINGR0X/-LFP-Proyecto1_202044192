import graphviz
from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstract.lexema import *
from Abstract.numero import *
from Errores.errores import *
import os
import webbrowser


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
global lista_errores
global lista_DatosGraphviz

n_linea = 1
n_columna = 0
lista_lexemas = []
instrucciones = []
lista_errores = []
lista_DatosGraphviz = []


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

        elif char == '-':
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
            n_columna = 0
            n_linea += 1
            puntero = 0

        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            lista_errores.append(Errores(char, n_linea, n_columna))

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
    isNegative = False

    for char in cadena:
        puntero += char

        if char == "-":
            isNegative = True

        if char == ".":
            is_decimal = True

        # se comprueba cuando es que termino de leer el numero
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ']':
            if is_decimal:
                # el -1 se agrega para que la cadena devuelta tenga el salto de linea (\n), para asi sumarle la fila
                return float(numero), cadena[len(puntero)-1:]
            if isNegative:
                return int(numero), cadena[len(puntero)-1:]
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

            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')

        elif operacion and n1 and (operacion.operar(None) == 'Seno' or operacion.operar(None) == 'Coseno' or operacion.operar(None) == 'Tangente'):

            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')

    return None


# Antes de operar y eliminar los valores de la lista de lexemas, se guardan los datos para el grafico
def lexemas_grafico():
    global lista_lexemas

    for i in range(len(lista_lexemas)):
        lexema = lista_lexemas[i]
        if lexema.operar(None) == 'Texto':
            lista_DatosGraphviz.append(lista_lexemas[i+1].operar(None))
        if lexema.operar(None) == 'Color-Fondo-Nodo':
            lista_DatosGraphviz.append(lista_lexemas[i+1].operar(None))
        elif lexema.operar(None) == 'Color-Fuente-Nodo':
            lista_DatosGraphviz.append(lista_lexemas[i+1].operar(None))
        elif lexema.operar(None) == 'Forma-Nodo':
            lista_DatosGraphviz.append(lista_lexemas[i+1].operar(None))


def operar_():
    global instrucciones

    left = ""
    right = ""

    while True:

        operacion = operar()
        # se agregan los objetos que son operaciones a instrucciones
        if operacion:
            instrucciones.append(operacion)
        else:
            break

        # Se operan para obtener los resultados de las operaciones
        for instruccion in instrucciones:
            instruccion.operar(None)

    return instrucciones


def graficar():

    titulo = lista_DatosGraphviz[0]

    dot = 'digraph grafo{\n'

    for i in range(len(instrucciones)):
        dot += separar(i, 0, '', instrucciones[i])

    dot += f'''
    labelloc = "t"
    label = "{titulo}"
    '''

    dot += '}'

    return dot


def generarGrafica(nombreGrafica):

    nombre = nombreGrafica+".dot"

    # Creación del dot
    with open(nombre, 'w') as f:
        f.write(graficar())

    # creamos la imagen
    os.system(
        f'dot -Tpdf {nombre} -o {nombreGrafica}.pdf')

    # obtener direccion actual
    ruta = os.path.dirname(os.path.abspath(f"{nombreGrafica}.pdf"))

    # reta del pdf
    archivo_pdf = ruta+f"\{nombreGrafica}.pdf"

    path = f'file:///{archivo_pdf}'

    # Abrir pdf en el navegador
    webbrowser.open_new(path)


def limpiarLista():
    instrucciones.clear()
    lista_DatosGraphviz.clear()


def limpiarListaErrores():
    global n_linea
    lista_errores.clear()
    n_linea = 1


def separar(i, id, etiqueta, objeto):

    global lista_DatosGraphviz

    colorFondo = lista_DatosGraphviz[1]
    colorFuente = lista_DatosGraphviz[2]
    forma = lista_DatosGraphviz[3]

    rojo = '#ff0000'
    amarillo = '#ffff00'
    azul = '#00ff00'
    Morado = '#8a2be2'
    naranja = '#ffa500'
    verde = '#008000'
    negro = '#000000'

    # se establecen los colores de fondo
    if colorFondo == "Rojo":
        colorFondo = "red"
    elif colorFondo == "Amarillo":
        colorFondo = "yellow"
    elif colorFondo == "Azul":
        colorFondo = "blue"
    elif colorFondo == "Morado":
        colorFondo = "purple"
    elif colorFondo == "Naranja" or colorFondo == "Anaranjado":
        colorFondo = "orange"
    elif colorFondo == "Verde":
        colorFondo = "green"
    else:
        colorFondo = "yellow"

    # se establecen los colores de fuente
    if colorFuente == "Rojo":
        colorFuente = rojo
    elif colorFuente == "Amarillo":
        colorFuente = amarillo
    elif colorFuente == "Azul":
        colorFuente = azul
    elif colorFuente == "Morado":
        colorFuente = Morado
    elif colorFuente == "Naranja" or colorFuente == "Anaranjado":
        colorFuente = naranja
    elif colorFuente == "Verde":
        colorFuente = verde
    elif colorFuente == "Negro":
        colorFuente = negro
    else:
        colorFuente = rojo

    # se establecen las formas
    if forma == "Circulo":
        forma = "circle"
    elif forma == "Cuadrado":
        forma = "box"
    elif forma == "Poligono" or forma == "Polígono":
        forma = "polygon"
    elif forma == "Elipse":
        forma = "ellipse"
    elif forma == "Triangulo":
        forma = "triangle"
    elif forma == "Ovalo":
        forma = "oval"
    elif forma == "Rombo":
        forma = "diamond"
    elif forma == "Trapezoide":
        forma = "trapezium"
    else:
        forma = "oval"

        # ===============================================
    dot = ""

    if objeto:
        if type(objeto) == Numero:
            # print(objeto.valor)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'

        if type(objeto) == Trigonometrica:
            # print(objeto.valor)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'

            dot += separar(i, id+1, etiqueta+"_angulo", objeto.left)
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_angulo;\n'

        if type(objeto) == Aritmetica:
            # print(objeto.tipo.lexema)
            # print(objeto.valor)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'
            # print("sub izquierdo")

            dot += separar(i, id+1, etiqueta + "_left", objeto.left)
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_left;\n'
            # print("Sub derecho")
            dot += separar(i, id+1, etiqueta+"_right", objeto.right)

            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_right;\n'

    return dot


def getErrores():
    global lista_errores

    formatoErrores = '{\n'

    for i in range(len(lista_errores)):
        error = lista_errores[i]
        formatoErrores += error.operar(i+1)
        if i != len(lista_errores)-1:
            formatoErrores += ',\n'
        else:
            formatoErrores += '\n'

    # contador = 1
    # while lista_errores:
    #     error = lista_errores.pop(0)
    #     formatoErrores += error.operar(contador)
    #     if len(lista_errores) != 0:
    #         formatoErrores += ',\n'
    #     else:
    #         formatoErrores += '\n'
    #     contador += 1

    formatoErrores += '}'

    return formatoErrores


def CrearArchivoErrores():

    nombre = "ERRORES_202044192"+".json"

    # Creación del dot
    with open(nombre, 'w') as f:
        f.write(getErrores())

    # obtener direccion actual
    ruta = os.path.abspath(nombre)

    print(ruta)

    os.system(f'start notepad.exe {ruta}')


# entrada = '''{
#     { @
#         "Operacion":"Resta"
#         "Valor1":-650
#         "Valor2":[
#                 "Operacion":"Suma"
#                 "Valor1":2.11
#                 "Valor2":1.5329
#                 ]
#     }, @
#     {
#         "Operacion":"Multiplicacion"
#         "Valor1":4
#         "Valor2": [
#             "Operacion":"Potencia"
#             "Valor1":2
#             "Valor2":[
#                 "Operacion":"Raiz"
#                 "Valor1":9
#                 "Valor2":2
#                 ]
#         ]
#     },@
#     {
#         "Operacion":"Suma"
#         "Valor1":[
#         "Operacion":"Coseno"
#         "Valor1":180
#         ]
#         "Valor2":5.32
#     }
#     "Texto":"===Realizacion de Operaciones===="
#     "Color-Fondo-Nodo":"Amarillo"
#     "Color-Fuente-Nodo":"Verde"
#     "Forma-Nodo":"Ovaloasd"
# }'''


# instruccion(entrada)
# lexemas_grafico()
# operar_()
# graficar()
# generarGrafica(str("RESULTADOS_202044192"))

# CrearArchivoErrores()
