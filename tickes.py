import random, json, pickle
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

            with open ("ex.json", "r", encoding="UTF-8") as f:
                info=json.load(f)
        
            Ticket={
                "Nombre":input("ingrese su nombre: "),
                "Sector":input("ingrese su sector: "),
                "Asunto":input("Ingrese su asunto: "),
                "Mensaje":input("Ingrese un contexto: "),
                "N_Ticket": numero_random
            }
            info.append(Ticket)
            with open("ex.json", "w", encoding="UTF-8") as f:
                json.dump(info,f,ensure_ascii=False,indent=4)
                

            print("="*40)
            print("Se genero el siguiente Ticket".center(40))
            print("="*40)
            print(f" Su nombre: {Ticket['Nombre']}               N°Ticket: {numero_random} ")
            print(f" Sector: {Ticket['Sector']}\n Asunto: {Ticket['Asunto']} \n Mensaje: {Ticket['Mensaje']} \n\n Es importante que recuerde el número de Ticket")
            Pregunta=input(" Desea generar un nuevo Ticket? (s/n): ").lower()
            if Pregunta== "s":
                continue 
            else: 
                print("Gracias por usar el sistema")
                break
    elif Respuesta==2:
        while True:
            with open("ex.json", "r", encoding="UTF-8") as f:
                info= json.load(f)

                code_busqueda=int(input("Ingrese el codigo del ticket que busca: "))
                encontrado= False

                for ticket_guardado in info:
                    if ticket_guardado["N_Ticket"]== code_busqueda:
                        print("="*40)
                        print("Ticket encontrado".center(40))
                        print("="*40)
                        print(f"Nombre: {ticket_guardado['Nombre']}")
                        print(f"Sector: {ticket_guardado['Sector']}")
                        print(f"Asunto: {ticket_guardado['Asunto']}")
                        print(f"Mensaje: {ticket_guardado['Mensaje']}\n")
                        
                        encontrado=True
                        break
                if not encontrado : print("No fue encontrado ningun ticket con ese codigo")
                
                Pregunta2=(input("¿Desea leer otro Ticket (s/n)? ")).lower()
                if Pregunta2== "s": continue
                else: break
    else:
        if input("¿Está seguro de salir (s/n)? ").lower() =="s":
            break
        else: continue 
