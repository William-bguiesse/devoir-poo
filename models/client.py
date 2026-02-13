class Client:
    def __init__(self, id_client, nom, prenom, mail, telephone, adresse):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.telephone = telephone
        self.adresse = adresse

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.mail})"