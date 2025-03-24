# ## Classes ###

class Persona:
    def __init__(self, name, surname, age, a):
        self.name = name
        self.surname = surname
        self.age = age
        self.a = a
        self.b = ""

my_person = Persona("sebas", "serrano",1 , 0)
print (my_person.surname)
print (my_person.b)
print(f"{my_person.name} {my_person.age}")

    



