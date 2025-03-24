nombre = input("🔹 Ingresa tu nombre: ")

def reclutando_tripulantes_aviso() :
    title = "se busca tripulante"
    message = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero. comida y bebida garantizada a lo largo de toda la aventura."
    contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino)."
    
    position = message.find(".")
    primer = message[0:position+1]
    segundo = message[position+1:len(message)].lstrip()
    print(title.upper() + "\n"+ primer.capitalize().replace("pyratilla", "PYRATILLA")+ "\n"+ segundo.capitalize().replace("pyratilla", "PYRATILLA") + "\n"+ contact.capitalize().replace("pyratilla", "PYRATILLA"))

def formulario_tripulacion():
    print("\n¡Bienvenido al formulario de reclutamiento del Capitán PYRATILLA! \n")
    
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    hobby = input("¿Cuál es tu hobby?: ")
    sueño = input("¿Cuál es tu mayor sueño?: ")

    print("\n¡Gracias por postularte a la tripulación de PYRATILLA! ")
    print(" Nombre:", nombre)
    print(" Edad:", edad)
    print(" Hobby:", hobby)
    print(" Sueño:", sueño)
    

#Llamo a las funciones
reclutando_tripulantes_aviso()
formulario_tripulacion()
