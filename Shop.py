#Shop
#id, addressId, workingHours (dict)

class Shop:
    def __init__(self, id, addressID, workingHours):
        self.id = id
        self.addressID = addressID
        self.workingHours = workingHours
    def __str__(self):
        return f"{self.id}, {self.addressID}, {self.workingHours}"
    def __repr__(self):
        return f"{self.id}, {self.addressID}, {self.workingHours}"


eShop = Shop(100, "www.100.md", {"Mo": "9.00-15.00", "Tu": "9.00-15.00", "We": "9.00-15.00", "Th": "9.00-15.00", "Fr": "9.00-15.00"  })
print (eShop)
