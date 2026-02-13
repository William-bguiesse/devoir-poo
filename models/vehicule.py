class Vehicule:
    def __init__(self, id_vehicule, marque, modele, cylindree, kilometrage_actuel, date_mise_en_circulation):
        self.id_vehicule = str(id_vehicule)
        self.marque = marque
        self.modele = modele
        self.cylindree = int(cylindree)
        self.kilometrage_actuel = float(kilometrage_actuel)
        self.date_mise_en_circulation = date_mise_en_circulation

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.cylindree} cyl., {self.kilometrage_actuel} km)"
    
    def to_dict(self):
        return {
            "id_vehicule": self.id_vehicule,
            "marque": self.marque,
            "modele": self.modele,
            "cylindree": self.cylindree,
            "kilometrage_actuel": self.kilometrage_actuel,
            "date_mise_en_circulation": self.date_mise_en_circulation
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    