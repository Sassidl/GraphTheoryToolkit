def dates_au_plus_tard(matrice, date_max):
    matrice_au_plus_tard = [[], [], [], [], []]
    # ligne 0 = rang / ligne 1 = nom(durée de la tâche)
    for i in range(len(matrice)):
        matrice_au_plus_tard[0].append(matrice[i][1])
        matrice_au_plus_tard[1].append(str(matrice[i][0])+"("+str(matrice[i][2])+")")


    # initialisation de la ligne 2
    matrice[-1].append('.')
    matrice[-1].append('.')
    for i in range(-1, -len(matrice), -1):
        predecesseur=[]
        for j in range(3, len(matrice[i])):
            if matrice[i][j]=='.':
                break
            predecesseur.append(matrice[i][j])
        for predessor in predecesseur :
            #on rajoute -1 à -len pour qu'il aille jusqu'à -8
            for k in range(-1, -len(matrice)-1, -1):
                if matrice[k][0] == predessor:
                    if '.' not in matrice[k]:
                        matrice[k].append('.')
                    matrice[k].append(matrice[i][0])
                    break
    #ligne 2 avec les sucesseurs
    for i in range(len(matrice)):
        l = []
        for j in range(-1,-len(matrice),-1):
            if matrice[i][j]=='.':
                break
            l.append(matrice[i][j])
        matrice_au_plus_tard[2].append(l)

    #ligne 3 et 4:
    matrice_au_plus_tard[3].insert(0,date_max)
    matrice_au_plus_tard[4].insert(0,date_max)
    l_diff = [date_max]
    liste = [l_diff]
    while len(liste)!=len(matrice):
        l_diff = []
        liste.insert(0,l_diff)
    for i in range (-2, -len(matrice)-1,-1):
        successeur = matrice_au_plus_tard[2][i]
        l_diff = []
        for successor in successeur:
            for k in range (len(matrice)):
                if matrice[k][0] == successor:
                    diff = min(liste[k][:])-int(matrice[i][2])
                    l_diff.insert(0, diff)
                    break
        liste[i] = l_diff
        matrice_au_plus_tard[3].insert(0, liste[i])
        matrice_au_plus_tard[4].insert(0, min(liste[i]))
    return matrice_au_plus_tard
