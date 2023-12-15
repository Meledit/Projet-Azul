from Variable import *
import os
from Fonctions_Graphique import *
from Fonctions_Initialisation import *
from Fonctions_Sauvegarde import *
from time import *
from upemtk import *
from math import *
from random import choice
from functools import wraps, lru_cache
from inspect import *


######################################################################################################################
def lru_cache_possible(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        print("Appel de la fonction", str(f.__name__),":")
        arguments = signature(f).bind(*args, **kwargs).arguments
        hashable = True
        for key in arguments:
            if not arguments[key].__hash__:
                print('\t arg pas hashable : ',key)
                hashable = False
        if hashable:
            pass
            # print("\ttous les paramètres sont hashables, lru_cache est utilisable")
        else:
            print("\tcertains paramètres ne sont pas hashables, lru_cache est inutilisable")
        r = f(*args, **kwargs)
        return r
    return decoration

def ChoixNbJoueurs():
    ''' Determine le nombre de joueur, et le genre des joueurs en fonction de l'endroit où clique l'utilisateur '''
    x,y = RecupClic()
    test = 0
    if x < 6*longueur//9:
        if y < hauteur//3:
            nbJoueurs = 2
            ListeTypejoueur = ['Humain','Bot']
        elif y < 2*hauteur//3:
            nbJoueurs = 3
            ListeTypejoueur = ['Humain','Bot', 'Bot']
        else:
            nbJoueurs = 4
            ListeTypejoueur = ['Humain','Bot','Bot','Bot']
    else:
        nbJoueurs = 4
        ListeTypejoueur = ['Bot','Bot', 'Bot', 'Bot']
        test = 1
    return nbJoueurs, ListeTypejoueur, test

def RemplirFabriques(nbJoueurs, sac):
    ''' Récupère des tuiles du sac de manière aléatoire pour les mettre dans les fabriques'''
    def FonctionFiltre(key):
        return sac[key]>0
    zoneFabriques = []
    nbTuilesDansSac= sum(sac.values())
    couleursDispo = list(filter(FonctionFiltre, sac.keys()))
    for i in range((nbJoueurs * 2) + 1):
        zoneFabriques.append([])
        if nbTuilesDansSac<4:
            zoneFabriques[i] = []
        else:
            for j in range(4):
                couleur = choice(couleursDispo)
                zoneFabriques[i].append(couleur)
                sac[couleur] += -1
                if sac[couleur] == 0:
                    couleursDispo.remove(couleur)
            nbTuilesDansSac += -4
    return zoneFabriques

def Confirmer():
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
        coordonee = RecupClic()
        if minxJ < coordonee[0] < maxxJ and minyJ < coordonee[1] < maxyJ:
            return True
        if minxR < coordonee[0] < maxxR and minyR < coordonee[1] < maxyR:
            return False

def DeterminerFabriqueSelectionnee(coordonee, nbJoueurs):
    ''' Renvoie le numero de la fabrique selectionée en fonction du nombre de fabriques totale et de l'endroit où a cliqué le joueur'''
    NbDeFabriques =(nbJoueurs * 2) + 1
    if coordonee[1] < hauteur//15 +tailleC and coordonee[1] > hauteur//15 - tailleC:
        n = longueur // NbDeFabriques
        for i in range(NbDeFabriques):
            if coordonee[0] >(i*n + n//4 + tailleC - tailleC) and coordonee[0]<(i*n + n//4 + 2*tailleC):
                return i
        return None
    elif ClicValideTable(coordonee):
        return 10


def ClicValideFabrique(coordonee, numFabrique, nbJoueurs):
    ''' Verifie si le clic est dans une des fabriques '''
    n =(nbJoueurs * 2) + 1
    centreX =((longueur // n) // 4) +(numFabrique *(longueur // n)) + tailleC
    centreY =(hauteur // 15)
    minx = centreX - tailleC
    miny = centreY - tailleC
    maxx = centreX + tailleC
    maxy = centreY + tailleC
    if coordonee[0]  > minx and coordonee[0] < maxx and coordonee[1] > miny and coordonee[1] < maxy:
        return True
    else:
        return False

def DeterminerTuileSelectionnee(coordonne, M, numFabrique, nbJoueurs):
    ''' Détermine la couleur de la tuile où a cliqué le joueur'''
    n =(nbJoueurs * 2) + 1
    centreX =((longueur // n) // 4) +(numFabrique *(longueur // n)) + tailleC
    centreY =(hauteur // 15)
    if coordonne[0] < centreX and coordonne[0] > centreX - tailleC :
        x = 0
    elif coordonne[0] > centreX and coordonne[0] < centreX + tailleC :
        x = 1
    else:
        return None
    if coordonne[1] < centreY and coordonne[1] > centreY - tailleC:
        y = 0
    elif coordonne[1] > centreY and coordonne[1] < centreY + tailleC:
        y = 1
    else:
        return None

    if M[numFabrique] == []:
        return None

    if y == 0:
        return M[numFabrique][x + y]
    else:
        return M[numFabrique][x + y + 1]

def ActualiserFabrique(fabriques, numFabrique):
    ''' Vide la fabrique sélectionnée, pour que les cases ne soient pas dessiner'''
    fabriques[numFabrique] = []

def RecupClic():
    '''Récupère les coordonees du clic'''
    x, y, _ = attente_clic()
    return x, y

def ClicValideEscalier(coordonee, numJoueur):
    ''' Vérifie que le clic du joueur se trouve dans son escalier'''
    if numJoueur % 2 == 0:
        minX = longueur//10
    else:
        minX = 6 * longueur//10
    if numJoueur < 2:
        minY =  3*hauteur//15
    else:
        minY =  10*hauteur//15

    maxX = minX + 7 * tailleC
    maxY = minY + 4/6*tailleC + 5*tailleC

    return not(coordonee[0]  < minX or coordonee[0] > maxX or coordonee[1] < minY or coordonee[1] > maxY)


def DeterminerLigneSelectionnee(coordonee, numJoueur):
    ''' Détermine quel ligne d'escalier ou plancher le joueur a sélectionné'''
    if numJoueur %2 == 0:
        xDebutPlancher = longueur//10
    else:
        xDebutPlancher = 6*longueur//10

    xFinPlancher = xDebutPlancher + 8*tailleC

    if numJoueur < 2:
        debutPlancher =(3 * hauteur // 15) + 7/6*tailleC + 5*tailleC
        if int((coordonee[1] -(3 * hauteur // 15)) //(7/6 * tailleC)) < 5:
            return int((coordonee[1] -(3 * hauteur // 15)) //(7/6 * tailleC))
        elif coordonee[1]> debutPlancher and coordonee[1]<debutPlancher + tailleC and xDebutPlancher<coordonee[0] and coordonee[0]<xFinPlancher:
            return 5
    else:
        debutPlancher =(10 * hauteur // 15) + 7/6*tailleC + 5*tailleC
        if int((coordonee[1] -(10 * hauteur // 15)) //(7/6 * tailleC)) < 5:
            return int((coordonee[1] -(10 * hauteur // 15)) //(7/6 * tailleC))
        elif coordonee[1]> debutPlancher and coordonee[1] < debutPlancher + tailleC and xDebutPlancher<coordonee[0] and coordonee[0]<xFinPlancher:
            return 5


def SelectionTuilesEtFabrique(fabriques, nbJoueurs, table):
    '''Renvoie la tuile sélectionée, la fabrique où a été sélectionnée la tuile et le nombre de tuile de cette couleur dans la fabrique'''
    numFabrique = None
    while numFabrique == None:
        coordonee=RecupClic()
        numFabrique = DeterminerFabriqueSelectionnee(coordonee, nbJoueurs)
    if numFabrique == 10:
        tuile = DeterminerTuileSelectionnerDansTable(coordonee, table)
        nbTuiles = table.count(tuile)
        SurbrillanceTable(table, tuile)
        return numFabrique, tuile, nbTuiles, coordonee
    else:
        tuile = DeterminerTuileSelectionnee(coordonee, fabriques, numFabrique, nbJoueurs)
        nbTuiles = fabriques[numFabrique].count(tuile)
        SurbrillanceFabrique(fabriques, numFabrique, tuile)
        return numFabrique, tuile, nbTuiles, coordonee

def SelectionLigneEscalier(joueur):
    ''' Renvoie la ligne d'escalier ou le plancher selectionné par le joueur '''
    coordonee = RecupClic()
    ligneEscalier = DeterminerLigneSelectionnee(coordonee, joueur)
    if ligneEscalier == 5:
        return ligneEscalier
    else:
        while not ClicValideEscalier(coordonee, joueur):
            coordonee = RecupClic()
            ligneEscalier = DeterminerLigneSelectionnee(coordonee, joueur)
            if ligneEscalier == 5:
                break

    return ligneEscalier

def ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nbTuiles, ligneSelectionnee, table, plancher, genreJoueur):
    ''' Deplace les tuiles venant d'une fabrique vers le plateau d'un joueur si ce dernier a confirmer ce choix '''
    DessinerBoutons()
    if genreJoueur == 'Bot':
        aConfirme = True
    else:
        aConfirme = Confirmer()
    if aConfirme == False:
        UpdateEcran(nbJoueurs, murs, planchers, escaliers, table, fabriques, score, numJoueur)
        return False
    else:
        placeDispo =(len(ligneSelectionnee) - ligneSelectionnee.count(tuile) - 1)
        if placeDispo >= nbTuiles:
            tuileAPlaceDansEscalier =  nbTuiles
        else:
            tuileAPlaceDansEscalier = placeDispo

        FabriqueVersTable(table, fabriques[fabrique], tuile)
        ActualiserLigneEscalier(ligneSelectionnee, tuile, tuileAPlaceDansEscalier)
        ActualiserFabrique(fabriques, fabrique)

        if AssezDePlace(nbTuiles, ligneSelectionnee,tuile) == False:
            tuile_a_placer_dans_plancher=nbTuiles-tuileAPlaceDansEscalier
            ActualiserPlancher(plancher,tuile, tuile_a_placer_dans_plancher)
        UpdateEcran(nbJoueurs, murs, planchers, escaliers, table, fabriques, score, numJoueur)
        return True

def DeroulementTour(nbJoueurs, fabriques, joueur, escalier, table, plancher, genreJoueur, murs, test):
    ''' Deplace les tuiles sélectionnés, vers la zone sélectionnés puis renvoie True, une fois finie'''
    if genreJoueur == 'Humain':
        tuile = None
        while tuile == None:
            fabrique, tuile, nb_tuile, coordonee = SelectionTuilesEtFabrique(fabriques, nbJoueurs, table)
            if ClicValideFabrique(coordonee, fabrique, nbJoueurs):
                if tuile == None:
                    continue
                ligne_escalier = SelectionLigneEscalier(joueur)
                if ligne_escalier == 5:
                    SurbrillancePlancher(joueur)
                    return ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, plancher, table, plancher, genreJoueur)
                else:
                    while not LigneEscalierValide(tuile, escalier[ligne_escalier]) or not CouleurDejaDansMur(tuile, murs[joueur][ligne_escalier]):
                        ligne_escalier = SelectionLigneEscalier(joueur)
                        if ligne_escalier == 5:
                            SurbrillancePlancher(joueur)
                            return ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, plancher, table,plancher, genreJoueur)
                    SurbrillanceEscalier(escalier, ligne_escalier, joueur)
                    return ConfirmerDeplacementDepuisFabrique(fabrique, tuile, nb_tuile, escalier[ligne_escalier], table,plancher, genreJoueur)

            elif ClicValideTable(coordonee):
                tuile, nb_tuile = SelectionTuileTable(table, coordonee)
                if tuile == None:
                    break
                ligne_escalier = SelectionLigneEscalier(joueur)
                if ligne_escalier == 5:
                    SurbrillancePlancher(joueur)
                    return ConfirmerDeplacementDepuisTable(table, tuile, nb_tuile, plancher, plancher, genreJoueur)
                else:
                    while not LigneEscalierValide(tuile, escalier[ligne_escalier]) or not CouleurDejaDansMur(tuile, murs[joueur][ligne_escalier]):
                        ligne_escalier = SelectionLigneEscalier(joueur)
                        if ligne_escalier == 5:
                            SurbrillancePlancher(joueur)
                            return ConfirmerDeplacementDepuisTable(table, tuile, nb_tuile, plancher, plancher, genreJoueur)
                    SurbrillanceEscalier(escalier, ligne_escalier, joueur)
                    return ConfirmerDeplacementDepuisTable(table, tuile, nb_tuile, escalier[ligne_escalier],plancher, genreJoueur)

    elif genreJoueur == 'Bot':
        TourIA(fabriques,table,escaliers,planchers,numJoueur, genreJoueur, murs, test)
        return True

def ConfirmerDeplacementDepuisTable(table, tuile, nbTuiles, ligneSelectionnee, plancher, genreJoueur):
    ''' Deplace les tuiles venant du table vers le plateau d'un joueur si ce dernier a confirmer ce choix '''
    DessinerBoutons()
    if genreJoueur == 'Bot':
        aConfirme = True
    else:
        aConfirme = Confirmer()
    if aConfirme == False:
        UpdateEcran(nbJoueurs, murs, planchers, escaliers, table, fabriques, score, numJoueur)
        return False
    else:
        if tuile == VJeton:
            tuileAPlacerDansPlancher = 1
            ActualiserPlancher(plancher,tuile, tuileAPlacerDansPlancher)
        else:
            placeDispo =(len(ligneSelectionnee) - ligneSelectionnee.count(tuile) - 1)
            if placeDispo >= nbTuiles:
                tuileAPlaceDansEscalier =  nbTuiles
            else:
                tuileAPlaceDansEscalier = placeDispo

            ActualiserLigneEscalier(ligneSelectionnee, tuile, tuileAPlaceDansEscalier)

            if AssezDePlace(nbTuiles, ligneSelectionnee, tuile) == False:
                tuileAPlacerDansPlancher=nbTuiles-tuileAPlaceDansEscalier
                ActualiserPlancher(plancher,tuile, tuileAPlacerDansPlancher)

            if table[0] == VJeton:      #Code Hexadécimal du jeton -1
                JetonPremierJoueurVersPlancher(table, plancher)               
            
        ActualiserTable(table, tuile)
        UpdateEcran(nbJoueurs, murs, planchers, escaliers, table, fabriques, score, numJoueur)
        return True

def ActualiserTable(table, tuile):
    ''' Met à jour la matrice Table, en retirant les tuiles sélectionnées par le joueur, puis trie la matrice afin de mettre les None en fin de matrice '''

    nbDeTuile = table.count(tuile)
    for i in range(nbDeTuile):
        table.remove(tuile)
    table.sort()

def JetonPremierJoueurVersPlancher(table, plancher):
    ''' Envoie le jeton vert premier joueur, vers le plancher du joueur qui a pioché dans le table en premier'''
    if table[0] == VJeton:
        table.remove(VJeton)

    for m in range(len(plancher)):
        if plancher[m] == '':
           plancher[m] = VJeton
           break

def ClicValideTable(coordonee):
    ''' Verifie si le joueur a cliqué dans le table '''
    minX = 4*longueur//10
    minY = 7*hauteur//15
    maxX = minX + 8*tailleC
    maxY = minY +4*tailleC + 3*tailleC//6
    if coordonee[0]  < minX or coordonee[0] > maxX or coordonee[1] < minY or coordonee[1] > maxY:
        return False
    else:
        return True

def SelectionTuileTable(table,coordonee):
    '''Renvoie la tuile sélectionée et le nombre de tuile de cette couleur dans le table'''
    tuile = DeterminerTuileSelectionnerDansTable(coordonee, table)
    nbTuiles = table.count(tuile)
    SurbrillanceTable(table, tuile)
    return tuile, nbTuiles

def DeterminerTuileSelectionnerDansTable(coordonne, table):
    ''' Détermine la couleur de la tuile où a cliqué le joueur, s'il a cliqué dans le table'''
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
    if i*7+j > len(table)-1:
        return None
    return table[i*7+j]

def LigneEscalierValide(tuile, ligneEscalier):
    ''' Renvoie True, si la tuile peut être placé dans la ligne de l'escalier, et False si elle ne peut pas être placé'''
    if '' not in ligneEscalier:
        return False
    for i in range(len(ligneEscalier)):
        if ligneEscalier[i] not in [tuile, '', 'FlecheR', 'FlecheV']:
            return False
    return True

def FabriqueVersTable(table, fabrique, tuile):
    ''' Deplace les tuiles restantes dans la fabrique sélectionnée vers la table'''
    table.extend([x for x in fabrique if x != tuile ])

def AssezDePlace(nbTuiles, ligneEscalier, tuile):
    '''Renvoie True, si on peut placer toutes les tuiles sélectionnées dans la ligne d'escalier sélectionnée, et False sinon'''
    return not(nbTuiles >(len(ligneEscalier) - ligneEscalier.count(tuile) - 1))

def ActualiserPlancher(lstPlancher,tuile, tuileAPlacer):
    ''' Met les tuiles qui doivent aller dans le plancher dans ce dernier'''
    for j in range(tuileAPlacer):
        for i in range(len(lstPlancher)):
            if lstPlancher[i] == '':
                lstPlancher[i] = tuile
                break

def ActualiserLigneEscalier(ligneEscalier, tuile, nbTuiles):
    ''' Met autant de tuiles sélectionnés que possible dans la ligne escalier sélectionné'''
    longueurLigneEscalier = len(ligneEscalier)
    for i in range(nbTuiles):
        for j in range(longueurLigneEscalier):
            if ligneEscalier[j] != 'FlecheR' and ligneEscalier[j]  != 'FlecheV' and ligneEscalier[j] not in CouleurTuile and ligneEscalier[j] != VJeton :
                ligneEscalier[j] = tuile
                break


    if longueurLigneEscalier != 7:
        if '' not in ligneEscalier:
            if ligneEscalier[-1] == 'FlecheV':
                ligneEscalier[-1] = 'FlecheR'
            else:
                ligneEscalier[-1] = 'FlecheV'

@lru_cache(maxsize=None)
def AlternerJoueur(numJoueur, nbJoueurs):
    ''' Modifie le joueur jouant actuellement pour passer au joueur suivant'''
    newNumJoueur = numJoueur + 1
    if newNumJoueur > nbJoueurs - 1:
        return 0
    return newNumJoueur

def FabriquesVides(fabriques):
    ''' Renvoie True si toutes les fabriques sont vides'''
    n = len(fabriques)
    for i in range(n):
        if fabriques[i] != []:
            return False
    return True

def RotationFinie(fabriques, table):
    ''' Renvoie True, si la rotation actuelle est finie, c'est à dire s'il n'y a plus de tuiles dans les fabriques et dans la table'''
    return not(not FabriquesVides(fabriques) or table != [])

def TourIA(fabriques,table,escaliers,planchers,numJoueur, genreJoueur, murs, test):
    ''' Gère le tour d'un joueur IA de manière intelligente'''
    temps = 2.5
    if test == 1:
        temps = 0.5
    lstMarge=[0,-1,-2,1,2,-3,-4,3,4]
    for marge in lstMarge:
        tourFini = RemplirLignes(escaliers, murs, murExemple, table, planchers, numJoueur, genreJoueur, marge, temps)
        if tourFini:
            break
    if not tourFini:
        RecherchePourPlancher(table,planchers,fabriques,genreJoueur)
    UpdateEcran(nbJoueurs, murs, planchers, escaliers, table, fabriques, score, numJoueur)

def RemplirLignes(escaliers,mursJoueur, murExemple, table, planchers, numJoueur, genreJoueur, marge, temps):
    '''Remplit les lignes qui rapporte le plus de points'''
    for numLigne in range(len(escaliers[numJoueur])-1,-1,-1):
        if escaliers[numJoueur][numLigne][-2]=='':
            couleurAPrendre, casesARemplir = CasesAChercher(numLigne,murExemple[numLigne],mursJoueur[numJoueur][numLigne], escaliers[numJoueur][numLigne])
            casesARemplir = casesARemplir + marge
            if casesARemplir > 0:
                compteur,couleur,endroit,numFabrique = RechercheCase(couleurAPrendre, casesARemplir)
                if compteur!=None:
                    if endroit == "Table":
                        SurbrillanceTable(table,couleur)
                        SurbrillanceEscalier(escaliers[numJoueur], numLigne, numJoueur)
                        mise_a_jour()
                        sleep(temps)
                        ConfirmerDeplacementDepuisTable(table, couleur, compteur, escaliers[numJoueur][numLigne], planchers[numJoueur], genreJoueur)
                        return True
                    elif endroit =="Fabriques":
                        SurbrillanceFabrique(fabriques, numFabrique, couleur)
                        SurbrillanceEscalier(escaliers[numJoueur], numLigne, numJoueur)
                        mise_a_jour()
                        sleep(temps)
                        ConfirmerDeplacementDepuisFabrique(numFabrique, couleur, compteur, escaliers[numJoueur][numLigne], table, planchers[numJoueur], genreJoueur)
                        return True
    return False

def RecherchePourPlancher(table,planchers,fabriques,genreJoueur):
    '''Cherche le nombre de cases minimum, si l'IA est obligé de jouer dans le plancher'''
    nbCases = 1
    while True:
        compteur,couleur,endroit,numFabrique = RechercheCase(['#FF4040','#4C5EFF','#80C324','#E1E1E1','#FFCC43'],nbCases)
        if compteur!=None:
            if endroit == "Table":
                SurbrillanceTable(table,couleur)
                SurbrillancePlancher(numJoueur)
                mise_a_jour()
                ConfirmerDeplacementDepuisTable(table, couleur, compteur, planchers[numJoueur], planchers[numJoueur], genreJoueur)
                return 
            elif endroit =="Fabriques":
                SurbrillanceFabrique(fabriques, numFabrique, couleur)
                SurbrillancePlancher(numJoueur)
                mise_a_jour()
                ConfirmerDeplacementDepuisFabrique(numFabrique, couleur, compteur, planchers[numJoueur], table, planchers[numJoueur], genreJoueur)
                return 
        nbCases+=1 

def CasesAChercher(numLigneEscalier,ligneMurExemple,ligneMurJoueur,ligneEscalier):
    '''Définit le nombre de cases à chercher et leurs couleurs'''
    if ligneEscalier[-2-numLigneEscalier] != '':
        couleurAPrendre = [ligneEscalier[-2-numLigneEscalier]]
    else:
        couleurAPrendre=[]
        for case in range(len(ligneMurJoueur)):
            if ligneMurJoueur[case] != ligneMurExemple[case]:
                couleurAPrendre.append(ligneMurExemple[case])
    casesARemplir = ligneEscalier.count('')
    return couleurAPrendre, casesARemplir

def RechercheCase(LstCouleur, NbCases):
    '''L'IA cherche où elle peut trouver les cases dont elle a besoin'''
    nbFabriques = len(fabriques)
    for couleur in LstCouleur:
        compteur = table.count(couleur)
        if compteur == NbCases:
            endroit = "Table"
            return compteur,couleur,endroit, None
        for numFabrique in range(nbFabriques):
            compteur = fabriques[numFabrique].count(couleur)
            if compteur == NbCases:
                endroit = "Fabriques"
                return compteur,couleur,endroit,numFabrique
    return None, None, None, None

def DeterminerPremierJoueur(planchers):
    for i in range(len(planchers)):
        if VJeton in planchers[i]:
            return i

def FinDeRotation(nbJoueurs, escaliers, murs, murExemple, score, planchers):
    for numjoueur in range(nbJoueurs):
        ExaminerLigne(numjoueur,escaliers,murs,murExemple)
        VideEscalier(numjoueur,escaliers)
        CalculMalus(numjoueur, planchers, score)
    return InitialiserPlanchers(nbJoueurs)

def ExaminerLigne(numJoueur, escaliers, murs, murExemple):
    for ligne in range(len(escaliers[numJoueur])):
        if escaliers[numJoueur][ligne][-2] != '':
            tuile = escaliers[numJoueur][ligne][-2]
            ActualisationMatFinDeTour(murExemple, murs, numJoueur, ligne, tuile)

def ActualisationMatFinDeTour(murExemple, murs, numJoueur, ligne, tuile):
    for i in range(len(murExemple[ligne])):
        if murExemple[ligne][i] == tuile:
            CalculPointsUneCase(numJoueur,score, (ligne,i),murs)
            murs[numJoueur][ligne][i] = tuile
            break

@lru_cache(maxsize=None)
def CaseValide(n,i,j):
    return (0 <= i <= (n - 1) and 0 <= j <= (n - 1))

def CalculPointsUneCase(numJoueur, score, coord, mursJoueur):
    comptV = 0
    n = len(mursJoueur[numJoueur])
    for depV in [-1,1]:
        i = coord[0] + depV
        j = coord[1]
        while True:
            if CaseValide(n,i,j) and mursJoueur[numJoueur][i][j] == murExemple[i][j]:
                comptV += 1
                i += depV
            else:
                break
    comptH = 0
    for depH in [-1,1]:
        i = coord[0]
        j = coord[1] + depH
        while True:
            if CaseValide(n,i,j) and mursJoueur[numJoueur][i][j] == murExemple[i][j]:
                comptH += 1
                j += depH
            else:
                break

    if comptH>0 and comptV >0:
        compteur = comptH+comptV+2
    else:
        compteur = comptH+comptV +1
    score[numJoueur]+=compteur

def CalculMalus(numJoueur, planchers, score):
    for case in range(len(planchers[numJoueur])):
        if planchers[numJoueur][case] != '':
            if case <= 1:
                score[numJoueur] += -1
            elif case <=4:
                score[numJoueur] += -2
            else:
                score[numJoueur] += -3
        else:
            break

def VideEscalier(numJoueur,escaliers):
    for ligne in range(len(escaliers[numJoueur])):
        if escaliers[numJoueur][ligne][-2] != '':
            tuile = escaliers[numJoueur][ligne][-2]
            for i in range(len(escaliers[numJoueur][ligne])):
                if escaliers[numJoueur][ligne][i] == tuile:
                    escaliers[numJoueur][ligne][i] =''
            escaliers[numJoueur][ligne][-1] = 'FlecheR'

def CouleurDejaDansMur(tuile, ligneDuMur):
    '''Verifie si la couleur de la tuile à placer est déjà dans le mur ou non'''
    if tuile in ligneDuMur:
        return False
    return True

def ChoixSauvegarde():
    x,y = RecupClic()
    while True:
        if  longueur//4 < x < 3*longueur//4 and 2*hauteur//6 < y < 3*hauteur//6:
            return True
        elif longueur//4 < x < 3*longueur//4 and 4*hauteur//6 < y < 5*hauteur//6:
            return False
        x,y = RecupClic()

def ConditionFinDePartie(murJoueur):
    '''renvoie un mur si ce dernier rempli la condition de fin de partie'''
    for ligne in murJoueur:
        if ligne in murExemple:
            return True
    return False

################## Calcul des bonus ############################################
def BonusScore(nbjoueur, score, murs):
    for i in range(nbjoueur):
        score[i] = BonusLigne(murs[i],score[i])
        score[i] = BonusColonne(murs[i],score[i])
        score[i] = BonusCouleur(murs[i], score[i])
    return score

def BonusLigne(murJoueur, score):
    for ligne in range(len(murJoueur)):
        if murJoueur[ligne] == murExemple[ligne]:
            score += 2
    return score

def BonusColonne(murJoueur, score):
    n=len(murJoueur)

    for i in range(len(murJoueur)):
        Colonne = True
        for j in range(n):
            if murJoueur[j][i] != murExemple[j][i]:
                Colonne = False
                break
        if Colonne:
            score += 7
    return score

def BonusCouleur(mur, score):
    dico = {R :0, Bl :0, Bc:0, V:0, J:0}
    for ligne in mur:
        for case in ligne:
            if case == R:
                dico[R]+=1
            elif case == Bl:
                dico[Bl]+=1
            elif case == Bc:
                dico[Bc]+=1
            elif case == V:
                dico[V]+=1
            elif case == J:
                dico[J]+=1
    for valeur in dico.values():
        if valeur >= 5:
            score += 10
    return score

################################################################################

if __name__ == '__main__':

    numJoueur = 0

    cree_fenetre(longueur, hauteur)

########## Initialisation des matrices et affichage de l'ecran #################
    save = 'Save.txt'
    DebutPartie()
    choix = ChoixSauvegarde()
    if choix:
        fichier = input("Choisir le fichier contenant votre matrice ")
        # fichier = "MatriceC.txt"
        murExemple, murJoueur = LectureMatDepart(fichier)
        nbJoueurs, listeTypeJoueur, test = EcranChoixNbJoueur()
        sac = InitialiserSac()
        fabriques = RemplirFabriques(nbJoueurs, sac)
        murs = InitialiserMurs(nbJoueurs, murJoueur)
        planchers = InitialiserPlanchers(nbJoueurs)
        escaliers = InitialiserEscaliers(nbJoueurs)
        table = InitialiserTable()
        score = InitialiserScore(nbJoueurs)
    else:
        nbJoueurs,listeTypeJoueur,sac,fabriques,murs,planchers,escaliers,table,score,murExemple,numJoueur,test = LectureFichierSauvegarde(save)

################################################################################

######################### Boucle principale du jeu #############################
    UpdateEcran(nbJoueurs,murs,planchers,escaliers,table,fabriques,score, numJoueur)
    while True:
        EcritureFichierSauvegarde(save, nbJoueurs,listeTypeJoueur,sac,fabriques,murs,planchers,escaliers,table,score,murExemple,numJoueur, test)
        tourFini = DeroulementTour(nbJoueurs, fabriques, numJoueur, escaliers[numJoueur], table, planchers[numJoueur], listeTypeJoueur[numJoueur], murs, test)
        while not tourFini:
            tourFini = DeroulementTour(nbJoueurs, fabriques, numJoueur, escaliers[numJoueur], table, planchers[numJoueur], listeTypeJoueur[numJoueur], murs, test)
        numJoueur = AlternerJoueur(numJoueur, nbJoueurs)
        if RotationFinie(fabriques, table):
            if sum(sac.values())==0:
                sac=InitialiserSac()
            fabriques = RemplirFabriques(nbJoueurs, sac)
            numJoueur = DeterminerPremierJoueur(planchers)
            table.append(VJeton)
            planchers = FinDeRotation(nbJoueurs, escaliers, murs, murExemple, score, planchers)
        UpdateEcran(nbJoueurs,murs,planchers,escaliers,table,fabriques,score, numJoueur)
        condition = ConditionFinDePartie(murs[numJoueur])
        if condition:
            joueurStoppeurDeLaPartie = numJoueur
            score = BonusScore(nbJoueurs, score, murs)
            break

################################################################################
    # Afficher gagnant et score de chacun
    sleep(2)
    DessinerEcranFin(score, nbJoueurs, joueurStoppeurDeLaPartie)
    print('Cliquez n\'importe où sur l\'écran')
    attente_clic()
    ferme_fenetre()
