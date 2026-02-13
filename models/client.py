class Client:
    def __init__(self, id_client, nom, prenom, mail, telephone, adresse):
        self.id_client = id_client
        self.nom = str(nom)
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone
        self.adresse = adresse

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.mail})"
    
    def to_dict(self):
        return {
            "id_client": self.id_client,
            "nom": self.nom,
            "prenom": self.prenom,
            "mail": self.mail,
            "telephone": self.telephone,
            "adresse": self.adresse
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)