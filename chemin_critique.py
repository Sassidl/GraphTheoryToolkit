def chemin_critique(marge, matrice_date_au_plus_tard, matrice, date_max):
    chemins_critiques = [[], [], [], []]
    # ligne 1 rang
    chemins_critiques[0] = marge[0]
    # ligne 2 nom tâche(durée)
    chemins_critiques[1] = marge[1]
    # ligne 3 marge
    chemins_critiques[2] = marge[4]

    # ligne 4 chemin critique
    # prendre toutes les tâches qui ont une marge totale 0 et mettre leurs successerus respectifs :
    def liste_marge(marge, matrice_date_au_plus_tard, matrice):
        liste = [[], [], [], []]
        for i in range(len(marge[4])):
            if marge[4][i] == 0:
                nom = matrice[i][0]
                liste[0].append(nom)
                index = i
                liste[1].append(index)
                successeurs = matrice_date_au_plus_tard[2][i]
                liste[2].append(successeurs)
                duree = matrice[i][2]
                liste[3].append(duree)
        # tri des successeurs :
        for i in range(len(liste[2])):
            l = []
            for j in range(len(liste[2][i])):
                if liste[2][i][j] in liste[0]:
                    l.append(liste[2][i][j])
            liste[2][i] = l
        return liste

    def parcours_prof(matrice, marge, matrice_date_au_plus_tard):
        l = liste_marge(marge, matrice_date_au_plus_tard, matrice)

        def dfs(nom, chemin, chemins):
            chemin.append(nom)
            if nom == l[0].index(l[0][-1]):
                chemins.append(chemin.copy())
            else:
                for succ in l[2][nom]:
                    succ_index = l[0].index(succ)
                    dfs(succ_index, chemin, chemins)
            chemin.pop()

        chemins = []
        dfs(0, [], chemins)
        chemins_i = []
        # vérification que la somme des durées fait bien la date_max :
        for chemin in chemins:
            somme = 0
            for index in chemin:
                somme += l[3][index]
            if somme == date_max:
                chemins_i.append(chemin)
        chemins_n = [[l[0][index] for index in chemin] for chemin in chemins_i]
        return chemins_n

    chemins_critiques[3] = parcours_prof(matrice, marge, matrice_date_au_plus_tard)
    return chemins_critiques
