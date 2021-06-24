#Shop
#id, addressId, workingHours (dict)
from Adress import Address

class Shop:
    def __init__(self, id, addressID, workingHours):
        self.id = id
        self.addressID = addressID
        self.workingHours = workingHours

    def __str__(self):
        return f"{self.id}, {self.addressID}, {self.workingHours}"

    def __repr__(self):
        return self.__str__()



