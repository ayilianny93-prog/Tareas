from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros"""
    
    total_paginas = 0
    
    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)


def contar_libros(libros: list[Libro]):
    """Retorna la cantidad total de libros"""
    return len(libros)
    # Funciones que debes implementar
    
def mostrar_disponibles(lista_libros: list[Libro]):
    """Muestra solo los libros que están disponibles"""
    # Implementan la lógica aquí
    for libro in lista_libros:
        if libro["disponible"]:
            print(libro["titulo"])

    

def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    """Muestra libros con menos páginas que max_paginas"""
 # Implementan la lógica aquí

    for libro in lista_libros:
        if libro["paginas"] <= max_paginas:
             print(libro["titulo"], "-", libro["paginas"])
   
 
def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    """Agrega una nueva categoría al set"""
    # Implementan la lógica aquí
    set_categorias.add(nueva_categoria)

