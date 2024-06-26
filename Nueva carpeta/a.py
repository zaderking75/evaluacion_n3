import os,json

def limpiarpantalla():
    os.system('cls')

def menuprincipar():
    print("*********************************************************")
    print("*                   Mundo Libro                         *")
    print("*********************************************************")
    print("")
    print("1 - Mantenedor de categorias")
    print("2 - Reportes")
    print("3 - Salir")
    print("")

def submenu():
    print("*********************************************************")
    print("*                Mantenedor Categorias                  *")
    print("*********************************************************")
    print("")
    print("1 - Agregar Categoria")
    print("2 - Editar Categoria")
    print("3 - Eliminar Categoria")
    print("4 - Buscar Categoria")
    print("5 - Volver")
    print("")

def agregar_Categoria(nombre:str):
    with open("biblioteca.json",mode="r") as archivoJson:
        json.load(archivoJson)
        
        a = {
            "id":len(archivoJson["posicion"]+1),
            "nombre":nombre
        }

        nombreS = str(input("ingrese el nombre"))
        archivoJson["posicion"].append(categoria)
        a["nombre"].append(nombreS)

    with open("bibloteca.jon",mode="w") as estructuraJson:
        json.dump(archivoJson,estructuraJson,indent=4)


def Editar_Categoria(parid:int):
    with open("bibloteca.json",mode="r") as PasaJson:
        json.load(PasaJson)
        contador = 0
        for i in archivoJson["categoria"]:
            archivoJson["CategoriaID"]

            contador+=1
    with open("bibloteca.json",mode="w") as archivoJson:
        json.dump(archivoJson,PasaJson,indent=4)

    
    

def Eliminar_Categoria():
    categoria = categorias
    for i,categorias in categoria:
        del categoria[i]
        print(f"ha sido eliminado correctamente {archivoJson["categoria"]}")
        input("presione enter para regresar...")

def Buscar_Categoria():
    buscarid = int(input("ingrese la Id Correspondiente:"))




def Resp():
    limpiarpantalla()
    while True:
        submenu()
        opcion = int(input("Eliga su opcion: "))
        if opcion == 1:
            limpiarpantalla()
            agregar_Categoria()
        if opcion == 2:
            limpiarpantalla()
            Editar_Categoria()
        if opcion == 3:
            limpiarpantalla()
            Eliminar_Categoria()
        if opcion == 4:
            limpiarpantalla()
            Buscar_Categoria()
        if opcion == 5:
            break
        else:
            print("Opcion no valida")
            input("presione enter parareintentar ...")



def Reportes():

    print("*********************************************************")
    print("*     Libros       -     Cantidad de veces Prestadas    *")
    print("*********************************************************")

    libros = {
            "La Caza de Bernanda ALba": 2,
            "La Fiesta del Chivo":11,
            "Don Quijote de la Mancha":7,
            "La ciudad y los Perros":5
        }
    with open("Reportes_biblioteca_mundo_libro.json", mode="w") as leerJson:
                json.dump(libros,leerJson,indent=4)

    print("reporte hecho exitosamente")
    print(libros)
    input("presione enter para continuar")
        

def Respuesta():

    while True:
        limpiarpantalla()
        menuprincipar()
        opcion = int(input("Eliga su opcion: "))

        if opcion == 2:
            Reportes()
        if opcion == 3:
            break
        else:
            print("opcion no valida")
            input("presione enter para reintentar ...")

Respuesta()

#funciona sin la mayoria de codigos

        