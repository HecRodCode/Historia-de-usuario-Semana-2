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
