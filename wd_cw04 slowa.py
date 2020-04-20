
print("zad6")

class Slowa:
    def __init__(self, wyraz1,wyraz2):
        self.wyraz1 = wyraz1
        self.wyraz2 = wyraz2
    def spr_czy_palindrom(self):
        r = self.wyraz1[::-1]
        if (self.wyraz1 == r):
            return "Wyraz jest palindromem."
        else:
            return "Wyraz nie jest palindromem."
    def spr_czy_metagramy(self):
            


slowo1 = Slowa("def","def")

print(slowo1.spr_czy_palindrom())
print(slowo1.spr_czy_metagramy())