# [LFP]Proyecto1_202044192

## 1. DESCRIPCIÓN GENERAL

### 1.1 OBJETIVO GENERAL

Que el estudiante cree una herramienta la cual sea capaz de reconocer un lenguaje, dado por medio de un analizador léxico el cual cumple con las reglas establecidas, manejando la lectura
y escritura de archivos para el manejo de la información. A través de un entorno gráfico.

### 1.2 OBJETIVOS ESPECÍFICOS

- Implementar por medio de estados un analizador léxico.
- Utilizar funciones de manejo de cadenas de caracteres en lenguaje Python.
- Programar un Scanner para el análisis léxico.
- Construir un scanner basándose en un autómata finito determinístico.
- Crear una herramienta para interactuar de forma visual con el usuario con Tkinter

### 1.3 DESCRIPCIÓN

Se solicita la lectura de código fuente, el cual tendrá un formato JSON, creando un programa el
cual sea capaz de identificar un lenguaje dado, identificando los errores léxicos y ejecutando las
instrucciones correspondientes.

Se listarán una serie de instrucciones las cuales deben de ser ejecutadas, cumpliendo con el
formato asignado, generándolo un resultado y graficarlos en un archivo según la jerarquía
operacional de cada instrucción. **Colocando el resultado en cada nodo que aplique.**

Los errores deben ser generados en un archivo JSON.

## 2. CARACTERÍSTICAS DE LA SOLUCIÓN

Para responder a las necesidades que se le plantean, se ha pensado en el desarrollo de una
aplicación en lenguaje Python que permita reconocer las distintas instrucciones, y la ejecución
de las mismas. Con el objetivo que se implemente el análisis léxico correspondiente.

Se deben de mostrar de manera funcional y agradable al usuario resumen de errores
detectados, así como el resultado de las operaciones realizadas en cada una de las funciones
que se describen más adelante, así como su respectivo archivo en forma gráfica (árbol de
operaciones, incluyendo el resultado en cada nodo que aplique).

### 2.1 DISEÑO DE LA INTERFAZ

En la aplicación se deberán demostrar como mínimo los siguientes menús, tomando en cuenta
que deberá de ser totalmente gráfica.

- menú
- Ayuda
