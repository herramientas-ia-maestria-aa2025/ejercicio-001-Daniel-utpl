# Abrir y leer el archivo txt
def leer_archivo(informacion):
    try:
        with open(informacion, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{informacion}' no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", e)

# Ejecutar función
leer_archivo('informacion.txt')

