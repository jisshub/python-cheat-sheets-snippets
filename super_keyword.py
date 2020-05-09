class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    # Here, we called the __init__() method of the Mammal class (from the Dog class) using code
    super().__init__('Dog')
  
#create a instance of dog class - no need of passing argument mammalName 
d1 = Dog()
