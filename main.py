class Tortburchak:
    def __init__(self, uzunlik, kenglik):
        self.uzunlik = uzunlik
        self.kenglik = kenglik

    def yuza(self):
        return self.uzunlik * self.kenglik

    def perimetr(self):
        return 2 * (self.uzunlik + self.kenglik)


tort = Tortburchak(5, 3)
print("Yuza:", tort.yuza())         
print("Perimetr:", tort.perimetr()) 
