from random import randint

class Carte():

    Mazzo = {1:'Asso',2:'Due',3:'Tre',4:'Quattro',5:'Cinque',6:'Sei',7:'Sette'}


    def carta(self):
        car = self.Mazzo.get(randint(1,7))
        return car


Giovanni = Carte()
car = Giovanni.carta()
print("Carta : ", car)
