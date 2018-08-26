class Giocatore():

    def __init__(self, carta):
        self.carta = carta

    def setcarta(self, carta):
        self.carta = self.carta + carta

    def getcarta(self):
        return self.carta


sfidante = Giocatore(0)
val = sfidante.getcarta()
print("Valore iniziale carta: ", val)
print("Setta a 5 il valoredella carta")
sfidante.setcarta(5)
print("Valore carta: ", sfidante.getcarta())
