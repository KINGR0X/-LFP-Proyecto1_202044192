# Manual técnico

## Requisitos para poder utilizar el programa

1. Tener instalado en la computadora python.
2. tener instalado en la computadora Visual Studio Code.
3. Tener un previsualizador de markdown en Visual Studio Code.

## Archivo analizador_lexico.py

### instruccion(cadena), armar_lexema(cadena), armar_numero(cadena)

La función instrucción recibe como parámetro una cadena de caracteres, archivo de entrada, y analiza cada carácter de la cadena para determinar si es un lexema aceptado por el programa o no. Si es un lexema aceptado se guarda en **lista_lexemas** y se continua analizando la cadena, si no es un lexema aceptado se guarda en **lista_errores** y se continua analizando la cadena.

```python
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

```

si el carácter que se esta leyendo es una comilla de apertura (") se llama a la función **armar_lexema** para recorrer la cadena hasta que se encuentre la comilla de cierre (") y devolver el lexema armado y la cadena ya "cortada" sin el lexema ya guardado. También Reiniciamos el puntero que utilizamos para recorrer la cadena, se guarda el numero de columna y el numero de fila.

```python
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

```

Si el carácter que se esta leyendo es un número se llama a la función **armar_numero** para recorrer la cadena hasta que se encuentre un caracter que no sea un número y devolver el número armado y la cadena ya "cortada" sin el número ya guardado. Se reinicia el puntero que utilizamos para recorrer la cadena, se guarda el numero de columna y el numero de fila.

```python
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
```

La función **armar_numero** recibe como parámetro la cadena de caracteres y analiza cada carácter de la cadena hasta encontrar uno de los siguientes caracteres: **" ", "\n", "\t", "]" o '"'**, estos caracteres indican que el número a acabado debido al formato del archivo. También se verifica si el número es decimal o es negativo, para devolver el número respectivo, de la misma manera se devuelve la cadena ya cortada.

```python
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

```

Si el carácter es **"-"** significa que es un número negativo, por lo cual se llama a la función **armar_numero**, para armar el número y devolverlo.

```python
lif char == '-':
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

```

Si el carácter es un corchete **"[" o "]"** se guarda la cadena, se suma 1 al numero de columna, se reinicia el puntero y se actualiza la cadena cortada.

```python
elif char == "[" or char == "]":
            # Armado de lexema como clase
            c = Lexema(char, n_linea, n_columna)

            n_columna += 1
            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0

```

Si hay una tabulacion, **\t**, se corta esa concatenación de la cadena, se actualiza el número de columna el puntero.

```python
 elif char == "\t":
            cadena = cadena[4:]
            n_columna += 4
            puntero = 0

```

Si hay un salto de línea, **\n**, se corta esa concatenación de la cadena, se actualiza el número de columna, el número de línea y el puntero.

```python
 elif char == "\n":
            cadena = cadena[1:]
            n_columna = 0
            n_linea += 1
            puntero = 0

```

Si el carácter es uno de los siguientes caracteres **" ", "\r", "{", "}", ",", ":", "."** se corta la cena, se actualiza el número de columna y el puntero.

```python
elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0

```

si el carácter no es ninguno de los anteriores se guarda en la lista de errores, se corta la cadena, se actualiza el número de columna y el puntero.

```python
else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            lista_errores.append(Errores(char, n_linea, n_columna))

```

## Función operar\_() y operar()

La función operar llama a la función **operar()**, la cual arma el árbol de las operaciones aritmeticas y trigonométricas, si la variable **operacion** no es **None** se agrega a la lista de instrucciones, de lo contrario se rompe el ciclo. LUego se iteran las instrucciones para guardar los resultados de las operaciones.

```python
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

```

