def dates_au_plus_tot(matrice_rang):
    matrice_au_plus_tot = [[], [], [], [], []]

    # ligne 0 = rang / ligne 1 = nom(durée de la tâche)
    for i in range(len(matrice_rang)):
        matrice_au_plus_tot[0].append(matrice_rang[i][1])
        matrice_au_plus_tot[1].append(str(matrice_rang[i][0])+"("+str(matrice_rang[i][2])+")")
    # ligne 2 = prédecesseurs
    matrice_au_plus_tot[2].append(".")
    for i in range(1, len(matrice_rang)):
        matrice_au_plus_tot[2].append(matrice_rang[i][3:])

    # initialisation de la ligne 3 de la matrice_au_plus_tot
    matrice_au_plus_tot[3].append(0)
    matrice_au_plus_tot[4].append(0)
    l_somme = [0]
    liste = [l_somme]

    for i in range(1, len(matrice_rang)):
        predecesseur = matrice_rang[i][3:]
        l_somme = []
        for predecessor in predecesseur:
            for k in range(len(matrice_rang)):
                if matrice_rang[k][0] == predecessor:
                    somme = max(liste[k][:]) + int(matrice_rang[k][2])
                    l_somme.append(somme)
        liste.append(l_somme)
        matrice_au_plus_tot[3].append(liste[i])
        matrice_au_plus_tot[4].append(max(liste[i]))
    return matrice_au_plus_tot, max(l_somme)
