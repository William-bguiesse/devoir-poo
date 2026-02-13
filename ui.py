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