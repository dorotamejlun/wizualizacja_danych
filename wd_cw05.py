print("zad1")

class Material():
    def __init__(self):
        self.rodz = 'bawelna'
        self.dl = '2'
        self.szer = '1'
    def wyswietl_nazwe(self):
        return self.rodz,self.dl,self.szer

class Ubrania(Material):
    def __init__(self):
        super().__init__()
        self.rozm = 'S'
        self.kolor = 'szary'
        self.dla_kogo = 'K'
    def wyswietl_dane(self):
        return self.rozm,self.kolor,self.dla_kogo

class Sweter(Ubrania):
    def __init__(self):
        super().__init__()
        self.rodz = 'golf'
    def wyswietl_dane2(self):
        return self.rodz

ubrania = Ubrania()
sweter = Sweter()
print("Rodz swetra: ",sweter.wyswietl_dane2())
print("Dane: ", sweter.wyswietl_dane())
print("Material: ",ubrania.rodz)

