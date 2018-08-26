from random import randint

class Carte():

    Mazzo = {1:'Asso',2:'Due',3:'Tre',4:'Quattro',5:'Cinque',6:'Sei',7:'Sette'}


    def carta(self):
        val = randint(1,7)
        car = self.Mazzo.get(val)
        print("Hai preso un: ",car)
        return val

Giovanni = Carte()
val = Giovanni.carta()
print("valore : ",val)