La función **operar()** itera sobre la lista de lexemas si el lexema es "Operacion" o "valor1" o "valor2" se guarda en operacion, se usa la recursividad para buscar todos los valores que conforman la operación, al tener una operacion, un valor 1 y valor 2 se guarda como una operación aritmetica, si por el contrario solo es una operacion, un valor 1 y el lexema es "Seno", "Coseno", "Tangente" se guarda como una operación trigonométrica. Se pasan los valores a la clase Aritmetica o Trifonometrica respectivamente y se retorna el objeto.

```python

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
```

### Función generarGrafica(), graficar() y separar()

La función **generarGrafica()** recibe el nombre de la gráfica para usarlo como para la gráfica, ya que no se crean archivo diferentes por cada archivo de entrada el nombre es siempre el mismo.Generar Grafica llama a la función **graficar()** para crear el archivo, luego se convierte el archivo **dot** a **pdf**.

Para que el pdf se abra en el navegador se guarda la ruta del archivo utilizando la función **os.path.abspath**, se concatena la ruta del pdf con su nombre, y se abre en el navegador.

```python
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

```

La función gráficar crea el archivo **dot** utilizando la función **separar()** para crear los nodos y las relaciones entre ellos, tambien se le agrega el titulo de la gráfica y las llaves de inicio y de fin.

```python
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
```

La función **separar()** recive como argumento el indice del ciclo for de la función graficar, un id para los nodos, una etiqueta para los nodos y el objeto que se va a graficar. segun el archivo de entrada se le asigna un color al fondo de los nodos, un color de fuente, y la forma de dichos nodos. Debido a que son una gran cantidad de colores y formas, solo se definieron los más comunes, si alguno de los argumentos anteriores no esta definido se le coloca un color y una forma por defecto

Cada nodo esta conformado por un id, un label que es el valor que se va a mostrar en el nodo, un color de fuente, un color de fondo y la forma. Se utsa la recursividad en caso de que el objeto sea de tipo Artimeticas o Trigonometricas, para recorrer los valores izquierdos y derechos de los objetos y asi obtener los valores.

```python
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
```

### CrearArchivoErrores() y getErrores()

La función **CrearArchivoErrores()** crear el archivo de errores con extension .json, Para obtener la lista de errores llama a la función **getErrores()** para obtener el formato del archivo json, luego obtiene la direccion del archivo para abrirlo con el block de notas. Escogi abrirlo con el block de notas.

```python
def CrearArchivoErrores():

    nombre = "ERRORES_202044192"+".json"

    # Creación del dot
    with open(nombre, 'w') as f:
        f.write(getErrores())

    # obtener direccion actual
    ruta = os.path.abspath(nombre)

    print(ruta)

    os.system(f'start notepad.exe {ruta}')

```

Como se menciono anteriormente la función **getErrores()** obtiene el formato de los errores, recorriendo la lista de errores que ya tienen un formato creado con la claase **Errores**, asi que le coloca las llaves necesarias, saltos de lineas y comas del formato de un json

```python
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

    formatoErrores += '}'

    return formatoErrores
```

También se definen las funciones **limpiarLista()** y **limpiarListaErrores()**, que como su nombre indica limpian las listas para que al momento de que se analice un archivo, y luego se analice otro archivo las listas este vacías y no ocurra ningún error.

```Python

def limpiarLista():
    instrucciones.clear()
    lista_DatosGraphviz.clear()


def limpiarListaErrores():
    global n_linea
    lista_errores.clear()
    n_linea = 1

```

## Archivo errores.py

En este archivo se crea la clase **Errores** la cual le da formato a los errores que detecta el analizador léxico.

```python
class Errores(Expression):

    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, no):
        no_ = f'\t\t"No.":{no}\n'
        desc = '\t\t"Descripcion-Token":{\n'
        lex = f'\t\t\t"Lexema": {self.lexema}\n'
        tipo = '\t\t\t"Tipo": Error\n'
        columna = f'\t\t\t"Columna": {self.columna}\n'
        fila = f'\t\t\t"Fila": {self.fila}\n'
        fin = "\t\t}\n"

        return '\t{\n' + no_ + desc + lex + tipo + columna + fila + fin + '\t}'

    def getColumna(self):
        return super().getColumna()

    def getFila(self):
        return super().getFila()

```

