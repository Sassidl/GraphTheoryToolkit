import os
import time

from creation_matrice import creation_matrice
from verification_matrice import verification_matrice
from affichage_matrice import afficher_matrice
from affichage_matrice import retourner_matrice_des_valeurs
from calcul_des_rangs import calculer_rangs
from dates_au_plus_tot import dates_au_plus_tot
from dates_au_plus_tard import dates_au_plus_tard
from marge import *
from chemin_critique import *

# menu
while True:
    print("===== Menu Principal =====")
    print('Affichage de la matrice')
    # Appel de la fonction lecture_fichier avec le nom du fichier
    # boucle de vérification
    while True:
        print("Entrez le nom de votre fichier")
        nom_fichier = input()
        if nom_fichier.endswith('.txt') and os.path.isfile(nom_fichier):
            break  # Sortie de la boucle si le fichier est valide
        else:
            print(
                "Nom de fichier invalide ou fichier non trouvé. Assurez-vous que le fichier se termine par '.txt' et "
                "qu'il existe.")
    matrice_resultat = creation_matrice(nom_fichier)
    print("\nLe tableau de contraintes est en mémoire\n")
    # Affichage du tableau résultat
    for ligne in matrice_resultat:
        print(ligne)
    time.sleep(3)

    # Affichage de la matrice des valeurs
    print('\nAffichage de la matrice des valeurs\n')
    afficher_matrice(matrice_resultat)
    matrice_des_valeurs = retourner_matrice_des_valeurs(matrice_resultat)
    time.sleep(3)

    # Vérification de la matrice
    print('\nVérification des circuits\n')
    verif, val = verification_matrice(matrice_resultat)
    print('\n' + verif + '\n')
    while not val:
        print('Veuillez resaisir un nouveau nom de fichier\n')
        while True:
            print("Entrez le nom de votre fichier")
            nom_fichier = input()
            if nom_fichier.endswith('.txt') and os.path.isfile(nom_fichier):
                break  # Sortie de la boucle si le fichier est valide
            else:
                print(
                    "Nom de fichier invalide ou fichier non trouvé. Assurez-vous que le fichier se termine par '.txt' "
                    "et qu'il existe.")
        matrice_resultat = creation_matrice(nom_fichier)
        print("\nLe tableau de contraintes est en mémoire\n")

        # Affichage du tableau résultat
        for ligne in matrice_resultat:
            print(ligne)
        # time.sleep(3)

        # Affichage de la matrice des valeurs
        print('\nAffichage de la matrice des valeurs\n')
        afficher_matrice(matrice_resultat)
        matrice_des_valeurs = retourner_matrice_des_valeurs(matrice_resultat)
        verif, val = verification_matrice(matrice_resultat)
        print('\n' + verif + '\n')

    # Affichage des rangs
    print('\nAffichage des rangs\n')
    matrice_rang = calculer_rangs(matrice_des_valeurs, matrice_resultat)
    print("\n")
    for ligne in matrice_rang:
        print(ligne)
    print("\n")
    time.sleep(3)

    # Affichage des dates au plus tôt
    print('\nAffichage de la matrice des dates au plus tôt\n')
    (matrice_date_au_plus_tot, date_max) = dates_au_plus_tot(matrice_rang)
    print("\n")
    headers = ["Rangs", "Tâches (Durée)", "Prédecesseurs", "Toutes les dates au plus tôt", "Dates au plus tôt"]
    max_widths = [max([len(str(item)) for item in column] + [len(header)]) for column, header in
                  zip(matrice_date_au_plus_tot, headers)]
    formatted_headers = ' | '.join(header.ljust(width) for header, width in zip(headers, max_widths))
    print(formatted_headers)
    print('-' * (sum(max_widths) + 3 * len(max_widths)))
    for i in range(len(matrice_date_au_plus_tot[0])):
        row_items = [column[i] for column in matrice_date_au_plus_tot]
        formatted_row = ' | '.join(str(item).ljust(width) for item, width in zip(row_items, max_widths))
        print(formatted_row)
    print("\n")
    time.sleep(3)

    # Affichage de la matrice de date au plus tard
    print('\nAffichage de la matrice des dates au plus tard\n')
    matrice_date_au_plus_tard = dates_au_plus_tard(matrice_rang, date_max)
    print("\n")
    headers = ["Rangs", "Tâches (Durée)", "Successeurs", "Toutes les dates au plus tard", "Dates au plus tard"]
    max_widths = [max([len(str(item)) for item in column] + [len(header)]) for column, header in
                  zip(matrice_date_au_plus_tard, headers)]
    formatted_headers = ' | '.join(header.ljust(width) for header, width in zip(headers, max_widths))
    print(formatted_headers)
    print('-' * (sum(max_widths) + 3 * len(max_widths)))
    for i in range(len(matrice_date_au_plus_tard[0])):
        row_items = [column[i] for column in matrice_date_au_plus_tard]
        formatted_row = ' | '.join(str(item).ljust(width) for item, width in zip(row_items, max_widths))
        print(formatted_row)
    print("\n")
    time.sleep(3)

    # Affichage des marges totales:
    print('\nAffichage des marges totales\n')
    matrice_marge = marge(matrice_date_au_plus_tot, matrice_date_au_plus_tard)
    print("\n")
    headers = ["Rangs", "Tâches (Durée)", "Dates au plus tôt", "Dates au plus tard", "Marges Totales"]
    # Calcul de la largeur maximale nécessaire pour chaque colonne, y compris les en-têtes
    column_widths = [max(len(str(item)) for item in category) for category in matrice_marge]
    max_header_width = max(len(header) for header in headers)
    column_widths = [max(width, max_header_width) for width in column_widths]
    # Affichage des en-têtes
    for header, width in zip(headers, column_widths):
        print(f"{header:{width}} | ", end="")
    print("\n" + "-" * (sum(column_widths) + 3 * len(column_widths)))
    # Transposition et affichage des données
    for row in zip(*matrice_marge):
        for item, width in zip(row, column_widths):
            print(f"{item:{width}} | ", end="")
        print()
    time.sleep(3)

    # Affichages des chemins critiques :
    print('\nAffichage des chemins critiques\n')
    matrice_chemin_critique = chemin_critique(matrice_marge, matrice_date_au_plus_tard, matrice_rang, date_max)
    print("\n")
    for lignes in matrice_chemin_critique[3]:
        for ligne in lignes:
            if ligne == lignes[-1]:
                print(ligne)
                break
            print(str(ligne) + '->', end='')
    print("\n")
    time.sleep(3)

    choix = input('Voulez quittez le menu:Y/N\n')
    while choix != 'Y' and choix != 'N':
        print('\nVous avez entré votre choix de manière incorrecte')
        choix = input('Voulez quittez le menu:Y/N\n')
    if choix == 'Y':
        print("==========================")
        break
