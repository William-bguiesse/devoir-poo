import json

class DataManager:
    def sauvegarder(self, fichier, liste):
        donnees = [obj.to_dict() for obj in liste]
        with open(fichier, "w") as f:
            json.dump(donnees, f)

    def charger(self, fichier, classe):
        try:
            with open(fichier, "r") as f:
                return [classe.from_dict(d) for d in json.load(f)]
        except:
            return []

    def generer_id_reservation(self, reservations):
        if not reservations: 
            return "RES001"
        last_id = reservations[-1].id_reservation 
        num = int(last_id[3:]) + 1  
        return f"RES{num:03d}" 

    def filtrer_reservations_par_client(self, reservations, id_c):
        res_filtrees = []
        for r in reservations:
            if r.id_client == id_c:
                res_filtrees.append(r)
        return res_filtrees