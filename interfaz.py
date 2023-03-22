from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from analizador_lexico import instruccion, operar_


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
        self. Frame = Frame(height=500, width=700)
        self.Frame.config(bg="#37474f")
        self.Frame.pack(padx=25, pady=25)
        self.text = ''

        # encabezado de Archivo
        Label(self.Frame, text="Archivo", font=(
            "Roboto Mono", 24), fg="white",
            bg="#19A7CE", width=18, justify="center").place(x=0, y=0)
        # botones de Archivo
        Button(self.Frame, command=self.abrirArchivo, text="Abrir archivo", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=60, y=60)

        Button(self.Frame, text="Guardar", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=60, y=130)

        Button(self.Frame, text="Guardar como", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=60, y=200)

        Button(self.Frame, command=self.ejecutar, text="Analizar", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=60, y=270)

        Button(self.Frame, text="Errores", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=60, y=340)

        Button(self.Frame, command=self.pp.destroy, text="Salir", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=60, y=410)

        # encabezado de Ayuda
        Label(self.Frame, text="Ayuda", font=(
            "Roboto Mono", 24), fg="white",
            bg="#19A7CE", width=18, justify="center").place(x=350, y=0)

        # botones de Ayuda

        Button(self.Frame, text="Manual de usuario", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=14).place(x=350, y=60)

        Button(self.Frame, text="Manual técnico", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=14).place(x=350, y=130)

        Button(self.Frame, text="Temas de ayuda", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=14).place(x=350, y=200)

        # Text(self.Frame, font=(
        #     "Times New Roman", 15), fg="black", width=30, height=5).place(x=100, y=250)

        self.Frame.mainloop()

    def abrirArchivo(self):
        x = ""
        Tk().withdraw()

        try:
            filename = askopenfilename(
                title="Seleccione un archivo", filetypes=[("Archivos lfp", f"*.lfp"), ("All files", "*")])

            with open(filename, encoding="utf-8") as infile:
                x = infile.read()

        except:
            print("Error, no se ha seleccionado ningun archivo")
            return

        self.texto = x
        # print(self.texto)

    def ejecutar(self):
        instruccion(self.texto)
        respuestas = operar_()

        for respuesta in respuestas:
            print(respuesta.operar(None))


        # mostrar pantalla
r = Pantalla_principal()
