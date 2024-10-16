class India():
    def capital(self):
        print("New delhi is the  capital of hagu")
    def language(self):
        print("Hindi is the most widely spoken language in india")
    
    def type(self):
        print("Ga theke gondho + developing country")

class Bd():
    def capital(self):
        print("Dhk is the capital of BD")
    def language(self):
        print("Bangla is the most widely spoken language in bd")

    def type(self):
        print("Beshirbhag noshu + developing country")

objInd = India()
objBd = Bd()

for country in (objInd, objBd):
    country.capital()
    country.language()
    country.type()
    print()