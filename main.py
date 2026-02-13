from models.client import Client
from models.vehicule import Vehicule
from models.reservation import Reservation
from models.tarifs import TarifsManager
from data_manager import DataManager
import ui

def main():
    dm = DataManager()
    tm = TarifsManager()
    clients = dm.charger("clients.json", Client)
    vehicules = dm.charger("vehicules.json", Vehicule)
    reservations = dm.charger("reservations.json", Reservation)

    while True:
        print("\n--- GESTION LOCA-AUTO ---")
        print("1. Ajouter un client")
        print("2. Ajouter un véhicule")
        print("3. Créer une réservation")
        print("4. Afficher tout")
        print("5. Quitter et sauvegarder")
        
        choix = input("\nVotre choix : ")

        if choix == "1":
            id_c = input("ID Client : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            clients.append(Client(id_c, nom, prenom, "mail@test.com", "0600", "Adresse"))
            print("Client ajouté.")

        elif choix == "2":
            id_v = input("ID Véhicule : ")
            marque = input("Marque : ")
            try:
                cyl = int(input("Cylindrée (4, 5 ou 6) : "))
                vehicules.append(Vehicule(id_v, marque, "Modèle", cyl, 0.0, "2024"))
                print("Véhicule ajouté !")
            except ValueError:
                print("Erreur : La cylindrée doit être un nombre !")

        elif choix == "3":
            id_res = input("ID Réservation : ")
            id_c = input("ID du Client : ")
            id_v = input("ID du Véhicule : ")
            
            c_obj = next((c for c in clients if c.id_client == id_c), None)
            v_obj = next((v for v in vehicules if v.id_vehicule == id_v), None)
            
            if c_obj and v_obj:
                try:
                    j = int(input("Nombre de jours : "))
                    k = int(input("Forfait KM : "))
                    res = Reservation(id_res, id_c, id_v, j, k, tm, v_obj)
                    reservations.append(res)
                    print(f"Réservation créée. Coût : {res.cout_estime}€")
                except ValueError:
                    print("Erreur : Jours et KM doivent être des nombres !")
            else:
                print("Erreur : ID Client ou Véhicule inconnu.")

        elif choix == "4":
            ui.afficher_clients(clients)
            ui.afficher_vehicules(vehicules)
            ui.afficher_reservations(reservations)

        elif choix == "5":
            dm.sauvegarder("clients.json", clients)
            dm.sauvegarder("vehicules.json", vehicules)
            dm.sauvegarder("reservations.json", reservations)
            print("Sauvegarde réussie. Fermeture...")
            break

if __name__ == "__main__":
    main()