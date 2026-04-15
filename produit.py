class Produit:

    def __init__(self, nom, prix, description):
        self.nom = nom
        self.prix = prix
        self.description = description

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Prix :", self.prix)
        print("Description :", self.description)
        print("----------------------")

    def modifier_prix(self, nouveau_prix):
        self.prix = nouveau_prix

    def modifier_description(self, nouvelle_description):
        self.description = nouvelle_description


produit1 = Produit("Iphone 14 pro", 250000, "Smartphone")
produit2 = Produit("Casque Sony", 15000, "Casque sans fil")

print("AVANT MODIFICATION :")
produit1.afficher_infos()

produit1.modifier_prix(230000)
produit1.modifier_description("Smartphone - promotion")

print("APRES MODIFICATION :")
produit1.afficher_infos()