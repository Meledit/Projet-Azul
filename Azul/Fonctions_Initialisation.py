from Variable import *
from Fonctions_Sauvegarde import *
from Fonctions_Actualisation import *
from Fonctions_Graphique import *
from time import *
from upemtk import *
from math import *


########################################################################################################

def InitialiserSac():
    ''' Initialise le sac qui est une liste contenant les 100 tuiles réparties en 5 couleurs différentes'''
    Sac = []
    Couleur = [Bl, J, R, V, Bc]
    nb_couleur = len(Couleur)
    for i in range(100):
        Sac.append(Couleur[i%nb_couleur])
    return Sac

def copie(T):
    if type(T)==list:
        M = []
        for elem in T:
            M.append(copie(elem))
        return M
    else:
        M=T
        return M

def InitialiserMurs(NbJoueurs, murJoueur):
    '''Crée la matrice contenant les murs des quatre joueurs'''
    Murs = []
    for i in range(NbJoueurs):
        NouvMur = copie(murJoueur)
        Murs.append(NouvMur)
    return Murs

def Creer_Un_Escalier():
    '''Initialise l'escalier d'un joueur, comme étant une matrice avec des listes contenant None pour ne pas dessiner la case, et vide '' pour une case vide'''
    Escalier = []
    for i in range(5):
        Escalier.append([])
        for j in range(5-i-1):
            Escalier[i].append(None)
        for k in range(i+1):
            Escalier[i].append('')
        Escalier[i].append('FlecheR')            #Désigne La fleche quand la ligne n'est pas remplie.
    return Escalier

def InitialiserEscaliers(NbJoueurs):
    '''Crée la matrice contenant les escaliers des quatre joueurs'''
    Escaliers = []
    for i in range(NbJoueurs):
        Escaliers.append(Creer_Un_Escalier())
    return Escaliers

def InitialiserPlanchers(NbJoueurs):
    '''Créer les plancher des quatres joueurs, les planchers sont des listes contenant 'Vide' pour dessiner une case Vide'''
    Planchers = []
    for i in range(NbJoueurs):
        Planchers.append(['','','','','','',''])
    return Planchers

def InitaliserCentreTable():
    '''Initialise la matrice représentant le centre de table, cette matrice ne contient que des None, sauf la première valeur qui est la case du jeton Premier Joueur (jeton vert)'''
    CentreTable = []
    for i in range(4):
        CentreTable.append([None, None, None, None, None, None, None])
    CentreTable[0][0] = VJeton
    return CentreTable

def InitialiserScore(NbJoueurs):
    ''' Initialise la liste contenant les scores de chaque joueur, chaque joueur à un score de 0 au début'''
    Lst = []
    for i in range(NbJoueurs):
        Lst.append(0)
    return Lst

def InitialiserCoeffMur(NbJoueur):
    matCM=[]
    for i in range(NbJoueur):
        matCM.append([])
        for j in range(5):
            matCM[i].append([0,0,0,0,0])
    return matCM
