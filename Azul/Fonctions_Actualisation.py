from Variable import *
import os
from Fonctions_Graphique import *
from Fonctions_Initialisation import *
from Fonctions_Sauvegarde import *
from time import *
from upemtk import *
from math import *
from random import randint


######################################################################################################################


def Choix_Nb_Joueur():
    ''' Determine le nombre de joueur, et le genre des joueurs en fonction de l'endroit où clique l'utilisateur '''
    x,y = recup_clic()
    test = 0
    if x < 6*longueur//9:
        if y < hauteur//3:
            NbJoueur = 2
            ListeTypejoueur = ['Humain','Bot']
        elif y < 2*hauteur//3:
            NbJoueur = 3
            ListeTypejoueur = ['Humain','Bot', 'Bot']
        else:
            NbJoueur = 4
            ListeTypejoueur = ['Humain','Bot','Bot','Bot']
    else:
        NbJoueur = 4
        ListeTypejoueur = ['Bot','Bot', 'Bot', 'Bot']
        test = 1
    return NbJoueur, ListeTypejoueur, test

def RemplirFabrique(NbJoueurs, Sac):
    ''' Récupère des tuiles du sac de manière aléatoire pour les mettre dans les fabriques'''
    ZoneFabrique = []
    for i in range((NbJoueurs * 2) + 1):
        ZoneFabrique.append([])
        if len(Sac)<4:
            ZoneFabrique[i] = [None,None,None,None]
        else:
            for j in range(4):
                couleur = randint(0, len(Sac) - 1)
                ZoneFabrique[i].append(Sac.pop(couleur))
    return ZoneFabrique

def confirmer():
    '''Renvoie True si l'utilisateur clique à l'emplacement du bouton valider et False s'il clique à l'endroit du bouton annuler'''
    minxJ = 19 * longueur // 20                                               #Bouton jaune
    minyJ = 4 * hauteur // 15
    maxxJ = minxJ + longueur // 10
    maxyJ = 2 * minyJ

    minxR = 19 * longueur // 20
    minyR = 9 * hauteur // 15
    maxxR = minxR + longueur // 10
    maxyR = minyR + 4*hauteur//15
    while True:
        coordonee = recup_clic()
        if minxJ < coordonee[0] < maxxJ and minyJ < coordonee[1] < maxyJ:
            return True
        if minxR < coordonee[0] < maxxR and minyR < coordonee[1] < maxyR:
            return False

