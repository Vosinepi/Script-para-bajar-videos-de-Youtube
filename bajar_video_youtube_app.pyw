from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox
import pytube


# variables
url_video = ""
carpeta_video = ""
tamaño_archivo = 0
archivo_en_bytes = 0


# ==========> FUNCIONAES

# ----------- Descarga de video -------------


def download_video(url, location=None):
    """
    Descarga el video de la URL dada y lo guarda en la ubicación especificada en la variable de
    ubicación

    :param url: La URL del video que desea descargar
    :param location: Ubicacion de descarga
    """
    global tamaño_archivo, archivo_en_bytes
    barra_progreso["value"] = 0
    print(f"carpeta_video: {carpeta_video}")

    if url == "":
        print("Por favor ingrese una URL")
        messagebox.showerror("Error", "Por favor ingrese una URL")
    elif carpeta_video == "":
        print("Por favor seleccione una carpeta")
        messagebox.showerror("Error", "Por favor seleccione una carpeta")
    else:
        try:
            video_instance = pytube.YouTube(
                url, on_progress_callback=progreso_descarga
            )  # crea una instancia de YouTube con su barra de progreso

            print(
                f"\nDescargando video: {video_instance.title}"
            )  # imprime el titulo del video
            descargando_label = Label(
                frame_textos, text=f"Descargando video: {video_instance.title}", pady=5
            )
            descargando_label.config(bg="#0D1117", fg="#C9D1CC")
            descargando_label.pack()

            # obtiene el stream de video de mayor resolución
            stream = video_instance.streams.get_highest_resolution()

            archivo_en_bytes = stream.filesize
            tamaño_archivo = archivo_en_bytes / 1024000

            stream.download(location)  # descarga el video

            # imprime el nombre del archivo descargado
            print(f"\nVideo descargado: {stream.default_filename}")

            video_descargado_label = Label(
                frame_textos, text=f"Video descargado 100%", pady=10
            )
            video_descargado_label.config(bg="#0D1117", fg="#C9D1CC")
            video_descargado_label.pack()

        # Detectar cualquier excepción que pueda ocurrir e imprimir el mensaje de error.
        except Exception as e:
            print("error de descarga del video: " + str(url))
            print(e)
            messagebox.showerror("Error", "Error de descarga del video")


# ----------- Seleccion de carpeta -------------


def select_location():
    """
    Crea una etiqueta que muestra la ruta a la carpeta que el usuario seleccionó.
    """
    global carpeta_video
    carpeta_video = rf"{filedialog.askdirectory()}"
    print(f"carpeta_video: {carpeta_video}")
    folder_label = Label(mi_frame, text=carpeta_video)
    folder_label.grid(row=1, column=1, padx=10, pady=10)
    folder_label.config(bg="#0D1117", fg="#C9D1CC")


# ----------- barra de progreso -------------


def progreso_descarga(stream, chunk, remaining):
    """
    Toma la secuencia, el fragmento y los bytes restantes como argumentos, y luego actualiza la barra de
    progreso con el porcentaje del archivo que se ha descargado.

    :param stream: El objeto de flujo
    :param chunk: el número de bytes descargados en el último fragmento
    :param remaining: El número de bytes que quedan para descargar
    """

    percent = (100 * (archivo_en_bytes - remaining)) / archivo_en_bytes
    barra_progreso["value"] += percent
    barra_progreso.update()

    print("{:00.0f}% downloaded".format(percent))


# ==========> INTERFAZ GRAFICA

# ------------- Tkinter Root y frames -----------------

root = Tk()
root.title("Descarga de videos de YouTube")
root.resizable(0, 0)
root.config(bg="#0D1117")
root.geometry("560x300")

mi_frame = Frame(root)
mi_frame.config(bg="#0D1117")
mi_frame.pack()

frame_textos = Frame(root, pady=10)
frame_textos.config(bg="#0D1117")
frame_textos.pack()

# ------------- Labels y entryes -----------------

titulo = Label(
    mi_frame,
    text="Ingrese la URL del video",
    font=("Arial", 10),
    fg="#C9D1CC",
    bg="#0D1117",
).grid(row=0, column=0, padx=10, pady=10)

url_video = Entry(mi_frame, width=50)
url_video.grid(row=0, column=1, padx=10, pady=10)
url_video.config(bg="#0D1117", fg="#C9D1CC", insertbackground="#C9D1CC")


titulo_location = Button(
    mi_frame, text="Seleccione la ubicación", command=select_location
)
titulo_location.grid(row=1, column=0, padx=10, pady=10)

# ------------- Botones -----------------

# Boton de salir
Button(mi_frame, text="Exit", command=root.destroy).grid(row=2, column=0)

# Boton de descarga
Boton_descarga = Button(
    mi_frame,
    text="Descargar",
    command=lambda: download_video(url_video.get(), carpeta_video),
)
Boton_descarga.grid(row=2, column=1)

# ------------- Barra de progreso GUI-----------------

barra_progreso = ttk.Progressbar(
    frame_textos, orient="horizontal", length=500, mode="determinate"
)
barra_progreso.pack()


root.mainloop()
