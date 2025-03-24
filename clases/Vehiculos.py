class Vehiculos():

    def __init__(self, marca, acelera)-> None:
        self.acelera=acelera
        self.marca= marca
        self.frena= True
        self.enMarcaha=True
    
    def arranca(self) -> bool:
        return False
    
    @classmethod
    def default(cls):
        return cls("Toyota", True)
    
    def imprimir(self)->None:
        print("marca: ", self.marca)
    
    

auto = Vehiculos("Renoalut", True)
auto.imprimir()


auto2 = Vehiculos.default()
auto2.imprimir()
