class Cat:

    def __init__(self, s, col, height, cry):
        self.numLegs = 4
        self.species = s
        self.color = col
        self.height = height
        self.cry = cry

    def getSpecies(self):
        return self.species

    def getColor(self):
        return self.color
    
    def getHeight(self):
        return self.height
    
    def getCry(self):
        return self.cry

    def setSpecies(self, s):
        self.species = s

    def setColor(self, col):
        self.color = col
        
    def setHeight(self, height):
        self.height = height

    def setCry(self, cry):
        self.cry = cry


def main():
    
    print("Hello! My favorite animal is...")
    
    cat1 = Cat("Siamese cat, ", "white, ", "26cm, ", "loud voice")
    cat2 = Cat("Persian cat, ", "white, ", "70cm, ", "no cry")
    cat3 = Cat("Abyssinian cat, ", "ruddy red, ", "50cm, ", "bell-like ringing cry")
    
    
    s = cat1.getSpecies()
    col = cat1.getColor()
    height = cat1.getHeight()
    cry = cat1.getCry()
    print(s, col, height, cry)
    
    s = cat2.getSpecies()
    col = cat2.getColor()
    height = cat2.getHeight()
    cry = cat2.getCry()
    print(s, col, height, cry)
    
    s = cat3.getSpecies()
    col = cat3.getColor()
    height = cat3.getHeight()
    cry = cat3.getCry()
    print(s, col, height, cry)
    
    
    

if __name__ == "__main__":
    main()
