
#Tupla carreras
carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

#Lista personas, donde más adelante se almacenarán los demás.
personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

#Aquí tenemos una lista que se utilizará más adelante, en el diccioanrio.
estudiantes = []


#for para repetir hasta 5, es decir, cuando se agregen las 5 personas, continuará con las demás indicaciones.
#Se definió cada variable con su tipo y se utilizó input para leer y almacenar los valores introducidos, de acuerdo a su variable.

for i in range(5):
    # Solicita los datos aquí
 
    print()
    prompt = f"Ingresa tu nombre:  "
    nombre = str(input(prompt))
    apellido = str(input("Ingrese apellido: "))
    edad = int(input("Ingrese edad: "))
    carrera = int(input("Ingrese carrera: pulse 0 para software, 1 para contabilidad, 2 para derecho. "))

    #La tupla con la variable student que tiene un índice de 3 de acuerdo a sus elementos.
    # Se utilizó .append para guardar la tupla student en la lista personas.
    student = (nombre, apellido, edad, carrera)
    personas.append(student)


#Otro bucle for que recorre los datos almacenados en almacenados en la lista personas.
#Utiliza una vaarible temporal que permite organizar los datos según su indice uno por uno.

for dts in personas: 
    nombre = dts[0]  
    apellido = dts[1]
    edad = dts[2] 
    #creacción de nueva variable para recorrer las carreras.
    carrera_choosen = dts[3]

    #Luego acá, en este diccionario se almacenan las informaciones.

    datos_estudiante = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad, 
    #Acá la lista carreras se guarda en la variable carrera_choosen, la cual tiene las carreras según el índice 0,1,2.
    "carrera": carreras[carrera_choosen] 
    }
    #luego que se cumple todo el proceso de lectura y almacenamiento,
    #Se utiliza .append para integrar hasta el último carácter a la lista estudiantes.
    estudiantes.append(datos_estudiante)


print("\n")

print("========= Estudiantes =========")
for est in estudiantes:
    print("\n")


    #La ultima parte, un bucle for que imprime todos los datos almacenados en la lista estudiantes que se imprimen según el número de agregado.
    #Con la variable est que representa cada estudiante mientras se recorre la lista.
    
    print(f"{est['nombre']} {est['apellido']} tiene {est['edad']} años y estudia {est['carrera']}") 