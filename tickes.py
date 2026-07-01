import random, sys, os
while True:
    print ("""Hola bienvenido al sistema de Tickes \n
    1. Generar un nuevo ticke 
    2. leer el Ticket 
    3. Salir """
    )
    Respuesta=(int(input("Elija una opción= ")))
    if Respuesta==1:
    
        while  True:
            numero_random=random.randrange(1000, 9999)
            print("ingrese los datos para Generar un nuevo Ticket")
            Nombre=input("ingrese su nombre: ")
            Sector=input("ingrese su sector: ")
            Asunto=input("Ingrese su asunto: ")
            Mensaje=input("Ingrese un contexto: ")
            print("="*40)
            print("Se genero el siguiente Ticket".center(40))
            print("="*40)
            print(f" Su nombre: {Nombre}               N°Ticket: {numero_random}\n sector: {Sector}\n Asunto: {Asunto} \n Mensaje: {Mensaje} \n\n Es importante que recuerde el número de Ticket ")
            Pregunta=input(" Desea generar un nuevo Ticket? (s/n): ").lower()
            if Pregunta== "s":
                continue 
            else: 
                print("Gracias por usar el sistema")
                break
    elif Respuesta==2: