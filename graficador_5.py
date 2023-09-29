import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ast import literal_eval
import string
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
import re


letras_alfabeticas = list(string.ascii_letters)

# Función para actualizar la gráfica y el grid
def actualizar_grafica():
    try:
        x_min = float(entry_x_min.get())
        x_max = float(entry_x_max.get())
        y_min = float(entry_y_min.get())
        y_max = float(entry_y_max.get())
        espaciado_grid = float(entry_espaciado.get())
        espaciado_grid_2 = float(entry_espaciado_2.get())

        # Actualizar los límites de los ejes
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        # Configurar el espaciado del grid
        ax.xaxis.set_major_locator(plt.MultipleLocator(base=espaciado_grid))
        ax.yaxis.set_major_locator(plt.MultipleLocator(base=espaciado_grid_2))

        # Dibujar las líneas del grid
        ax.grid(True)

        # Redibujar la gráfica
        canvas.draw()
    except ValueError:
        pass

# Función para graficar datos ingresados por el usuario
def graficar_datos():
    datos = entrada_datos.get()
    print(f' raw: {datos}')
    canastastr = []
    canastanum = []
    
    ## EJEMPLO A RECREAR
    ## das = [1,2,3], model = [1,4,9]

    def separar_cadenas(cadena):
        # Utilizar expresiones regulares para encontrar pares de palabras y listas
        patron = r'(\w+)\s*=\s*\[([\d\s,]+)\]'
        coincidencias = re.findall(patron, cadena)

        # Inicializar listas para almacenar las palabras y las listas correspondientes
        palabras = []
        listas = []

        for coincidencia in coincidencias:
            palabra = coincidencia[0].strip()
            lista = [int(x.strip()) for x in coincidencia[1].split(',')]
            palabras.append(palabra)
            listas.append(lista)

        return palabras, listas
    canastastr,canastanum = separar_cadenas(datos)
    print(canastastr,canastanum)
            
##    try:
    x = canastanum[0]
    y = canastanum[1]

    if len(canastastr) != len(canastanum):
        messagebox.showwarning("Advertencia", "Las listas no tienen la misma longitud.")
        

    # Verificar si la longitud de las listas es menor de 2 o impar
    if len(canastastr) < 2 or len(canastanum) % 2 != 0:
        messagebox.showerror("Error", "Los datos ingresados son insuficientes o impares.")
    
    # Limpiar la gráfica actual
    ax.clear()

    # Si no se cumplen las condiciones anteriores, graficar los datos
    # Aquí puedes agregar el código para generar la gráfica con Matplotlib
    # Por ejemplo:
    for i in range(int(len(canastanum)/2)):
        print(i)
        ax.plot(canastanum[2*i],canastanum[2*i+1], label=canastastr[2*i]+' vs '+canastastr[2*i+1])
    

    # Actualizar la leyenda y el título
    ax.legend()
    ax.set_title('Gráfica de Datos')

    # Actualizar la gráfica
    canvas.draw()

# Función para guardar la gráfica como una imagen
def guardar_grafica():
    archivo_guardado = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png"), ("Todos los archivos", "*.*")])
    if archivo_guardado:
        plt.savefig(archivo_guardado)
        print(f"Gráfica guardada en: {archivo_guardado}")

##    except (ValueError, SyntaxError):
##        print("Si hay error")
##        pass

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Gráfica con Control de Ejes, Espaciado del Grid y Entrada de Datos")

# Crear una figura de Matplotlib
figura = plt.figure(figsize=(6, 4))
ax = figura.add_subplot(111)

# Crear un lienzo para la gráfica en la interfaz de Tkinter
canvas = FigureCanvasTkAgg(figura, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0,column=0)

# Panel de control de ejes y espaciado del grid
panel_control = ttk.Frame(ventana)
panel_control.grid(row=1,column=0)
espaciados = ttk.Frame(ventana)
espaciados.grid(row=2,column=0)
# Etiquetas y Entrys para los límites de los ejes
ttk.Label(panel_control, text="X min:").grid(row=0, column=0)
ttk.Label(panel_control, text="X max:").grid(row=1, column=0)
ttk.Label(panel_control, text="Y min:").grid(row=0, column=2)
ttk.Label(panel_control, text="Y max:").grid(row=1, column=2)

entry_x_min = ttk.Entry(panel_control)
entry_x_max = ttk.Entry(panel_control)
entry_y_min = ttk.Entry(panel_control)
entry_y_max = ttk.Entry(panel_control)

entry_x_min.grid(row=0, column=1)
entry_x_max.grid(row=1, column=1)
entry_y_min.grid(row=0, column=3)
entry_y_max.grid(row=1, column=3)

# Etiqueta y Entry para el espaciado del grid X
ttk.Label(espaciados, text="Grid X:").grid(row=0, column=0, columnspan=4)
entry_espaciado = ttk.Entry(espaciados)
entry_espaciado.grid(row=0, column=1)

# Etiqueta y Entry para el espaciado del grid Y
ttk.Label(espaciados, text="Grid Y:").grid(row=1, column=0, columnspan=4)
entry_espaciado_2 = ttk.Entry(espaciados)
entry_espaciado_2.grid(row=1, column=1)

# Botón para actualizar la gráfica
boton_actualizar = ttk.Button(espaciados, text="Actualizar", command=actualizar_grafica)
boton_actualizar.grid(row=3, column=3)

# Botón para guardar la gráfica
boton_guardar = ttk.Button(espaciados, text="Guardar Gráfica", command=guardar_grafica)
boton_guardar.grid(row=3,column=0)

# Entrada de datos para la curva
ttk.Label(ventana, text="Ingrese datos de la curva:").grid(row=3,column=0)
entrada_datos = ttk.Entry(ventana, width=40)
entrada_datos.grid(row=4,column=0)
ttk.Button(espaciados, text="Graficar Datos", command=graficar_datos).grid(row=3,column=1)

# Ejecutar la aplicación
ventana.mainloop()