def determiner_fabrique_selectioner(coordonee, NbJoueur):
    ''' Renvoie le numero de la fabrique selectionée en fonction du nombre de fabriques totale et de l'endroit où a cliqué le joueur'''
    NbDeFabrique =(NbJoueur * 2) + 1
    if coordonee[1] < hauteur//15 +tailleC and coordonee[1] > hauteur//15 - tailleC:
        n = longueur // NbDeFabrique
        for i in range(NbDeFabrique):
            if coordonee[0] >(i*n + n//4 + tailleC - tailleC) and coordonee[0]<(i*n + n//4 + 2*tailleC):
                return i
        return None
    elif clic_valide_centre(coordonee):
        return 10

def clic_valide_fabrique(coordonee, num_fabrique, NbJoueurs):
    ''' Verifie si le clic est dans une des fabriques '''
    n =(NbJoueurs * 2) + 1
    centrex =((longueur // n) // 4) +(num_fabrique *(longueur // n)) + tailleC
    centrey =(hauteur // 15)
    minx = centrex - tailleC
    miny = centrey - tailleC
    maxx = centrex + tailleC
    maxy = centrey + tailleC
    if coordonee[0]  > minx and coordonee[0] < maxx and coordonee[1] > miny and coordonee[1] < maxy:
        return True
    else:
        return False

def determiner_tuile_selectioner(coordonne, M, num_fabrique, NbJoueurs):
    ''' Détermine la couleur de la tuile où a cliqué le joueur'''
    n =(NbJoueurs * 2) + 1
    centrex =((longueur // n) // 4) +(num_fabrique *(longueur // n)) + tailleC
    centrey =(hauteur // 15)
    if coordonne[0] < centrex and coordonne[0] > centrex - tailleC :
        x = 0
    elif coordonne[0] > centrex and coordonne[0] < centrex + tailleC :
        x = 1
    else:
        x=None
    if coordonne[1] < centrey and coordonne[1] > centrey - tailleC:
        y = 0
    elif coordonne[1] > centrey and coordonne[1] < centrey + tailleC:
        y = 1
    else:
        y=None

    if x == None or y == None:
        return None

    if y == 0:
        return M[num_fabrique][x + y]
    else:
        return M[num_fabrique][x + y + 1]

def actualiser_fabrique(matF, num_fabrique):
    ''' Remplit la fabrique sélectionner de None, pour que les cases ne soient pas dessiner'''
    for i in range(len(matF[num_fabrique])):
        matF[num_fabrique][i] = None

def recup_clic():
    '''Récupère les coordonees du clic'''
    x, y, _ = attente_clic()
    return x, y

def compter_couleur_identique(lst, tuile):
    '''Compte le nombre de tuile de la même couleur que la tuile précédemment sélectionnée dans la fabrique'''
    nb = 0
    for i in range(len(lst)):
        if lst[i] == tuile:
            nb += 1
    return nb

def tuile_valide(tuile):
    '''Vérifie que la tuile sélectionnée ne vaut pas None'''
    if tuile == None:
        return False
    return True

def clic_valide_escalier(coordonee, numJoueur):
    ''' Vérifie que le clic du joueur se trouve dans son escalier'''
    if numJoueur % 2 == 0:
        minx = longueur//10
    else:
        minx = 6 * longueur//10
    if numJoueur < 2:
        miny =  3*hauteur//15
    else:
        miny =  10*hauteur//15

    maxx = minx + 7 * tailleC
    maxy = miny + 4/6*tailleC + 5*tailleC

    if coordonee[0]  < minx or coordonee[0] > maxx or coordonee[1] < miny or coordonee[1] > maxy:
        return False
    else:
        return True

def determiner_ligne_selectioner(coordonee, numJoueur):
    ''' Détermine quel ligne d'escalier ou plancher le joueur a sélectionné'''
    if numJoueur %2 == 0:
        XDebutPlancher = longueur//10
    else:
        XDebutPlancher = 6*longueur//10

    XFinPlancher = XDebutPlancher + 8*tailleC

    if numJoueur < 2:
        DebutPlancher =(3 * hauteur // 15) + 7/6*tailleC + 5*tailleC
        if int((coordonee[1] -(3 * hauteur // 15)) //(7/6 * tailleC)) < 5:
            return int((coordonee[1] -(3 * hauteur // 15)) //(7/6 * tailleC))
        elif coordonee[1]> DebutPlancher and coordonee[1]<DebutPlancher + tailleC and XDebutPlancher<coordonee[0] and coordonee[0]<XFinPlancher:
            return 5
    else:
        DebutPlancher =(10 * hauteur // 15) + 7/6*tailleC + 5*tailleC
        if int((coordonee[1] -(10 * hauteur // 15)) //(7/6 * tailleC)) < 5:
            return int((coordonee[1] -(10 * hauteur // 15)) //(7/6 * tailleC))
        elif coordonee[1]> DebutPlancher and coordonee[1] < DebutPlancher + tailleC and XDebutPlancher<coordonee[0] and coordonee[0]<XFinPlancher:
            return 5

def SelectionTuilesEtFabrique(matF, NbJoueur, centre):
    '''Renvoie la tuile sélectionée, la fabrique où a été sélectionnée la tuile et le nombre de tuile de cette couleur dans la fabrique'''
    fabrique = None
    while fabrique == None:
        coordonee=recup_clic()
        fabrique = determiner_fabrique_selectioner(coordonee, NbJoueur)
    if fabrique == 10:
        tuile = determiner_tuile_selectioner_dans_centre(coordonee, centre)
        nb_tuile = compter_couleur_identique_matrice(centre, tuile)
        SurbrillanceCentre(centre, tuile)
        return fabrique, tuile, nb_tuile, coordonee
    else:
        tuile = determiner_tuile_selectioner(coordonee, matF, fabrique, NbJoueur)
        nb_tuile = compter_couleur_identique(matF[fabrique], tuile)
        SurbrillanceFabrique(matF, fabrique, tuile)
        return fabrique, tuile, nb_tuile, coordonee

def SelectionLigneEscalier(joueur):
    ''' Renvoie la ligne d'escalier ou le plancher selectionné par le joueur '''
    coordonee = recup_clic()
    ligne_escalier = determiner_ligne_selectioner(coordonee, joueur)
    if ligne_escalier == 5:
        return ligne_escalier
    else:
        while not clic_valide_escalier(coordonee, joueur):
            coordonee = recup_clic()
            ligne_escalier = determiner_ligne_selectioner(coordonee, joueur)
            if ligne_escalier == 5:
                break

    return ligne_escalier

def ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, ligne_select, centre, plancher, GenreJoueur):
    ''' Deplace les tuiles venant d'une fabrique vers le plateau d'un joueur si ce dernier a confirmer ce choix '''
    Dessine_boutons()
    if GenreJoueur == 'Bot':
        A_confirme = True
        sleep(1) 
    else:
        A_confirme = confirmer()
    if A_confirme == False:
        update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)
        return False
    else:
        PlaceDispo =(len(ligne_select) - ligne_select.count(None) - ligne_select.count(tuile) - 1)
        if PlaceDispo >= nb_tuile:
            TuileAPlaceDansEscalier =  nb_tuile
        else:
            TuileAPlaceDansEscalier = PlaceDispo

        FabriqueVersCentre(centre, matF[fabrique], tuile)
        actualiser_ligne_escalier(ligne_select, tuile, TuileAPlaceDansEscalier)
        actualiser_fabrique(matF, fabrique)

        if assez_de_place(nb_tuile, ligne_select,tuile) == False:
            tuile_a_placer_dans_plancher=nb_tuile-TuileAPlaceDansEscalier
            actualiser_plancher(plancher,tuile, tuile_a_placer_dans_plancher)
        update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)
        return True

def DeroulementTour(NbJoueur, matF, joueur, escalier, centre, plancher, GenreJoueur, matM, test):
    ''' Deplace les tuiles sélectionnés, vers la zone sélectionnés puis renvoie True, une fois finie'''
    if GenreJoueur == 'Humain':
        tuile = None
        while tuile == None:
            fabrique, tuile, nb_tuile, coordonee = SelectionTuilesEtFabrique(matF, NbJoueur, centre)
            while not clic_valide_centre(coordonee) and not clic_valide_fabrique(coordonee, fabrique, NbJoueur) :
                coordonee = recup_clic()
            if clic_valide_fabrique(coordonee, fabrique, NbJoueur):
                if tuile == None:
                    break
                ligne_escalier = SelectionLigneEscalier(joueur)
                if ligne_escalier == 5:
                    SurbrillancePlancher(joueur)
                    return ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, plancher, centre,plancher, GenreJoueur)
                else:
                    while not Ligne_Escalier_Valide(tuile, escalier[ligne_escalier]) or not CouleurDejaDansMur(tuile, matM[joueur][ligne_escalier]):
                        ligne_escalier = SelectionLigneEscalier(joueur)
                        if ligne_escalier == 5:
                            SurbrillancePlancher(joueur)
                            return ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, plancher, centre,plancher, GenreJoueur)
                    SurbrillanceEscalier(escalier, ligne_escalier, joueur)
                    return ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, escalier[ligne_escalier], centre,plancher, GenreJoueur)

            elif clic_valide_centre(coordonee):
                tuile, nb_tuile = SelectionTuileCentre(centre, coordonee)
                if tuile == None:
                    break
                ligne_escalier = SelectionLigneEscalier(joueur)
                if ligne_escalier == 5:
                    SurbrillancePlancher(joueur)
                    return ConfirmerDeplacementDepuisCentre(centre, tuile, nb_tuile, plancher, plancher, GenreJoueur)
                else:
                    while not Ligne_Escalier_Valide(tuile, escalier[ligne_escalier]) or not CouleurDejaDansMur(tuile, matM[joueur][ligne_escalier]):
                        ligne_escalier = SelectionLigneEscalier(joueur)
                        if ligne_escalier == 5:
                            SurbrillancePlancher(joueur)
                            return ConfirmerDeplacementDepuisCentre(centre, tuile, nb_tuile, plancher, plancher, GenreJoueur)
                    SurbrillanceEscalier(escalier, ligne_escalier, joueur)
                    return ConfirmerDeplacementDepuisCentre(centre, tuile, nb_tuile, escalier[ligne_escalier],plancher, GenreJoueur)

    elif GenreJoueur == 'Bot':
        TourIA(matF,matT,matE,matP,num_joueur, GenreJoueur, matM)
        #TourRobot(matF, centre,escalier,plancher, joueur, GenreJoueur, matM, test)
        return True

def ConfirmerDeplacementDepuisCentre(centre, tuile, nb_tuile, ligne_select, plancher, GenreJoueur):
    ''' Deplace les tuiles venant du centre vers le plateau d'un joueur si ce dernier a confirmer ce choix '''
    Dessine_boutons()
    if GenreJoueur == 'Bot':
        A_confirme = True
        sleep(1)
    else:
        A_confirme = confirmer()
    if A_confirme == False:
        update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)
        return False
    else:
        if tuile == VJeton:
            tuile_a_placer_dans_plancher = 1
            actualiser_plancher(plancher,tuile, tuile_a_placer_dans_plancher)
            actualiser_centre(centre, tuile)
            update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)
        else:
            PlaceDispo =(len(ligne_select) - ligne_select.count(None) - ligne_select.count(tuile) - 1)
            if PlaceDispo >= nb_tuile:
                TuileAPlaceDansEscalier =  nb_tuile
            else:
                TuileAPlaceDansEscalier = PlaceDispo
            actualiser_ligne_escalier(ligne_select, tuile, TuileAPlaceDansEscalier)
            actualiser_centre(centre, tuile)

            if assez_de_place(nb_tuile, ligne_select,tuile) == False:
                tuile_a_placer_dans_plancher=nb_tuile-TuileAPlaceDansEscalier
                actualiser_plancher(plancher,tuile, tuile_a_placer_dans_plancher)
            for i in range(len(centre)):
                if VJeton in centre[i]:                             #Code Hexadécimal du jeton -1
                    JetonPremierJoueurVersPlancher(centre, plancher)
                    actualiser_centre(centre, tuile)

            update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)
        return True

def actualiser_centre(centre, tuile):
    ''' Met à jour la matrice Centre, en retirant les tuiles sélectionnées par le joueur pour les remplacer par des None, puis trie la matrice afin de mettre les None en fin de matrice '''
    for i in range(len(centre)):
        for j in range(len(centre[i])):
            if centre[i][j] == tuile:
                centre[i][j] = None

    Lstcentre = []
    for i in range(len(centre)):
        for j in range(len(centre[i])):
            Lstcentre.append(centre[i][j])

    NbDeNone = Lstcentre.count(None)
    for i in range(NbDeNone):
        Lstcentre.remove(None)
    Lstcentre.sort()

    for i in range(NbDeNone):
        Lstcentre.append(None)

    m=0
    for i in range(len(centre)):
        for j in range(len(centre[i])):
            centre[i][j] = Lstcentre[m]
            m += 1

def JetonPremierJoueurVersPlancher(centre, plancher):
    ''' Envoie le jeton vert premier joueur, vers le plancher du joueur qui a pioché dans le centre en premier'''
    for i in range(len(centre)):
        for j in range(len(centre[i])):
            if centre[i][j] == VJeton:
                centre[i][j] = None
                break

    for m in range(len(plancher)):
        if plancher[m] == '':
           plancher[m] = VJeton
           break

def clic_valide_centre(coordonee):
    ''' Verifie si le joueur a cliqué dans le centre '''
    minx = 4*longueur//10
    miny = 7*hauteur//15
    maxx = minx + 8*tailleC
    maxy = miny +4*tailleC + 3*tailleC//6
    if coordonee[0]  < minx or coordonee[0] > maxx or coordonee[1] < miny or coordonee[1] > maxy:
        return False
    else:
        return True

def SelectionTuileCentre(Centre,coordonee):
    '''Renvoie la tuile sélectionée et le nombre de tuile de cette couleur dans le centre'''
    tuile = determiner_tuile_selectioner_dans_centre(coordonee, Centre)
    nb_tuile = compter_couleur_identique_matrice(Centre, tuile)
    SurbrillanceCentre(Centre, tuile)
    return tuile, nb_tuile

def determiner_tuile_selectioner_dans_centre(coordonne, centre):
    ''' Détermine la couleur de la tuile où a cliqué le joueur, s'il a cliqué dans le centre'''
    xInit = 4*longueur//10
    x = coordonne[0]
    for l in range(7):
        xTuile = xInit +(l+1)* 7*tailleC//6
        if x <= xTuile:
            j = l
            break

    yInit = 7*hauteur//15
    y = coordonne[1]
    for m in range(4):
        yTuile = yInit +(m+1)* 7*tailleC//6
        if y <= yTuile:
            i = m
            break
    return centre[i][j]

def compter_couleur_identique_matrice(mat, tuile):
    '''Compte le nombre de tuile de la même couleur que la tuile que le joueur '''
    nb = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == tuile:
                nb += 1
    return nb

def Ligne_Escalier_Valide(tuile, ligne_escalier):
    ''' Renvoie True, si la tuile peut être placé dans la ligne de l'escalier, et False si elle ne peut pas être placé'''
    if '' not in ligne_escalier:
        return False
    for i in range(len(ligne_escalier)):
        if ligne_escalier[i] not in [None, tuile, '', 'FlecheR', 'FlecheV']:
            return False
    return True

def FabriqueVersCentre(MatT, Fabrique, tuile):
    ''' Deplace les tuiles restantes dans la fabrique sélectionnée vers le centre'''
    for i in range(len(Fabrique)):
        if Fabrique[i] != tuile:
            PosV = 0
            PosH = 0
            while MatT[PosV][PosH] != None:
                if PosH < len(MatT[0])-1:
                    PosH +=1
                else:
                    PosV += 1
                    PosH = 0
            MatT[PosV][PosH] = Fabrique[i]

def assez_de_place(nb_tuile, ligne_escalier, tuile):
    '''Renvoie True, si on peut placer toutes les tuiles sélectionnées dans la ligne d'escalier sélectionnée, et False sinon'''
    if nb_tuile >(len(ligne_escalier) - ligne_escalier.count(None) - ligne_escalier.count(tuile) - 1):
        return False
    return True

def actualiser_plancher(Lst_plancher,tuile, tuile_a_placer):
    ''' Met les tuiles qui doivent aller dans le plancher dans ce dernier'''
    for j in range(tuile_a_placer):
        for i in range(len(Lst_plancher)):
            if Lst_plancher[i] == '':
                Lst_plancher[i] = tuile
                break

def actualiser_ligne_escalier(ligne_escalier, tuile, nb_tuile):
    ''' Met autant de tuiles sélectionnés que possible dans la ligne escalier sélectionné'''
    for i in range(nb_tuile):
        for j in range(len(ligne_escalier)):
            if ligne_escalier[j]  != None and ligne_escalier[j] != 'FlecheR' and ligne_escalier[j]  != 'FlecheV' and ligne_escalier[j] not in CouleurTuile and ligne_escalier[j] != VJeton :
                ligne_escalier[j] = tuile
                break


    if len(ligne_escalier) == 6:
        if '' not in ligne_escalier:
            if ligne_escalier[-1] == 'FlecheV':
                ligne_escalier[-1] = 'FlecheR'
            else:
                ligne_escalier[-1] = 'FlecheV'

def alterner_joueur(num_joueur, nbjoueur):
    ''' Modifie le joueur jouant actuellement pour passer au joueur suivant'''
    new_num_joueur = num_joueur + 1
    if new_num_joueur > nbjoueur - 1:
        return 0
    return new_num_joueur

def Fabriques_vides(matF):
    ''' Renvoie True si toutes les fabriques sont vides'''
    n = len(matF)
    p = len(matF[0])
    for i in range(n):
        for j in range(p):
            if matF[i][j] != None:
                return False
    return True

def rotation_finie(matF, centre):
    ''' Renvoie True, si la rotation actuelle est finie, c'est à dire s'il n'y pas plus de tuiles dans les fabrique et dans le centre'''
    if not Fabriques_vides(matF) or centre[0][0] != None:
        return False
    return True

def TourRobot(matF, centre, escalier, plancher, num_Joueur, GenreJoueur, matM, test):
    ''' Gere les choix de tuile sélectionnées et endroit de dépose si c'est au tour d'un robot de jouer,'''
    temps = 2.5
    if test == 1:
        temps = 0
    LstEndroit = ['Fabriques', 'Centre']
    Endroit = LstEndroit[randint(0,1)]

    if centre[0][0] == None:
        Endroit = 'Fabriques'
    if Fabriques_vides(matF) == True:
        Endroit = 'Centre'

    if Endroit == 'Fabriques' :
        nb_tuile, Tuile,NumFabrique = ChoixRobotDansFabrique()
    if Endroit == 'Centre':
        nb_tuile, Tuile = ChoixRobotDansCentre(centre)

    LigneEscalier=ChoixLigneEscalierRobot(Tuile, escalier, num_Joueur, matM)
    mise_a_jour()
    sleep(temps)

    if LigneEscalier == 5:
        EndroitDeDepot = plancher
    else:
        EndroitDeDepot = escalier[LigneEscalier]

    if Endroit == 'Fabriques':
        ConfirmerDeplacementDepuisFabrique(NumFabrique, Tuile, nb_tuile, EndroitDeDepot, centre, plancher, GenreJoueur)
    if Endroit == 'Centre':
        ConfirmerDeplacementDepuisCentre(centre, Tuile, nb_tuile, EndroitDeDepot, plancher, GenreJoueur)

    update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)

def TourIA(matF,matT,matE,matP,num_joueur, GenreJoueur, matM):
    LstMarge=[0,-1,-2,1,2,-3,-4,3,4]
    for marge in LstMarge:
        TourFini = RemplirLignes(matE, murCoeff, murExemple, matT, matP, num_joueur, GenreJoueur, marge)
        if TourFini:
            break

    update_ecran(NbJoueur, matM, matP, matE, matT, matF, score, num_joueur)

def RemplirLignes(matE,murCoeff, murExemple, matT,matP,num_joueur, GenreJoueur, marge):
    for ligne in range(len(matE[num_joueur])-1,-1,-1):
        print('la ligne actuelle est ', ligne)
        if matE[num_joueur][ligne][-2]=='':
            CouleurAPrendre, CasesARemplir = CasesAChercher(ligne,num_joueur,murExemple,murCoeff, matE)
            CasesARemplir += marge
            compteur,couleur,endroit,numFabrique = RechercheCase(CouleurAPrendre, CasesARemplir)
            print(compteur)
            if compteur!=None:
                if endroit == "Centre":
                    SurbrillanceCentre(matT,couleur)
                    mise_a_jour()
                    ConfirmerDeplacementDepuisCentre(matT, couleur, compteur, matE[num_joueur][ligne], matP[num_joueur], GenreJoueur)
                    return True
                elif endroit =="Fabriques":
                    SurbrillanceFabrique(matF, numFabrique, couleur)
                    mise_a_jour()
                    ConfirmerDeplacementDepuisFabrique(numFabrique, couleur, compteur, matE[num_joueur][ligne], matT, matP[num_joueur], GenreJoueur)
                    return True
        else:
            print(ligne, 'est pas vide')
    return False


def CasesAChercher(numLigneEscalier,num_joueur,murExemple,murCoeff,matE):
    if matE[num_joueur][numLigneEscalier][-2-numLigneEscalier] != '':
        CouleurAPrendre = matE[num_joueur][numLigneEscalier][-2-numLigneEscalier]
        print(CouleurAPrendre)
    else:
        CouleurAPrendre=[]
        for case in range(len(murCoeff[num_joueur][numLigneEscalier])):
            if murCoeff[num_joueur][numLigneEscalier][case] == 0:
                CouleurAPrendre.append(murExemple[numLigneEscalier][case])
    CasesARemplir = matE[num_joueur][numLigneEscalier].count('')
    print(CasesARemplir,CouleurAPrendre, 'pour la ligne numéro', numLigneEscalier)
    return CouleurAPrendre, CasesARemplir

def RechercheCase(LstCouleur, NbCases):
    for couleur in LstCouleur:
        compteur = 0
        for ligne in range(len(matT)):
            compteur += matT[ligne].count(couleur)
        if compteur == NbCases:
            Endroit = "Centre"
            return compteur,couleur,Endroit, None
        for numFabrique in range(len(matF)):
            compteur = matF[numFabrique].count(couleur)
            if compteur == NbCases:
                Endroit = "Fabriques"
                return compteur,couleur,Endroit,numFabrique
    return None, None, None, None
        

def ChoixRobotDansFabrique():
    Tuile = None
    while Tuile == None:
        NumFabrique = randint(0,len(matF)-1)
        NumTuile = randint(0,3)
        Tuile = matF[NumFabrique][NumTuile]

    nb_tuile = compter_couleur_identique(matF[NumFabrique], Tuile)
    SurbrillanceFabrique(matF, NumFabrique, Tuile)
    return nb_tuile, Tuile, NumFabrique

def ChoixRobotDansCentre(centre):
    Tuile = None
    while Tuile == None:
        LigneCentre = randint(0,3)
        ColonneCentre = randint(0,6)
        Tuile = matT[LigneCentre][ColonneCentre]
    nb_tuile = compter_couleur_identique_matrice(centre, Tuile)
    SurbrillanceCentre(centre, Tuile)
    return nb_tuile, Tuile

def ChoixLigneEscalierRobot(Tuile, escalier, num_Joueur, matM):
    LigneEscalier = None
    while LigneEscalier == None:
        LigneEscalier = randint(0,5)
        if LigneEscalier == 5:
            break
        elif LigneEscalier < 5 :
            if Ligne_Escalier_Valide(Tuile, escalier[LigneEscalier]) == False or CouleurDejaDansMur(Tuile, matM[num_Joueur][LigneEscalier]) == False:
                LigneEscalier = None
    if LigneEscalier < 5:
        SurbrillanceEscalier(escalier, LigneEscalier, num_Joueur)
    else:
        SurbrillancePlancher(num_joueur)
    return LigneEscalier

def DeterminerPremierJoueur(matP):
    for i in range(len(matP)):
        if VJeton in matP[i]:
            return i

def FinDeRotation(NbJoueur, matE, matM, murCoeff, murExemple, score, matP):
    for numjoueur in range(NbJoueur):
        ExaminerLigne(numjoueur,matE,matM,murCoeff,murExemple)
        VideEscalier(numjoueur,matE)
        CalculMalus(numjoueur, matP, score)
    return InitialiserPlanchers(NbJoueur)

def ExaminerLigne(num_joueur, matE, matM, murCoeff, murExemple):
    for ligne in range(len(matE[num_joueur])):
        if matE[num_joueur][ligne][-2] != '':
            Tuile = matE[num_joueur][ligne][-2]
            ActualisationMatFinDeTour(murExemple, murCoeff, matM, num_joueur, ligne, Tuile)

def ActualisationMatFinDeTour(murExemple, murCoeff, matM, num_joueur, ligne, Tuile):
    for i in range(len(murExemple[ligne])):
        if murExemple[ligne][i] == Tuile:
            murCoeff[num_joueur][ligne][i] = 1
            CalculPointsUneCase(num_joueur,score, (ligne,i),murCoeff)
            matM[num_joueur][ligne][i] = Tuile
            break

def case_valide(M,i,j):
    n = len(M)
    return (0 <= i <= (n - 1) and 0 <= j <= (n - 1))

def CalculPointsUneCase(num_joueur, score, coord, murCoeff):
    ComptV = 0
    for DepV in [-1,1]:
        i = coord[0] + DepV
        j = coord[1]
        while True:
            if case_valide(murCoeff[num_joueur],i,j) and murCoeff[num_joueur][i][j] == 1:
                ComptV += 1
                i += DepV
            else:
                break
    ComptH = 0
    for DepH in [-1,1]:
        i = coord[0]
        j = coord[1] + DepH
        while True:
            if case_valide(murCoeff[num_joueur],i,j) and murCoeff[num_joueur][i][j] == 1:
                ComptH += 1
                j += DepH
            else:
                break

    if ComptH>0 and ComptV >0:
        Compteur = ComptH+ComptV+2
    else:
        Compteur = ComptH+ComptV +1
    score[num_joueur]+=Compteur

def CalculMalus(num_joueur, matP, score):
    for case in range(len(matP[num_joueur])):
        if matP[num_joueur][case] != '':
            if case <= 1:
                score[num_joueur] += -1
            elif case <=4:
                score[num_joueur] += -2
            else:
                score[num_joueur] += -3
        else:
            break

def VideEscalier(num_joueur, matE):
    for ligne in range(len(matE[num_joueur])):
        if matE[num_joueur][ligne][-2] != '':
            Tuile = matE[num_joueur][ligne][-2]
            for i in range(len(matE[num_joueur][ligne])):
                if matE[num_joueur][ligne][i] == Tuile:
                    matE[num_joueur][ligne][i] =''
                matE[num_joueur][ligne][-1] = 'FlecheR'

def CouleurDejaDansMur(tuile, LigneDuMur):
    '''Verifie si la couleur de la tuile à placer est déjà dans le mur ou non'''
    if tuile in LigneDuMur:
        return False
    return True

def ChoixSauvegarde():
    x,y = recup_clic()
    while True:
        if  longueur//4 < x < 3*longueur//4 and 2*hauteur//6 < y < 3*hauteur//6:
            return True
        elif longueur//4 < x < 3*longueur//4 and 4*hauteur//6 < y < 5*hauteur//6:
            return False
        x,y = recup_clic()

def ConditionFinDePartie(murCoeff):
    '''renvoie un mur si ce dernier rempli la condition de fin de partie'''
    for mur in range(len(murCoeff)):
        for ligne in murCoeff[mur]:
            if ligne == [1,1,1,1,1]:
                return mur

################## Calcul des bonus ############################################
def BonusScore(nbjoueur, score, murCoeff, matM):
    for i in range(nbjoueur):
        score[i] = BonusLigne(murCoeff[i],score[i])
        score[i] = BonusColonne(murCoeff[i],score[i])
        score[i] = BonusCouleur(matM[i], score[i])
    return score

def BonusLigne(matcoeff, score):
    for ligne in matcoeff:
        if ligne == [1,1,1,1,1]:
            score += 2
    return score

def BonusColonne(matcoeff, score):
    for i in range(len(matcoeff[0])):
        Colonne = True
        for j in range(len(matcoeff)):
            if matcoeff[j][i] == 0:
                Colonne = False
                break
        if Colonne:
            score += 7
    return score

def BonusCouleur(mur, score):
    Dico = {R :0, Bl :0, Bc:0, V:0, J:0}
    for ligne in mur:
        for case in ligne:
            if case == R:
                Dico[R]+=1
            elif case == Bl:
                Dico[Bl]+=1
            elif case == Bc:
                Dico[Bc]+=1
            elif case == V:
                Dico[V]+=1
            elif case == J:
                Dico[J]+=1
    for valeur in Dico.values():
        if valeur >= 5:
            score += 10
    return score

################################################################################

if __name__ == '__main__':

    num_joueur = 0

    cree_fenetre(longueur, hauteur)

########## Initialisation des matrices et affichage de l'ecran #################
    Save = 'Save.txt'
    DebutPartie()
    Choix = ChoixSauvegarde()
    if Choix:
        Fichier = input("Choisir le fichier contenant votre matrice ")
        murExemple, murJoueur = LectureMatDepart(Fichier)
        NbJoueur, ListeTypeJoueur, test = EcranChoixNbJoueur()
        sac = InitialiserSac()
        matF = RemplirFabrique(NbJoueur, sac)
        matM = InitialiserMurs(NbJoueur, murJoueur)
        matP = InitialiserPlanchers(NbJoueur)
        matE = InitialiserEscaliers(NbJoueur)
        matT = InitaliserCentreTable()
        score = InitialiserScore(NbJoueur)
        murCoeff = InitialiserCoeffMur(NbJoueur)
    else:
        NbJoueur,ListeTypeJoueur,sac,matF,matM,matP,matE,matT,score,murCoeff,murExemple,num_joueur,test = LectureFichierSauvegarde(Save)

################################################################################

######################### Boucle principale du jeu #############################
    update_ecran(NbJoueur,matM,matP,matE,matT,matF,score, num_joueur)
    #quadrillage()
    while True:
        EcritureFichierSauvegarde(Save, NbJoueur,ListeTypeJoueur,sac,matF,matM,matP,matE,matT,score,murCoeff,murExemple,num_joueur, test)
        tour_fini = DeroulementTour(NbJoueur, matF, num_joueur, matE[num_joueur], matT, matP[num_joueur], ListeTypeJoueur[num_joueur], matM, test)
        while not tour_fini:
            tour_fini = DeroulementTour(NbJoueur, matF, num_joueur, matE[num_joueur], matT, matP[num_joueur], ListeTypeJoueur[num_joueur], matM, test)
        num_joueur = alterner_joueur(num_joueur, NbJoueur)
        if rotation_finie(matF, matT):
            if len(sac)==0:
                sac=InitialiserSac()
            matF = RemplirFabrique(NbJoueur, sac)
            num_joueur = DeterminerPremierJoueur(matP)
            matT[0][0] = VJeton
            matP = FinDeRotation(NbJoueur, matE, matM, murCoeff, murExemple, score, matP)
        update_ecran(NbJoueur,matM,matP,matE,matT,matF,score, num_joueur)
        condition = ConditionFinDePartie(murCoeff)
        if condition != None:
            score = BonusScore(NbJoueur, score, murCoeff, matM)
            update_ecran(NbJoueur,matM,matP,matE,matT,matF,score, num_joueur)
            break

################################################################################
    # Afficher gagnant et score de chacun
    sleep(2)
    Dessine_ecran_fin(score, NbJoueur, condition)
    print('Cliquez n\'importe où sur l\'écran')
    attente_clic()
    ferme_fenetre()
