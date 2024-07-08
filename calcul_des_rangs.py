def calculer_rangs(matrice, matrice_contrainte):

    # création de la liste de valeurs de rang finale

    liste_des_rangs = []

    rang = 0

    transposee = [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]

    transposee = [[i] + row for i, row in enumerate(transposee)]

    tmp_transposee = transposee

    # calcul de chaque rang

    while len(tmp_transposee) != 0:

        rangs_a_retirer = []

        for i in range(len(tmp_transposee)):
            predecesseur = False
            for j in range(1, len(tmp_transposee) + 1):
                if tmp_transposee[i][j] != '*':
                    predecesseur = True

                if j == len(tmp_transposee):
                    if not predecesseur:
                        liste_des_rangs.append([tmp_transposee[i][0], rang])
                        rangs_a_retirer.append(i)

        nombre_variable_a_retirer = 0

        for i in range(0, len(rangs_a_retirer)):

            # Initialisation de new_matrix à partir de tmp_transposee pour cette itération
            new_matrix = list(tmp_transposee)

            # Ajustement pour la suppression des colonnes
            le_rang_a_retirer = rangs_a_retirer[i] + 1 - nombre_variable_a_retirer

            # Supprimer la colonne spécifiée
            for j in range(len(new_matrix)):
                new_matrix[j] = [element for k, element in enumerate(new_matrix[j]) if k != le_rang_a_retirer]

            # Réajustement pour la suppression des lignes
            le_rang_a_retirer = rangs_a_retirer[i] - nombre_variable_a_retirer

            # Supprimer la ligne spécifiée en utilisant la matrice déjà mise à jour (new_matrix)
            new_matrix = [row for x, row in enumerate(new_matrix) if x != le_rang_a_retirer]

            nombre_variable_a_retirer += 1
            tmp_transposee = new_matrix

        rang += 1

    # concaténation du rang
    for i in range(len(matrice_contrainte)):
        for j in range(len(liste_des_rangs)):
            if matrice_contrainte[i][0] == liste_des_rangs[j][0]:
                liste_des_rangs[j].append(matrice_contrainte[i][1])
                predecesseur = matrice_contrainte[i][2:]
                for predecessor in predecesseur:
                    liste_des_rangs[j].append(predecessor)
    # la liste des rangs croissante contient dans l'ordre : le nom, le rang, la durée de la tâche, les prédécesseurs
    return liste_des_rangs
