#Validacion de una ip

def validar_ip(direccion_ip):
    try:
        octetos = list(map(int, direccion_ip.split('.')))
    except ValueError:
        return False

    if len(octetos) == 4 and all(0 <= octeto <= 255 for octeto in octetos):
        return True
    else:
        return False

while True:
    direccion_ingresada = input("Ingrese una dirección IP: ")

    if validar_ip(direccion_ingresada):
        confirmacion = input(f"Ha ingresado la dirección IP: {direccion_ingresada}. Su ip es correcta")
        break
    else:
        print("La entrada no es una dirección IP válida. Inténtelo de nuevo.")
