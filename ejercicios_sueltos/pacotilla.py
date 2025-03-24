# Filtrando solicitudes
# El nombre debe empezar por mayúscula. Si es un nombre compuesto, entonces todos deben empezar por mayúscula.
# La edad debe ser mayor o igual a 16 y menor o igual a 40.
# El hobby indicado debe tener más de 10 caracteres.
# La casilla del sueño no puede haber sido dejada en blanco.

def validar_nombre(nombre: str) -> bool:
    palabras = nombre.split()
    return all(palabra[0].isupper() for palabra in palabras if palabra)
    
def validar_filtros() -> str:
  nombre = str(input("Ingrese su nombre: "))
  edad = int(input("Ingrese su edad: "))
  hobby = input("Ingrese su hobby: ")
  suenio = input("Ingrese su sueño: ")
  
  if (validar_nombre(nombre)):
    bandera_nombre = True
  else: bandera_nombre = False

  if (edad >= 16 and edad <= 40):
     bandera_edad = True
  else: bandera_edad = False

  if(len(hobby) > 10):
    bandera_hobby = True
  else: bandera_hobby = False
  
  if suenio is not None and suenio != "":
        bandera_suenio = True
  else: bandera_suenio = False

  if (bandera_nombre & bandera_edad & bandera_hobby & bandera_suenio):
     return "Aprobada"
  else: return "Rechazada"
    

      
  
print("La solicitud fue: ", validar_filtros())