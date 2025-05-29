from entities.sistemas import Sistema
from Exceptions.EntidadYaExiste import EntidadYaExiste
from Exceptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste


def main():
    sistema = Sistema()

    while True:
        print ("Menu Principal:")
        print ("1. Registrar Cliente")
        print ("2. Registrar Pieza")
        print ("3. Registrar Máquina")
        print ("4. Registrar Orden")
        print ("5. Consultar Cliente")
        print ("6. Consultar Pieza")
        print ("7. Consultar Máquina")
        print ("8. Consultar Orden")
        print ("9. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo_cliente = input("Ingrese el tipo de cliente (1. Empresa | 2. Particular): ")
            if tipo_cliente == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                dni = input("Ingrese el DNI del cliente: ")
                try:
                    sistema.registrar_cliente_empresa(nombre, telefono, direccion, dni)
                    print("Cliente registrado exitosamente.")
                except EntidadYaExiste as e:
                    print(f"Error al registrar cliente: {e}")
            elif tipo_cliente == "2":
                nombre = input ("Ingrese el nombre de la empresa: ")
                telefono = input("Ingrese el teléfono de la empresa: ")
                direccion = input("Ingrese la dirección de la empresa: ")
        elif opcion == "2":
            nombre_pieza = input("Ingrese el nombre de la pieza: ")
            descripcion = input("Ingrese la descripción de la pieza: ")
            costo = float(input("Ingrese el costo de la pieza: "))
            cantidad_disponible = 0
            try:
                sistema.registrar_pieza(nombre_pieza, descripcion)
                print("Pieza registrada exitosamente.")
                sistema.registrar_costo_pieza(nombre_pieza, costo)
                print ("Costo de la pieza registrado exitosamente.")
                sistema.cantidad_pieza(nombre_pieza, cantidad_disponible)
                cantidad_disponible.append(cantidad_disponible)
            except ExceptionPiezaYaExiste as e:
                print(f"Error al registrar pieza: {e}")

