class Reservation:
    def __init__(self, id_reservation, id_client, id_vehicule, nb_jours, forfait_km, tarifs_manager, vehicule):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.nb_jours = int(nb_jours)
        self.forfait_km = int(forfait_km)
        
        p_jour, p_km = tarifs_manager.get_tarifs(vehicule.cylindree)
        
        self.cout_estime = (self.nb_jours * p_jour) + (self.forfait_km * p_km)

    def __str__(self):
        return f"Réservation {self.id_reservation}, Coût : {self.cout_estime}€"

    def to_dict(self):
        return {
            "id_reservation": self.id_reservation,
            "id_client": self.id_client,
            "id_vehicule": self.id_vehicule,
            "nb_jours": self.nb_jours,
            "forfait_km": self.forfait_km,
            "cout_estime": self.cout_estime
        }

    @classmethod
    def from_dict(cls, data):
        res = cls.__new__(cls)
        for key, value in data.items():
            setattr(res, key, value)
        return res