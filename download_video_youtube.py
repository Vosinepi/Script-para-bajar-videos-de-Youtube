import pytube  # importa la libreria pytube
from pytube.cli import on_progress  # importa la barra de progreso de pytube


location = "./"  # directorio de descarga. En este caso es el directorio actual


def download_video(url, filename=None):
    """
    Descarga el video de la URL dada y lo guarda en la ubicación especificada en la variable de
    ubicación

    :param url: La URL del video que desea descargar
    :param filename: El nombre del archivo a descargar (no utilizado en esta version)
    """

    try:
        video_instance = pytube.YouTube(
            url, on_progress_callback=on_progress
        )  # crea una instancia de YouTube con su barra de progreso

        print(
            f"\nDescargando video: {video_instance.title}"
        )  # imprime el titulo del video

        stream = (
            video_instance.streams.get_highest_resolution()
        )  # obtiene el stream de video de mayor resolución

        stream.download(location)  # descarga el video

        print(
            f"\nVideo descargado: {stream.default_filename}"
        )  # imprime el nombre del archivo descargado
    # Detectar cualquier excepción que pueda ocurrir e imprimir el mensaje de error.
    except Exception as e:
        print("error de descarga del video: " + str(url))
        print(e)


if __name__ == "__main__":
    video_url = input("Ingrese la url del video: ")  # solicita la url del video
    # Nombre_video = input("Ingrese el nombre del video(opcional): ")
    download_video(video_url)  # llama a la función de descarga de video
