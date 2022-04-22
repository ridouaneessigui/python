class Pizza:
    def __init__(self, nom, prix,ing,veg):
        self.nom = nom
        self.prix = prix
        self.ing = ing
        self.veg = veg

pizza1=Pizza("4fromage",20,"fgd","t")

print(pizza1.nom)
print(pizza1.prix)