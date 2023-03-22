import graphviz
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


# hay que convertir en string los argumentos antes
graficar("resta", 650, 5)
