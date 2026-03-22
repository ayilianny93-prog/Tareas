# Importa tus módulos aquí

#Para opcion 1
from data.biblioteca import libros
from utils.operaciones import mostrar_disponibles

#Para opcion 2
from utils.operaciones import buscar_por_paginas

#para opcion 3
from utils.operaciones import contar_libros 
from utils.operaciones import promedio_paginas

#Para opcion 4
from utils.operaciones import agregar_categoria
categorias = set()


continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    print()

    if opcion == "1":
        # Llama a mostrar_disponibles()
        mostrar_disponibles(libros)
        pass

    elif opcion == "2":
        # Llama a buscar_por_paginas()

        max_paginas = 400
        buscar_por_paginas(libros, max_paginas)
        pass

    elif opcion == "3":
        # Llama contar_libros()

        cantidadLibros = contar_libros(libros)
        print("Cantidad de libros:", cantidadLibros)

        print()

        # Llama promedio_paginas()
        
        promedio = promedio_paginas(libros)
        print("El promedio de paginas es: ", promedio)
        pass
        # ... completa las demás opciones

    elif opcion == "4":
        nueva_categoria = str(input("Ingrese nueva categoria: "))
        agregar_categoria(categorias, nueva_categoria)
        print("Categoria añadida")


    elif opcion == "5":
        confirmacion = str(input("Desea cerrar la biblioteca? (aceptar / cancelar): "))

        if confirmacion == "aceptar":
            print("Biblioteca cerrada")
            break

        else:
            print("Regresando al menú...")