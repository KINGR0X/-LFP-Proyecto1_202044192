# palabras reservadas (lexemas)

#  token | lexema
reserved = {
    "Reser_operacion": "operacion",
    "reser_valor1": "valor1",
    "reser_valor2": "valor2",
    "reser_suma": "suma",
    "reser_resta": "resta",
    "reser_multiplicacion": "multipliacacion",
    "reser_division": "division",
    "reser_potencia": "potencia",
    "reser_raiz": "raiz",
    "reser_inverso": "inverso",
    "reser_seno": "seno",
    "reser_coseno": "coseno",
    "reser_tangente": "tangente",
    "reser_modulo": "modulo",
    "reser_texto": "texto",
    "reser_colorFondoNodo": "color_fondo_nodo",
    "reser_colorFuenteNodo": "color_fuente_nodo",
    "reser_formaNodo": "forma_nodo",
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
n_columna = 1
lista_lexemas = []


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

                # se guarda el lexema en la lista
                lista_lexemas.append(lexema)
                # +1 por la comilla final
                n_columna += len(lexema)+1
                puntero = 0

        elif char.isdigit():
            # no se recorta porque se estaria eliminando el primer numero
            token, cadena = armar_numero(cadena)

            if token and cadena:
                n_columna += 1

                # se guarda el lexema en la lista
                lista_lexemas.append(token)
                # +1 por la comilla final
                n_columna += len(str(token))+1
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

    for lexema in lista_lexemas:
        print(lexema)


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

        # cuando termina de leer el numero se enceuntran espacios
        if char == '"' or char == ' ' or char == '\n' or char == '\t':
            if is_decimal:
                # el -1 se agrega para que la cadena devuelta tenga el salto de linea (\n), para asi sumarle la fila
                prueba1 = cadena[len(puntero):]
                prueba2 = cadena[len(puntero)-1:]
                print(prueba1)
                print(prueba2)

                return float(numero), cadena[len(puntero)-1:]

            else:
                return int(numero), cadena[len(puntero)-1:]

        # si aun no se a terminado de leer el numero se sigue armando
        else:
            numero += char
    return None, None


entrada = '''
    {
 { 
    "Operacion":"Suma"
    "Valor1":4.5
    "Valor2":5.32
 },
 {
    "Operacion":"Resta"
    "Valor1":4.5
    "Valor2": [
            "Operacion":"Potencia"
            "Valor1":10
            "Valor2":3
 ]},
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
}


'''


instruccion(entrada)
