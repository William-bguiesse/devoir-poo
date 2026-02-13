def afficher_clients(liste_clients):
    print("\n" + "="*30)
    print("REPERTOIRE DES CLIENTS")
    if not liste_clients:
        print("Aucun client dans la base.")
    else:
        for c in liste_clients:
            print(c)

def afficher_vehicules(liste_vehicules):
    print("\n" + "="*30)
    print("PARC AUTOMOBILE")
    if not liste_vehicules:
        print("Aucun véhicule dans la base.")
    else:
        for v in liste_vehicules:
            print(v)
            
def afficher_reservations(liste_reservations):
    print("\n--- RESERVATIONS ---")
    if not liste_reservations:
        print("Aucune réservation.")
    for res in liste_reservations:
        print(res)
        
def demander_reservation(tm):
    print("\n--- NOUVELLE RESERVATION ---")
    id_res = input("ID Réservation : ")
    id_c = input("ID Client : ")
    id_v = input("ID Véhicule : ")
    try:
        j = int(input("Jours : "))
        k = int(input("KM : "))
        return id_res, id_c, id_v, j, k
    except:
        print("Erreur de saisie.")
        return None