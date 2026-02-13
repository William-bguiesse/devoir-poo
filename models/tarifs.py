class TarifsManager:
    def __init__(self):
        self.prix_jours = {4: 30.0, 5: 50.0, 6: 80.0}
        self.prix_kms = {4: 0.5, 5: 0.7, 6: 1.1}

    def get_tarifs(self, cylindree):
        p_jour = self.prix_jours.get(cylindree, 0.0)
        p_km = self.prix_kms.get(cylindree, 0.0)
        return p_jour, p_km

    def __str__(self):
        return "Grille tarifaire : 4 cyl (30€/j), 5 cyl (50€/j), 6 cyl (80€/j)"