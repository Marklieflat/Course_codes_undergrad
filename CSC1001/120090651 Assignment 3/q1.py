class Flower:
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price
    
    def getName(self):
        return self.name

    def getPetals(self):
        return self.petals

    def getPrice(self):
        return self.price

    def setName(self, name):
        self.name = name
    
    def setPetals(self, petals):
        self.petals = petals

    def setPrice(self, price):
        self.price = price

def main():
    while True:
        try:
            name1 = input('Enter the name of the flower:')
            try:
                petals1 = int(input('Enter the petals of the flower:'))
                try:
                    price1 = float(input('Enter the price of the flower:'))
                    flower1 = Flower(name1,petals1,price1)
                    flower1.setName(name1)
                    flower1.setPetals(petals1)
                    flower1.setPrice(price1)
                    print("Flower's name is",flower1.getName())
                    print("The numbers of petals of the flower is",flower1.getPetals())
                    print("Flower's price is",flower1.getPrice())
                    return
                except:
                    print('Invalid input.Please try again!')
            except:
                print('Invalid input.Please try again!')
        except:
            print('Invalid input.Please try again!')

main()