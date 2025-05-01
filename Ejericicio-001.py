# Abrir y leer el archivo txt
''' def leer_archivo(informacion):
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

'''
archivo = open("informacion.txt", "r")

lineas = archivo.readlines()
print(lineas)
print("-------------------")

lineas= [r.split(";") for r in lineas]

print(lineas)
print("-------------------")

for l in lineas:
    print(l)

print("-------------------")

lineas = lineas [1:]
for l in lineas:
    apellido = l[1]
    if apellido [0] == "B":
        print(l)