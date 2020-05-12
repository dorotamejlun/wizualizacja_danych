class Parzyste_Indeksy:
   def __init__(self, numer):
       self.numer = numer
   def __iter__(self):
       return self
   def __next__(self):
       for i in range (1,len(self.numer)):
            if i % 2 == 0:
                print(self.numer[i])

obiekt = Parzyste_Indeksy("01234567")
print(next(obiekt))
