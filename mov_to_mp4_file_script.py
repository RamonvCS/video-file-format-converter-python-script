# Importación de las librerías necesarias
import ffmpeg
import sys

def convert_mov_to_mp4(input_file, output_file):
    """
    Convierte un archivo .mov a formato .mp4 con codecs específicos para compatibilidad.
    
    :param input_file: Ruta al archivo de entrada .mov.
    :param output_file: Ruta al archivo de salida .mp4.
    """
    try:
        # Usar ffmpeg para convertir el archivo con codecs específicos
        ffmpeg.input(input_file).output(output_file, vcodec='libx264', acodec='aac', strict='experimental').run(overwrite_output=True)
        print(f"Archivo {input_file} convertido exitosamente a {output_file}")
    except ffmpeg.Error as e:
        # Imprimir el error específico de ffmpeg
        print(f"Error al convertir el archivo: {e}")
    except Exception as e:
        # Imprimir cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    # Verificar si se ha proporcionado el número correcto de argumentos
    if len(sys.argv) != 3:
        # Imprimir las instrucciones de uso si los argumentos son incorrectos
        print("Uso incorrecto del script.")
        print("Asegúrate de proporcionar los archivos de entrada y salida.")
        print("Formato de uso correcto: python mov_to_mp4_file_script.py <archivo_entrada.mov> <archivo_salida.mp4>")
        print("Ejemplo: python mov_to_mp4_file_script.py video.mov video.mp4")
        sys.exit(1)

    # Obtener las rutas de los archivos de entrada y salida desde los argumentos de la línea de comandos
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Llamar a la función de conversión
    convert_mov_to_mp4(input_file, output_file)
