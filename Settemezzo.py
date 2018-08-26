from random import randint

'''
    CLASSE CARTE 
    METODO CARTA: RESTITUISCE UNA CARTA DA UNO A 7
'''

class Carte():

    Mazzo = {1:'Asso',2:'Due',3:'Tre',4:'Quattro',5:'Cinque',6:'Sei',7:'Sette'}


    def carta(self):
        val = randint(1,7)
        # car = self.Mazzo.get(val)
        print("Hai preso un: ", self.Mazzo.get(val))
        return val

'''

  CLASSE GIOCATORE
  METODO __INIT__ : INIZIALIZZA IL VALORE DELLA CARTA DEL GIOCATORE
  METODO SETCARTA : IMPOSTA IL VALORE DELLA CARTA
  METODO GETCARTA : RESTITUISCE IL TOTALE ACCUMULATO DAL GIOCATORE

'''

class Giocatore():

    def __init__(self, carta):
        self.carta = carta

    def setcarta(self, carta):
        self.carta = self.carta + carta

    def getcarta(self):
        return self.carta

'''
 
    CLASSE ENGINE
    METODO PLAY: INIZIA IL GIOCO, LO SFIDANTE PRELEVA UNA CARTA CON  "giu" FINO A TOTALIZZARE IL PUNTEGGIO MASSIMO  (7).
    SUCCESSIVAMENTE E' IL TURNO DEL BANCO. VINCE CHI SI AVVICINA DI PIU AL PUNTEGGIO MASSIMO, CHI SBALLA PERDE E A PARITA'
    DI PUNTO VINCE IL BANCO 

'''

class Engine():
    
    def play(self):

        Mazzo = Carte()
        sfidante = Giocatore(0)
        banco = Giocatore(0)
        
        carta = 'giu'

        print("\n" + '-' * 10 + " S F I D A N T E " + '-' * 10 + "\n")        
 
        while sfidante.getcarta() <= 7 :
            carta = input("giu x carta ?: ")
            if (carta != 'giu'):
                break
            sfidante.setcarta(Mazzo.carta())
            
    
        print("\n" + '-' * 10 + " B A N C O " + '-' * 10 + "\n")

        #banco.setcarta(Mazzo.carta())
        while (banco.getcarta() <= 7 and banco.getcarta() < sfidante.getcarta() and sfidante.getcarta() <= 7):
            banco.setcarta(Mazzo.carta())
        
        if (banco.getcarta() == 7 ):
            print("Banco vince!!!")
            exit(1)
        elif (banco.getcarta() > 7 and sfidante.getcarta() <= 7):
            print("Banco perde!")
            exit(1)
        else:
            print('-' * 10 + " S B A L L A T O !" + '-' * 10)  



mano = Engine()
mano.play() 
