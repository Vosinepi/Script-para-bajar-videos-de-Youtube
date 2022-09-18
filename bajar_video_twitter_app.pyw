from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox

import yt_dlp

# ==========> VARIABLES
url_video = ""
carpeta_video = ""


# ==========> FUNCIONES

# ----------- Descarga de video ------------


def bajar_twitter(url_video, carpeta_video):
    """
    Descarga el video de la URL dada y lo guarda en la ubicación especificada en la variable de
    ubicación

    :param url_video: La URL del video que desea descargar
    :param carpeta_video: Ubicacion de descarga
    """

    if url_video == "":
        print("Por favor ingrese una URL")
        messagebox.showerror("Error", "Por favor ingrese una URL")

    elif carpeta_video == "":
        print("Por favor seleccione una carpeta")
        messagebox.showerror("Error", "Por favor seleccione una carpeta")

    else:
        try:
            ydl_ops = {"paths": {"home": carpeta_video}}
            with yt_dlp.YoutubeDL(ydl_ops) as ydl:
                ydl.download(url_video)

        except Exception as e:
            print("error de descarga del video: " + str(url_video))
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
    command=lambda: bajar_twitter(url_video.get(), carpeta_video),
)
Boton_descarga.grid(row=2, column=1)


root.mainloop()
