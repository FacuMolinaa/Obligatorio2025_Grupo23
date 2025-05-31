from entities.sistemas import Sistema
from entities.cliente import Cliente
from entities.Maquina import Maquina
from entities.Piezas import Pieza
from entities.Requerimiento import Requerimiento
from entities.Pedido import Pedido
from Exceptions.EntidadYaExiste import EntidadYaExiste
from Exceptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste


def main():
    sistema = Sistema()

    while True:
        print ("Menu Principal:")
        print ("==================================")
        print ("============ Menú Registrar ============")
        print ("1. Registrar Cliente | Empresa.")
        print ("1.1 Registrar Pieza")
        print ("1.2 Registrar Máquina")
        print ("1.3 Registrar Orden")
        print(" ============ Menú Listar ============")
        print ("2.1 Listar Clientes")
        print ("2.2 Listar Piezas")
        print ("2.3 Listar Máquinas")
        print ("2.4 Listar Órdenes")
        print ("3. Consultar Clientes")
        print ("4. Salir")
        print ("===================================")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo_cliente = input("Ingrese el tipo de cliente (1. Empresa | 2. Particular): ")
            if tipo_cliente == "2":
                nombre = input("Ingrese el nombre del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                dni = input("Ingrese el DNI del cliente: ")
                try:
                    cliente = Cliente(nombre, telefono, direccion, dni)
                    print("Cliente registrado exitosamente.")
                except EntidadYaExiste as e:
                    print(f"Error al registrar cliente: {e}")
            elif tipo_cliente == "1":
                nombre = input ("Ingrese el nombre de la empresa: ")
                telefono = input("Ingrese el teléfono de la empresa: ")
                direccion = input("Ingrese la dirección de la empresa: ")
                correo = input("Ingrese el correo de la empresa: ")
                try:
                    cliente = Cliente(nombre = nombre, telefono = telefono, direccion = direccion, correo=correo)
                    print("Empresa registrada exitosamente.")
                except EntidadYaExiste as e:
                    print(f"Error al registrar empresa: {e}")
        elif opcion == "1.1":
            nombre_pieza = input("Ingrese el nombre de la pieza: ")
            descripcion = input("Ingrese la descripción de la pieza: ")
            costo = float(input("Ingrese el costo de la pieza: "))
            cantidad_disponible = int(input("Ingrese la cantidad disponible de la pieza: "))
            try:
                registrar_pieza = []
                pieza = Pieza(descripcion=descripcion, costo=costo, nombre_pieza=nombre_pieza, cantidad_disponible=cantidad_disponible, registrar_pieza=registrar_pieza, listar_piezas=[])
                pieza.registrar_pieza.append(pieza)
                print("Pieza registrada exitosamente.")
            except ExceptionPiezaYaExiste as e:
                print(f"Error al registrar pieza: {e}")
                return
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == "1.2":
            id_maquina = input ("Ingrese el ID de la máquina: ")
            disponibilidad_maquina = input("Ingrese la disponibilidad de la máquina (Disponible/No Disponible): ")
            if disponibilidad_maquina.lower() == "disponible":
                disponibilidad_maquina = True
            else:
                disponibilidad_maquina = False
        elif opcion == "1.3":
            id_pedido = input("Ingrese el ID del pedido: ")
            id_cliente = input("Ingrese el ID del cliente: ")
            id_maquina = input("Ingrese el ID de la máquina: ")
            id_pieza = input("Ingrese el ID de la pieza: ")
            cantidad_pieza = int(input("Ingrese la cantidad de piezas: "))
            try:
                sistema.registrar_pedido(id_pedido, id_cliente, id_maquina, id_pieza, cantidad_pieza)
                print("Pedido registrado exitosamente.")
            except Exception as e:
                print(f"Error al registrar pedido: {e}")

        elif opcion == "2.1":
            clientes = sistema.listar_clientes()
            if clientes:
                print("Clientes registrados: ", (clientes))
                for cliente in clientes:
                    print(cliente)
            else:
                print("No hay clientes registrados.")

        elif opcion == "2.2":
            piezas = piezas.listar_piezas()
            if piezas:
                print("Piezas registradas:")
                for pieza in piezas:
                    print(pieza)
            else:
                print("No hay piezas registradas.")
        
        elif opcion == "2.3":
            maquinas = sistema.listar_maquinas()
            if maquinas:
                print("Máquinas registradas:")
                for maquina in maquinas:
                    print(maquina)
            else:
                print("No hay máquinas registradas.")
        
        elif opcion == "2.4":
            pedidos = sistema.listar_pedidos()
            if pedidos:
                print("Órdenes registradas:")
                for pedido in pedidos:
                    print(pedido)
            else:
                print("No hay órdenes registradas.")
        
        elif opcion == "3":
            id_cliente = input("Ingrese el ID del cliente a consultar: ")
            cliente = sistema.consultar_cliente(id_cliente)
            if cliente:
                print("Cliente encontrado:")
                print(cliente)
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            pass

if __name__ == "__main__":
    main()


