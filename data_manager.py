import json

class DataManager:
    def sauvegarder(self, fichier: str, liste: list):
        """Enregistre la liste d'objets dans un fichier JSON."""
        try:
            donnees = [obj.to_dict() for obj in liste]
            with open(fichier, "w") as f:
                json.dump(donnees, f, indent=4)
        except:
            print("Erreur : Impossible d'enregistrer le fichier !")

    def charger(self, fichier: str, classe) -> list:
        """Charge les données depuis un fichier JSON et crée les objets."""
        try:
            with open(fichier, "r") as f:
                return [classe.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            print(f"Fichier {fichier} introuvable, on part de zero.")
            return []
        except:
            print(f"Erreur : Le fichier {fichier} est mal ecrit ou corrompu !")
            return []

    def generer_id_reservation(self, reservations: list) -> str:
        """Génère un nouvel ID automatique (ex: RES004)."""
        if not reservations: 
            return "RES001"
        last_id = reservations[-1].id_reservation 
        num = int(last_id[3:]) + 1  
        return f"RES{num:03d}" 

    def filtrer_reservations_par_client(self, reservations: list, id_c: str) -> list:
        """Retourne uniquement les réservations d'un client donné."""
        res_filtrees = []
        for r in reservations:
            if r.id_client == id_c:
                res_filtrees.append(r)
        return res_filtrees