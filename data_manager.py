import json

class DataManager:
    @staticmethod
    def sauvegarder(fichier, liste_objets):
        donnees = [obj.to_dict() for obj in liste_objets]
        with open(fichier, "w") as f:
            json.dump(donnees, f, indent=4)

    @staticmethod
    def charger(fichier, classe_cible):
        try:
            with open(fichier, "r") as f:
                donnees = json.load(f)
                return [classe_cible.from_dict(d) for d in donnees]
        except FileNotFoundError:
            return []