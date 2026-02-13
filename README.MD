# Exercice de Location de Véhicules

## 02 - explication :

### 1. La Classe Client
* [cite_start]**Rôle** : elle représente un client de l'agence.
* **Attributs** :
    * [cite_start]`id_client` (str) : Identifiant unique du client[cite: 93].
    * [cite_start]`nom` (str), `prenom` (str)[cite: 94, 95].
    * [cite_start]`mail` (str), `telephone` (str)[cite: 96, 97].
    * [cite_start]`adresse` (str)[cite: 98].

### 2. Classe Vehicule
* [cite_start]**Rôle** : Représente un véhicule de la flotte.
* **Attributs** :
    * [cite_start]`id_vehicule` (str) : Identifiant unique du véhicule[cite: 100].
    * [cite_start]`marque` (str), `modele` (str)[cite: 101, 102].
    * [cite_start]`cylindree` (int) : Nombre de cylindres (4, 5 ou 6)[cite: 103].
    * [cite_start]`kilometrage_actuel` (float) : Distance totale parcourue[cite: 105].
    * [cite_start]`date_mise_en_circulation` (str) : Date au format AAAA-MM-JJ[cite: 106].

### 3. Classe Reservation
* [cite_start]**Rôle** : Gère la location d'un véhicule par un client.
* **Attributs** :
    * [cite_start]`id_reservation` (str), `id_client` (str), `id_vehicule` (str)[cite: 108, 109, 110].
    * [cite_start]`date_depart` (str), `date_retour` (str)[cite: 111, 112].
    * [cite_start]`forfait_km` (int) : Forfait choisi (100, 200, 300 ou +300)[cite: 113].
    * [cite_start]`cout_journalier` (float), `prix_km_supp` (float)[cite: 114, 115].
    * [cite_start]`cout_estime` (float) : Calculé automatiquement selon le tarif et la durée.