#importo funzione random
from random import randint
class Classe ():
    '''class object: Classe, contiene essenzialmente l'orario'''
    def __init__(self):
        '''class init: crea matrice 5(giorni)x6(ore), inizializzata a False,
        usato per indicare se quell'ora è ancora "buca"'''
        self.or_cl=[[False, False, False, False, False, False],\
          [False, False, False, False, False, False],\
          [False, False, False, False, False, False],\
          [False, False, False, False, False, False],\
          [False, False, False, False, False, False]]
        
    
class Prof ():
    def __init__ (self):
        self.or_pr=[[False, False, False, False, False, False],\
          [False, False, False, False, False, False],\
          [False, False, False, False, False, False],\
          [False, False, False, False, False, False],\
          [False, False, False, False, False, False]] 
    def inizia (self, nome, oretot, opc, classiCheHa):
        self.nome=str(nome)
        self.otot=int(oretot)
        self.opc=int(opc)
        self.chi=list(classiCheHa)
    def assegnagenerale (self):
        for j in range(len(self.chi)-1):
            print (self.chi[j])
            #for i in range (self.opc):
               # giorno=randint(0,5)-1
                #ora=randint(0,6)-1
                #while item.or_cl[giorno][ora] != False and self.or_pr[giorno][ora] !=False:
                  #  giorno=randint(0,5)-1
                   # ora=randint(0,6)-1
                #item.or_cl[giorno][ora]=self.nome
                #self.or_pr[giorno][ora]=item

_1E=Classe()
_2E=Classe()
_4E=Classe()
tegon=Prof()
tegon.inizia("A. Tegon", 18, 6, [_1E, _2E, _4E])
tegon.assegnagenerale()

'''
print ("l'orario della classe 1E per ora e': \n" )
print (_1E.or_cl[0], "\n", _1E.or_cl[1], "\n", _1E.or_cl[2], "\n", _1E.or_cl[3], "\n", _1E.or_cl[4], "\n" )
print ("l'orario della classe 2E per ora e': \n" )
print (_2E.or_cl[0], "\n", _2E.or_cl[1], "\n", _2E.or_cl[2], "\n", _2E.or_cl[3], "\n", _2E.or_cl[4], "\n" )
print ("l'orario della classe 1E per ora e': \n" )
print (_4E.or_cl[0], "\n", _4E.or_cl[1], "\n", _4E.or_cl[2], "\n", _4E.or_cl[3], "\n", _4E.or_cl[4], "\n" )
print ("l'orario del prof Tegon per ora e': \n" )
print (tegon.or_pr[0], "\n", tegon.or_pr[1], "\n", tegon.or_pr[2], "\n", tegon.or_pr[3], "\n", tegon.or_pr[4], "\n" )
'''
