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
    sac = []
    couleur = [Bl, J, R, V, Bc]
    nbCouleurs = len(couleur)
    for i in range(100):
        sac.append(couleur[i%nbCouleurs])
    return sac

def copie(T):
    if type(T)==list:
        M = []
        for elem in T:
            M.append(copie(elem))
        return M
    else:
        M=T
        return M

def InitialiserMurs(nbJoueurs, murJoueur):
    '''Crée la matrice contenant les murs des quatre joueurs'''
    murs = []
    for i in range(nbJoueurs):
        nouvMur = copie(murJoueur)
        murs.append(nouvMur)
    return murs

def Creer_Un_Escalier():
    '''Initialise l'escalier d'un joueur, comme étant une matrice avec des listes contenant None pour ne pas dessiner la case, et vide '' pour une case vide'''
    escalier = []
    for i in range(5):
        escalier.append([])
        # for j in range(5-i-1):
        escalier[i].extend([None]*(5-i-1))
            # Escalier[i].append(None)
        for k in range(i+1):
            escalier[i].append('')
        escalier[i].append('FlecheR')            #Désigne La fleche quand la ligne n'est pas remplie.
    return escalier

def InitialiserEscaliers(nbJoueurs):
    '''Crée la matrice contenant les escaliers des quatre joueurs'''
    escaliers = []
    for i in range(nbJoueurs):
        escaliers.append(Creer_Un_Escalier())
    return escaliers

def InitialiserPlanchers(nbJoueurs):
    '''Créer les plancher des quatres joueurs, les planchers sont des listes contenant 'Vide' pour dessiner une case Vide'''
    planchers = []
    for i in range(nbJoueurs):
        planchers.append(['','','','','','',''])
    return planchers

def InitialiserTable():
    '''Initialise la matrice représentant le table de table, cette matrice ne contient que des None, sauf la première valeur qui est la case du jeton Premier Joueur (jeton vert)'''
    table = 28*[None]
    table[0] = VJeton
    return table

def InitialiserScore(nbJoueurs):
    ''' Initialise la liste contenant les scores de chaque joueur, chaque joueur à un score de 0 au début'''
    Lst = []
    for i in range(nbJoueurs):
        Lst.append(0)
    return Lst

def InitialiserCoeffMur(nbJoueurs):
    matCM=[]
    for i in range(nbJoueurs):
        matCM.append([])
        for j in range(5):
            matCM[i].append([0,0,0,0,0])
    return matCM
