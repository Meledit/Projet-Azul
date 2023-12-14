from Variable import *
from Fonctions_Sauvegarde import *
from Fonctions_Actualisation import *
from Fonctions_Graphique import *
from time import *
from upemtk import *
from math import *
from inspect import *


########################################################################################################
def InitialiserSac():
    ''' Initialise le sac qui est une liste contenant les 100 tuiles réparties en 5 couleurs différentes'''
    couleur = [Bl, J, R, V, Bc]
    sac = dict()
    for i in couleur:
        sac[i] = 20
    return sac

def Copie(T):
    if type(T)==list:
        M = []
        for elem in T:
            M.append(Copie(elem))
        return M
    else:
        M=T
        return M

def InitialiserMurs(nbJoueurs, murJoueur):
    '''Crée la matrice contenant les murs des quatre joueurs'''
    murs = []
    for i in range(nbJoueurs):
        nouvMur = Copie(murJoueur)
        murs.append(nouvMur)
    return murs

def CreerUnEscalier():
    '''Initialise l'escalier d'un joueur, comme étant une matrice avec des listes contenant None pour ne pas dessiner la case, et vide '' pour une case vide'''
    escalier = []
    for i in range(5):
        escalier.append([])
        for k in range(i+1):
            escalier[i].append('')
        escalier[i].append('FlecheR')            #Désigne La fleche quand la ligne n'est pas remplie.
    return escalier


def InitialiserEscaliers(nbJoueurs):
    '''Crée la matrice contenant les escaliers des quatre joueurs'''
    escaliers = []
    for i in range(nbJoueurs):
        escaliers.append(CreerUnEscalier())
    return escaliers

def InitialiserPlanchers(nbJoueurs):
    '''Créer les plancher des quatres joueurs, les planchers sont des listes contenant 'Vide' pour dessiner une case Vide'''
    planchers = []
    for i in range(nbJoueurs):
        planchers.append(['','','','','','',''])
    return planchers

def InitialiserTable():
    '''Initialise la matrice représentant le table de table, cette matrice ne contient que des None, sauf la première valeur qui est la case du jeton Premier Joueur (jeton vert)'''
    table = [VJeton]
    return table

def InitialiserScore(nbJoueurs):
    ''' Initialise la liste contenant les scores de chaque joueur, chaque joueur à un score de 0 au début'''
    Lst = [0]*nbJoueurs
    return Lst
