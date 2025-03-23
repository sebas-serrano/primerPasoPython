class Coche():

    def __init__(self) -> None:
        self.largoChasis = 2
        self.anchoChasis = 3
        self.__rueda=4
        self.enMarcha=False
        self.color="marron"

    def get_rueda(self) -> int:
        return self.__rueda

    def suma_ruedas(self) -> int:
        return self.color

    

coche = Coche();
#print(coche.get_rueda())
print(coche.suma_ruedas())

#coche.rueda=3
#print(coche.rueda)