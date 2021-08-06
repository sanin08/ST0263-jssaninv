#import socket
from socket import socket

def Main():
    
    mySocket = socket()
    mySocket.connect( ('172.31.54.84', 3000) )

    directorio = "a"

    operacion = input(">")
    numero1 = input(">")
    numero2 = input(">")
    mensaje = ""

    while True:


        
        if operacion == "SUMA":
            print("Enviando:", numero1, "+", numero2)
            mensaje = "SUMA" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        elif operacion == "RESTA":
            print("Enviando:", numero1, "-", numero2)
            mensaje = "RESTA" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        elif operacion == "MULTIPLICACION":
            print("Enviando:", numero1, "*", numero2)
            mensaje = "MULTIPLICACION" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        elif operacion == "DIVICION":
            print("Enviando:", numero1, "/", numero2)
            mensaje = "DIVICION" + numero1 + "." + numero2
            mySocket.send(mensaje.encode())
            datos = mySocket.recv(1024).decode()
            print('El resultado es: ' + datos)

        else:
            mySocket.send(operacion.encode())
            datos = mySocket.recv(1024).decode()

            print(datos)
            

        operacion = input(">")
        if operacion == 'EXIT':
            mySocket.send(operacion.encode())
            datos = mySocket.recv(1024).decode()
            print(datos)
            break

        numero1 = input(">")
        numero2 = input(">")

    mySocket.close()

if __name__ == '__main__':
    print("• Primero elija la operación que desea realizar y luego digíte los dos números •")
    print("--------------|| OPERACIONES ||---------------")
    print("• Si quiere sumar:         SUMA")
    print("• Si quiere restar:        RESTA")
    print("• Si quiere una multiplicar:   MULTIPLICACION")
    print("• Si quiere dividir:       DIVICION")
    print("--------------------------------------")
    print("• Para salir escriba: EXIT")
    print("")
    Main()
    
