import random

_piedra='piedra'.lower();
_papel='papel'.lower();
_tijera='tijeras'.lower();
posibles=(_piedra,_papel,_tijera)

def quienGana(a,b):
  a=a.lower()
  b=b.lower()
  print(a)
  print(b)
  try:
    if (posibles.index(a)>=0) and (posibles.index(b)>=0):
      if (a==b):
        return 'Empate!'
      elif (a==_piedra and b==_tijera) or (a==_papel and b==_piedra) or (a==_tijera and b==_papel):
        return 'Ganaste!'
      else:
        return 'Perdiste!'
  except:      
    return '????'

if __name__== '__main__':
  # X=input('Jugador 1:')    
  ia=random.choice(posibles)
  yo=input('Eleccion:')    
  print(quienGana(yo,ia))
  