def marge(matrice_date_au_plus_tot, matrice_date_au_plus_tard):
    marge = [[], [], [], [], []]
    # ligne 1 rang
    marge[0] = matrice_date_au_plus_tard[0]
    # ligne 2 nom tâche(durée)
    marge[1] = matrice_date_au_plus_tard[1]
    # ligne 3 date au plus tôt
    marge[2] = matrice_date_au_plus_tot[4]
    # ligne 4 date au plus tard
    marge[3] = matrice_date_au_plus_tard[4]
    # ligne 5 marge
    for j in range(len(matrice_date_au_plus_tot[1])):
        marge[4].append(matrice_date_au_plus_tard[4][j] - matrice_date_au_plus_tot[4][j])
    return marge
