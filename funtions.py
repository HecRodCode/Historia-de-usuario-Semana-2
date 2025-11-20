import os
import data

# Limpiar terminal
def restart():
    os.system('cls' if os.name == 'nt' else 'clear')

# Diseño de menu principal
def main_menu():
    print("""
0==========================================0
|                                          |
|              Menú principal              | 
|                                          |
|------------------------------------------|
|                                          |
|   [1] Gestión de inventario              |
|   [2] Mostrar Inventario                 |
|   [3] Calcular estadisticas              |
|   [4] Salir                              |
|                                          |
0==========================================0
""")

# Diseño para agregar o eliminar un producto
def product_menu():
    print("""
0==========================================0
|                                          |
|          Gestión de inventario           |
|                                          |
|------------------------------------------|
|                                          |
|  [1] Agregar un producto                 |
|  [2] Eliminar un producto                |
|  [3] Salir al menú principal             | 
|                                          |
0==========================================0
""")

# Diseño para agregar un producto
def add_product_menu():
    print("""
0==========================================0
|                                          |
|             Agregar producto             |
|                                          |
|------------------------------------------|
|                                          |
|  >> Nombre del producto:                 |
|  >> Cantidad del producto:               |
|  >> Precio del producto:                 | 
|                                          |
|  [4] Salir al menú de opciones           |
|                                          |
0==========================================0
""")

# Diseño para eliminar un producto
def delete_menu():
    print("""
0==========================================0
|                                          |
|           Eliminar un producto           |
|                                          |
|------------------------------------------|
|                                          |
|  >> Nombre del producto a eliminar:      |
|                                          |
|  [4] Salir al menú de opciones           |               
|                                          |
0==========================================0
""")
    
# Diseño para salir del programa
def exit_menu():
    print("""
0==========================================0
|                                          |
|             ¡Hasta luego!                |
|                                          |
0==========================================0
""")

# Loop para agregar productos
def add_product_loop():
    restart()
    add_product_menu()
    while True:

        # Pedimos al usuario los datos del producto
        try:
            add_product = input("Ingrese el nombre del producto a agregar:")
            quiantity_product = int(input("Ingrese la cantidad del producto:"))
            price_product = int(input("Ingrese el precio del producto:"))
        except ValueError:
            print("\nIngrese datos validos:")
        

        data.products[add_product] = {
            "Cantidad": quiantity_product,
            "Precio": price_product
        }
        print("\n¡Producto agregado correctamente")
        input("--Presione Enter para continuar ")
        break

# Loop para eliminar un producto
def delete_product_loop():
    restart()
    delete_menu()
    while True:

        # Preguntamos el nombre del producto a eliminar
        try:
            delete_product = input("Ingrese el nombre del producto a eliminar:")
        except ValueError:
            print("\n--Ingrese una opción valida--")
        
        if delete_product in data.products:
            datos = data.products[delete_product]

            # Mostramos estadisticas del producto, y preguntamos al usuario si esta seguro de que quiere eliminar este producto
            print(f"\n Producto: {delete_product} | Cantidad: {datos["Cantidad"]} | Precio: {datos["Precio"]} |")
            delete_confirmation = input(f"¿Estas seguro que deseas eliminar este producto?: {delete_product} (Si/No)").lower()


            if delete_confirmation == "si":
                del data.products[delete_product]

                print("\n/---Producto eliminado correctamente---/")
                input("\n/---Presione enter para volver al menu de Gestión---/")
                break

            elif delete_confirmation == "no":
                break
        else:
            print("\n/---Este producto no existe---/")


# Ciclos for para mostrar el contenido del inventario
def show_inventory():
    restart()
    while True:

        # Mensaje por si el inventario esta vacio
        if not data.products:
            print("""
0==========================================0
|                                          |
|        El inventario esta vacio          |
|                                          |
0==========================================0
""")
            input("\n/---Presiona Enter para volver al menu principal---/")
        
        # Si el inventario tiene elementos, mostrarlos de manera ordenada
        else:
            print("""
0==========================================0      
|                                          |     
|                Inventario                |
|                                          |
0==========================================0
      Producto  |  Cantidad  |  Precio
""") 
        for nombres, datos in data.products.items():
            print(f"       {nombres:<7}  | {datos["Cantidad"]:^10} | {datos["Precio"]:^8}")
            input("\n--Presione Enter para continuar--")
        break

# Ciclos for para calcular estadisticas de inventario
def stats_menu():
    restart()
    while True:
        print("""
0==========================================0
|                                          |
|          Calcular estadisticas           |
|                                          |
0------------------------------------------0
""")
        
        total = 0
        for nombres, datos in data.products.items():
            subtotal = datos["Cantidad"] * datos["Precio"]
            total += subtotal
        print(f"  >>  Valor del inventario: {total}")

        total_cantidad = 0
        for nombres, datos in data.products.items():
            cantidad = datos["Cantidad"]
            total_cantidad += cantidad
        print(f"  >>  Cantidad de productos: {total_cantidad}")

        input("\n--Dale enter para continuar--")
        break