7iimport funtions
import data
import os

# Loop menu inical
while True:
    funtions.restart()
    funtions.main_menu()
    
    try:
        option = int(input("Ingrese una opción:"))
    except ValueError:
        print("\n--Ingrese una opción valida.--")
        continue
    
    #Loop menú de gestión de inventario
    match option:
        case 1:
            while True:
                funtions.restart()
                funtions.product_menu()

                try:
                    option1 = int(input("Ingresa una opción:"))
                except ValueError:
                    print("\n-- Ingresa una opción valida:")
                    continue

                match option1:
                    case 1:
                        funtions.add_product_loop()
                    case 2:
                        funtions.delete_product_loop()
                    case 3:
                        break
        case 2:
            funtions.show_inventory()
        case 3:
            funtions.stats_menu()
        case 4:
            funtions.exit_menu()
            exit()
            break

# 1. Definición del Diccionario/Lista
# Utilizamos una Lista [] que contiene Diccionarios {} (cada diccionario es un libro)
libros_inventario = [
    {
        "Title": "Cien Años de Soledad",
        "Author": "Gabriel García Márquez",
        "Price": 15500,
        "ISBN": "978-0307474278"
    },
    {
        "Title": "El Principito",
        "Author": "Antoine de Saint-Exupéry",
        "Price": 9800,
        "ISBN": "978-3791550117"
    },
    {
        "Title": "Libro Ejemplo",
        "Author": "bbhuu",
        "Price": 12344,
        "ISBN": "978-1234567890"
    }
]

# 2. Obtener la Búsqueda del Usuario
nombre_buscado = input("📚 Ingrese el nombre exacto del libro que desea buscar: ")
print("\n") # Salto de línea para mejor presentación

# Variable para rastrear si encontramos el libro
libro_encontrado = None

# 3. Iniciar el Ciclo for para Recorrer la Lista
# Recorremos cada diccionario individual (cada 'libro') dentro de la lista 'libros_inventario'.
for libro in libros_inventario:
    # 4. Condición de Búsqueda
    # Comprobamos si el valor de la clave "Title" en el diccionario actual coincide con la búsqueda del usuario.
    if libro["Title"].lower() == nombre_buscado.lower():
        libro_encontrado = libro  # Guardamos la referencia al diccionario encontrado
        break # ¡Muy importante! Salimos del ciclo 'for' inmediatamente una vez que encontramos el libro.

# 5. Imprimir la Información
if libro_encontrado:
    print(f"--- ✅ ¡Libro Encontrado! Información de '{libro_encontrado['Title']}' ---")
    
    # Usamos un SEGUNDO ciclo 'for' para recorrer e imprimir todas las claves y valores
    # (Author, Price, ISBN, etc.) del diccionario del libro.
    for clave, valor in libro_encontrado.items():
        print(f"**{clave}:** {valor}")
    
    print("--------------------------------------------------")
else:
    # Si el ciclo 'for' principal termina sin encontrar el libro.
    print(f"❌ Lo siento, el libro '{nombre_buscado}' no se encontró en el inventario.")

# 1. Definición del Diccionario/Lista (misma estructura)
libros_inventario = [
    {
        "Title": "Cien Años de Soledad",
        "Author": "Gabriel García Márquez",
        "Price": 15500,
        "ISBN": "978-0307474278"
    },
    {
        "Title": "El Principito",
        "Author": "Antoine de Saint-Exupéry",
        "Price": 9800,
        "ISBN": "978-3791550117"
    },
    {
        "Title": "Libro Ejemplo",
        "Author": "bbhuu",
        "Price": 12344,
        "ISBN": "978-1234567890"
    }
]

# 2. Obtener la Búsqueda del Usuario
nombre_a_eliminar = input("🔥 Ingrese el nombre del libro que desea ELIMINAR: ")
print("\n")

# Variables para rastrear el índice y el estado
indice_a_eliminar = -1 # Usamos -1 como valor inicial para indicar que no se encontró
libro_encontrado_info = None

# 3. Ciclo for para Encontrar el Libro y su Posición (Índice)
# Usamos enumerate() para obtener el índice y el diccionario del libro en cada iteración.
for i, libro in enumerate(libros_inventario):
    if libro["Title"].lower() == nombre_a_eliminar.lower():
        indice_a_eliminar = i
        libro_encontrado_info = libro
        break # Detenemos la búsqueda

# 4. Proceso de Confirmación y Eliminación
if indice_a_eliminar != -1:
    print(f"--- ⚠️ Se encontró el libro '{libro_encontrado_info['Title']}' ---")
    
    # Imprimir la información que se va a eliminar
    for clave, valor in libro_encontrado_info.items():
        print(f"**{clave}:** {valor}")
        
    # Pedir confirmación al usuario
    confirmacion = input("\n¿Está seguro de que desea eliminar este libro? (escriba 'SÍ' para confirmar): ").upper()
    
    if confirmacion == "SÍ":
        # Usamos el método pop() de la lista con el índice encontrado
        libros_inventario.pop(indice_a_eliminar)
        print(f"\n✅ El libro '{nombre_a_eliminar}' y su información han sido **eliminados**.")
    else:
        print("\n❌ Eliminación cancelada por el usuario.")
else:
    # Si el ciclo 'for' principal termina sin encontrar el libro.
    print(f"❌ Lo siento, el libro '{nombre_a_eliminar}' no se encontró en el inventario.")
    
# Opcional: Imprimir el inventario restante para verificar la eliminación
print("\n--- Inventario Actualizado ---")
for libro in libros_inventario:
    print(f"- {libro['Title']}")
print("----------------------------")

