from models.client import Client
from models.vehicule import Vehicule
from models.reservation import Reservation
from models.tarifs import TarifsManager
from data_manager import DataManager

def main():
    dm = DataManager()
    tm = TarifsManager()
    
    # Chargement initial
    clients = dm.charger("clients.json", Client)
    vehicules = dm.charger("vehicules.json", Vehicule)
    reservations = dm.charger("reservations.json", Reservation)

    while True:
        print("\n--- GESTION LOCA-AUTO ---")
        print("1. Ajouter un client")
        print("2. Ajouter un véhicule")
        print("3. Faire une réservation")
        print("4. Afficher tout")
        print("5. Quitter et sauvegarder")
        
        choix = input("\nVotre choix : ")

        if choix == "1":
            id_c = input("ID Client : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            clients.append(Client(id_c, nom, prenom, "mail@test.com", "0600", "Adresse"))
            print("Client ajouté !")

        elif choix == "2":
            id_v = input("ID Véhicule : ")
            marque = input("Marque : ")
            cyl = int(input("Cylindrée (4, 5 ou 6) : "))
            vehicules.append(Vehicule(id_v, marque, "Modèle", cyl, 0.0, "2024"))
            print("Véhicule ajouté !")

        elif choix == "3":
            id_res = input("ID Réservation : ")
            id_c = input("ID du Client : ")
            id_v = input("ID du Véhicule : ")
            
            # Recherche des objets par ID
            c_obj = next((c for c in clients if c.id_client == id_c), None)
            v_obj = next((v for v in vehicules if v.id_vehicule == id_v), None)
            
            if c_obj and v_obj:
                j = int(input("Nombre de jours : "))
                k = int(input("Forfait KM : "))
                res = Reservation(id_res, id_c, id_v, j, k, tm, v_obj)
                reservations.append(res)
                print(f"OK ! Coût estimé : {res.cout_estime}€")
            else:
                print("Erreur : Client ou Véhicule introuvable.")

        elif choix == "4":
            print("\n--- CLIENTS ---")
            for c in clients: print(c)
            print("\n--- VEHICULES ---")
            for v in vehicules: print(v)
            print("\n--- RESERVATIONS ---")
            for r in reservations: print(r)

        elif choix == "5":
            dm.sauvegarder("clients.json", clients)
            dm.sauvegarder("vehicules.json", vehicules)
            dm.sauvegarder("reservations.json", reservations)
            print("Sauvegarde effectuée. Au revoir !")
            break

if __name__ == "__main__":
    main()