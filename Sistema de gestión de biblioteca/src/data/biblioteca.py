"""Libros y categorías almacenadas"""
from models.libro import Libro

# Lista de libros (usa esta estructura)
libros: list[Libro] = [
    {"titulo": "Cien años de soledad", "autor": "García Márquez",
        "paginas": 471, "disponible": True, "categoria": "Poesía"},
    {"titulo": "Don Quijote", "autor": "Cervantes",
        "paginas": 863, "disponible": False, "categoria": "Ficción"},
    {"titulo": "El principito", "autor": "Saint-Exupéry",
        "paginas": 96, "disponible": True, "categoria": "Ficción"},
    {"titulo": "1984", "autor": "George Orwell", 
     "paginas": 328, "disponible": True, "categoria": "Historia"},
    {"titulo": "Percy Jackson", "autor": "Rick Riordan", 
     "paginas": 350, "disponible": True, "categoria": "Ficción"},
    {"titulo": "Divergente", "autor": "Veronica Roth", 
     "paginas": 467, "disponible": False, "categoria": "Acción"}
    ]

# SET con las categorías disponibles
categorias = {"Ficción", "Ciencia", "Historia", "Poesía", "Acción"}
