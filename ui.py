import os

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
    
def afficher_reservations(liste_res):
    print("\n--- TOUTES LES RESERVATIONS ---")
    if not liste_res:
        print("Aucune réservation.")
    for r in liste_res:
        print(r)
        
def afficher_reservations_client(liste_res: list, id_c: str):
    print(f"\n--- RESERVATIONS DU CLIENT {id_c} ---")
    trouve = False
    for r in liste_res:
        if r.id_client == id_c:
            print(r)
            trouve = True
    if not trouve:
        print("Aucune réservation pour ce client.")


def nettoyer_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')