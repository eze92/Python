import pickle, sys, os, random

def alta_ticket():
    while True:
        print("Ingrese los datos para generar un nuevo ticket")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")
        
        # Generar número de ticket aleatorio entre 1000 y 9999
        numero_ticket = random.randint(1000, 9999)
        
        # Mostrar el ticket generado
        print("********************************")
        print("Se genero el siguiente ticket:")
        print("********************************")
        print("N° Ticket:", numero_ticket)
        print("Nombre:", nombre)
        print("Sector:", sector)
        print("Asunto:", asunto)
        print("Problema:", problema)

        
        # Mensaje recordatorio
        input("Por favor, acuérdese del número de ticket. Presione Enter para confirmar...")
        
        # Guardar el ticket en un archivo pickle
        guardar = f"ticket_{numero_ticket}.pkl"
        if not os.path.isfile(guardar):
            with open(guardar, "wb") as f:
                pickle.dump({
                    "numero": numero_ticket,
                    "nombre": nombre,
                    "sector": sector,
                    "asunto": asunto,
                    "problema": problema
                }, f)
        
        # Preguntar si se desea crear otro ticket
        crear_otro_ticket = input("¿Desea crear otro ticket? (s/n): ")
        if crear_otro_ticket.lower() != 's':
            break  # Salir del bucle si la respuesta no es 's'

def leer_ticket():
    while True:
        numero_ticket = input("Número de ticket a leer: ")
        
        # Leer el ticket desde el archivo pickle
        abrir = f"ticket_{numero_ticket}.pkl"
        if os.path.isfile(abrir):
            with open(abrir, "rb") as f:
                ticket = pickle.load(f)
                
                # Mostrar el ticket almacenado
                print("\nTicket almacenado:")
                print("Número de Ticket:", ticket["numero"])
                print("Nombre:", ticket["nombre"])
                print("Sector:", ticket["sector"])
                print("Asunto:", ticket["asunto"])
                print("Problema:", ticket["problema"])
                
                # Preguntar si se desea leer otro ticket
                leer_otro_ticket = input("¿Desea leer otro ticket? (s/n): ")
                if leer_otro_ticket.lower() != 's':
                    break  # Salir del bucle si la respuesta no es 's'
        else:
            print("El número de ticket especificado no existe.")
        
def menu():
    while True:
        os.system("cls")  # Limpiar la terminal
        print("Bienvenido al sistema de tickets")
        print("Menú:")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            confirmacion = input("¿Está seguro que desea salir? (s/n): ")
            if confirmacion.lower() == 's':
                print("¡Hasta luego!")
                sys.exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida. Presione ENTER para continuar")
            input()

if __name__ == "__main__":
    menu()
