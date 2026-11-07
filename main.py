taches = []
def afficher_menu():
    print()
    print("=== GESTION DES TÂCHES ===")
    print()
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")
    print()

def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        print("--- Liste des tâches ---")
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")
    


def rechercher_tache():
    mot = input("Mot-clé à rechercher : ").strip().lower()
    if mot == "":
        print("Erreur : le mot-clé ne peut pas être vide.")
        return
    trouve = False
    for i in range(len(taches)):
        if mot in taches[i].lower():
            print(f"{i + 1}. {taches[i]}")
            trouve = True
    if not trouve:
        print("Aucune tâche ne correspond à ce mot-clé.")



def main():
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            rechercher_tache()
        elif choix == "0":
            print("Au revoir !")
        else:
            print("Erreur : option invalide, choisissez 1, 2, 3 ou 0.")
main()
