import random
import string

def RandomPasswordGenerator(l):
  res=''
  for i in range(l-1):
    if i % 3 == 1:
      res=res + random.choice(string.ascii_letters)
    elif i % 3 == 2:  
      res=res + random.choice(string.digits)
    else:
      res=res + random.choice(string.punctuation)
  return res          


if __name__== '__main__':
  print(RandomPasswordGenerator(6))
  print(RandomPasswordGenerator(7))
  print(RandomPasswordGenerator(12))
  
    