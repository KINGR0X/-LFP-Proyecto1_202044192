from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.filedialog import asksaveasfilename
from analizador_lexico import instruccion, operar_, generarGrafica, limpiarLista,  CrearArchivoErrores, limpiarListaErrores, lexemas_grafico
import os


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

        Button(self.Frame, command=self.guardar, text="Guardar", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=posicionx1, y=130)

        Button(self.Frame, command=self.guardarComo, text="Guardar como", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=posicionx1, y=200)

        Button(self.Frame, command=self.ejecutar, text="Analizar", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=posicionx1, y=270)

        Button(self.Frame, command=self.getErrores, text="Errores", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=posicionx1, y=340)

        Button(self.Frame, command=self.pp.destroy, text="Salir", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=12).place(x=posicionx1, y=410)

        # encabezado de Ayuda
        Label(self.Frame, text="Ayuda", font=(
            "Roboto Mono", 24), fg="white",
            bg="#19A7CE", width=18, justify="center").place(x=755, y=0)

        # botones de Ayuda

        Button(self.Frame, command=self.ManualUsuario, text="Manual de usuario", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=14).place(x=posicionx2, y=60)

        Button(self.Frame, command=self.ManualTecnico, text="Manual técnico", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=14).place(x=posicionx2, y=130)

        Button(self.Frame, command=self.TemasDeAyuda, text="Temas de ayuda", font=(
            "Roboto Mono", 20), fg="black",
            bg="white", width=14).place(x=posicionx2, y=200)

        self.cuadroTexto = scrolledtext.ScrolledText(self.Frame, font=(
            "Times New Roman", 15), fg='white', bg="#45545c", width=39, height=23)

        self.cuadroTexto.place(x=0, y=0)

        # self.scrollbar_x = Scrollbar(
        #     self.cuadroTexto, orient=HORIZONTAL, command=self.cuadroTexto.xview)

        # self.scrollbar_x.place(x=0, y=0)

        # self.cuadroTexto.config(xscrollcommand=self.scrollbar_x.set)

        self.Frame.mainloop()

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

            # # se separa el nombre del archivo en directorio y nombre
            # os.path.split(filename)
            # # se obtiene el nombre del archivo con la extension
            # self.filename = os.path.split(filename)[1]
            # # se obtiene el nombre del archivo sin la extension
            # self.filename = os.path.splitext(self.filename)[0]

            # Elimina contenido del cuadro
            self.cuadroTexto.delete(1.0, "end")

            # set contenido
            self.cuadroTexto.insert(1.0, self.texto)

        except:
            messagebox.showerror(
                "Error", "Archivo no soportado")
            return

    def ejecutar(self):
        # variable para saber si ya se presiono el boton de analizar
        self.analizado = True
        # En caso de que despues de analizar un arhivo se analice otro se limpian las listas
        limpiarListaErrores()
        limpiarLista()
        try:
            instruccion(self.texto)
            lexemas_grafico()
            operar_()
            generarGrafica(str("RESULTADOS_202044192"))

            # set contenido
            messagebox.showinfo("Analisis completado",
                                "Analisis realizado con exito, archivo .dot y .pdf generados")

        except:
            messagebox.showerror(
                "Error", "No se ha seleccionado ningún archivo")
            return

    def guardar(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")

            archivo = open(self.archivo_seleccionado, 'w', encoding="utf-8")
            archivo.write(self.texto)

            # mensaje de guardado
            messagebox.showinfo("Guardado", "Archivo guardado con exito")

        except:
            messagebox.showerror(
                "Error", "No se ha seleccionado ningún archivo")
            return

    def guardarComo(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")

            self.extensions = [("Archivos txt", f".txt"),
                               ("Archivos lfp", f".lfp"), ("All files", "*")]

            self.archivo_seleccionado = filename = asksaveasfilename(
                title="Seleccione un archivo", filetypes=[("Archivos txt", f".txt"), ("Archivos lfp", f".lfp"), ("All files", "*")], defaultextension=self.extensions, initialfile="Documento")

            archivo = open(self.archivo_seleccionado, 'w', encoding="utf-8")
            archivo.write(self.texto)

            # mensaje de guardado
            messagebox.showinfo("Guardado", "Archivo guardado con exito")

        except:
            messagebox.showerror(
                "Error", "No se ha seleccionado ningún archivo")
            return

    def getErrores(self):
        # Solo generamos los errores si ya se ha presionado el boton de analizar, porque si se presiona guardar sin analizar no se generan errores
        if (self.analizado == False):
            messagebox.showerror(
                "Error", "Para generar el archivo de errores primero debe de analizar el archivo")
            return
        try:
            CrearArchivoErrores()
            # mensaje de guardado
            messagebox.showinfo(
                "Guardado", "Archivo de errores generado con exito")
        except:
            messagebox.showerror(
                "Error", "No se ha podido generar el archivo de errores")
            return

    def ManualUsuario(self):
        try:
            # obtener direccion actual
            ruta = os.path.abspath("Manual_de_usuario.md")

            print(ruta)

            # se abre el archivo co Visual Studio Code
            os.system(f'code {ruta}')
        except:
            messagebox.showerror(
                "Error", "No se ha podido abrir el archivo, asegurese de tener instalado Visual Studio Code")
            return

    def ManualTecnico(self):
        try:
            # obtener direccion actual
            ruta = os.path.abspath("Manual_tecnico.md")

            print(ruta)

            # se abre el archivo co Visual Studio Code
            os.system(f'code {ruta}')
        except:
            messagebox.showerror(
                "Error", "No se ha podido abrir el archivo, asegurese de tener instalado Visual Studio Code")
            return

    def TemasDeAyuda(self):
        messagebox.showinfo(
            "Temas de ayuda", "Nombre: Elian Angel Fernando Reyes Yac\nCarnet: 202044192\nCurso:Lenguajes Formales y de Poramación\nSección: B+\n")

        # mostrar pantalla
r = Pantalla_principal()