## Clases abstractas

El archivo **abstractas.py** como su nombre indica es una clase abstracta donde se definen diferentes métodos que son utilizados por otros archivo, es una clase abstracta ya que cada archivo que implementa la clase abstracta hace uso de los métodos que se definen en esta clase de una manera diferente.

```python

from abc import ABC, abstractmethod


class Expression(ABC):

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def operar(self, arbol):
        pass

    @abstractmethod
    def getFila(self):
        return self.fila

    @abstractmethod
    def getColumna(self):
        return self.columna
```

Los archivos de **lexema.py**, y **numeros.py** son clases abstracatas que son utilizadas para obtener el lexema, la fila y la columna de los tokens.

## Archivos de operaciones

Los archivos **aritmeticas.py** y **trigonometricas.py** tambien hacen uso de las clases abstractas para saber que tipo de operación realizar, la cual es obtenida mediante el metodo **operar()**. la cual devuelve el nombre de la operación, luego de saber que operación realizar, obtiene los valores del lado derecho e izquierdo de las operacionesy retorna su valor.

Fragmento de la clase:

```python
class Aritmetica (Expression):

    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.right != None:
            rightValue = self.right.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma':

            resultado = leftValue+rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Resta':

            resultado = leftValue - rightValue

            return resultado

```

## Archivo interfaz.py

Como su nombre indica en este archivo se crea la interfaz grafica de la aplicación. Se crean las pantallas, los botones, labels, y cuadros de texto.

Fragmento del codigo:

```python
class Pantalla_principal():

    def __init__(self):
        self.pp = Tk()
        self.pp.title("Pantalla Principal | Proyecto 1")
        self.centrar(self.pp, 1000, 800)
        self.pp.configure(bg="#102027")
        self.pantalla_1()

    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        x = (anchura_pantalla//2)-(ancho//2)
        y = (altura_pantalla//2)-(alto//2)
        r.geometry(f"+{x}+{y}")

    def pantalla_1(self):
        self. Frame = Frame(height=500, width=1100)
        self.Frame.config(bg="#37474f")
        self.Frame.pack(padx=25, pady=25)
        self.text = ''
        posicionx1 = 480
        posicionx2 = 809
        self.analizado = False

        # encabezado de Archivo
        Label(self.Frame, text="Archivo", font=(
            "Roboto Mono", 24), fg="white",
            bg="#19A7CE", width=18, justify="center").place(x=405, y=0)
        # botones de Archivo
        Button(self.Frame, command=self.abrirArchivo, text="Abrir archivo", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=posicionx1, y=60)

```

Para llamra las funciones al presionar los botones se utilizan diferentes funciones.

Las diferentes funciones siguen la misma logica, llaman a funciones del archivo **analizador_lexico.py** para realizar las operaciones.

Si la operación se realiza correctamente se ejecutan las funciones definidas, en caso de que ocurra un error se muestra una ventana de error.

Esta abre el archivo que se selecciona en el explorador de archivos, y lo muestra en el cuadro de texto. Si ocurre un error al abrir el archivo, se muestra una ventana de error.
Ejemplo:

```python
def abrirArchivo(self):
        self.analizado = False
        x = ""
        self.archivo_seleccionado = ''
        Tk().withdraw()

        try:
            self.archivo_seleccionado = filename = askopenfilename(
                title="Seleccione un archivo", filetypes=[("Archivos txt", f"*.txt"), ("Archivos lfp", f"*.lfp"), ("All files", "*")])

            with open(filename, encoding="utf-8") as infile:
                x = infile.read()

            self.texto = x
            self.cuadroTexto.delete(1.0, "end")

            # set contenido
            self.cuadroTexto.insert(1.0, self.texto)

        except:
            messagebox.showerror(
                "Error", "Archivo no soportado")
            return

```

Todos las funciones siguen la misma logica.
