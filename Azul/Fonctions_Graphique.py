from Variable import *
from Fonctions_Actualisation import *
from Fonctions_Initialisation import *
from Fonctions_Sauvegarde import *
from time import *
from upemtk import *
from math import *


########################################################################################################
def Quadrillage():
    '''Fonction temporaire, permettant de repérer la position de chaque élément en s'adaptant à la taille de la fenêtre'''
    for i in range(11):
        ligne(i*longueur//10,0, i*longueur//10, hauteur, 'silver', 2)
    for i in range(16):
        ligne(0, i*hauteur//15, longueur,i*hauteur//15, 'silver', 2)


################### Ecran Nb Joueur ###################################################################
def EcranChoixNbJoueur():
    ''' Affiche l'écran de selection du nombre de joueur ( les rectangles à gauche désignent les modes de jeu contenant uniquement des joueurs humains, et le rectangle à droite le mode Humain vs Ordi)'''
    DessinerEcran()
    Dessiner2Joueurs()
    Dessiner3Joueurs()
    Dessiner4Joueurs()
    DessinerOrdi()
    nbJoueurs, listeTypejoueur, test = ChoixNbJoueurs()
    return nbJoueurs, listeTypejoueur, test

def DessinerEcran():
    '''Dessine les rectangles contenant les personnages et les écrans d'ordinateur sur l'écran de choix de nb de joueurs'''
    for i in range (3):
        y = i * hauteur // 3
        rectangle (0, y, longueur, y + hauteur //3, 'white', '#323342', 4)
    rectangle ((6 * longueur // 9), 0, longueur, hauteur, 'white', '#323342', 4)

def DessinerOrdi():
    '''Desssine un pictogramme d'écran d'ordinateur'''
    x = (13 * longueur // 18)
    y = (hauteur // 2)
    rectangle (x + (longueur // 9) // 8, y - (hauteur // 12), x + 16 * ((longueur // 9) // 8), y + (hauteur // 12), 'white', '', 4)
    rectangle (x + 2 * (longueur // 9) // 8, y - hauteur // 18, x + 15 * ((longueur // 9) // 8),  y + hauteur // 18, 'white', 'white', 4)
    rectangle (x + 4 * (longueur // 9) // 8, y + hauteur // 10, x + 13 * ((longueur // 9) // 8), y + hauteur // 9, 'white', 'white')


def Bonhomme(xInit, yInit, rayon, clr):
    '''Dessine un pictogramme de bonhomme au point d'encrage xInit, yInit le milieu de son corps'''
    rectangle (xInit - rayon, yInit - 1.5 * rayon, xInit + rayon, yInit + 1.5 * rayon, clr, '#323342', 4)
    cercle (xInit, yInit - 2.5 * rayon, 0.85 * rayon, clr, '#323342', 4 )
    ligne (xInit - rayon // 4, yInit - 2.8 * rayon, xInit - rayon // 4, yInit - 2.3 * rayon, clr, 4)
    ligne (xInit + rayon // 4, yInit - 2.8 * rayon, xInit + rayon // 4, yInit - 2.3 * rayon, clr, 4)

def Dessiner2Joueurs():
    '''Dessine deux pictogrammes de personnages'''
    Bonhomme((5 * longueur // 18), (2 * hauteur // 9), (longueur // 9) // 4, '#FF4040')
    Bonhomme((7 * longueur // 18), (2 * hauteur // 9), (longueur // 9) // 4, '#4C5EFF')

def Dessiner3Joueurs():
    '''Dessine trois pictogrammes de personnages'''
    Bonhomme((2 * longueur // 9), (5 * hauteur // 9), (longueur // 9) // 4, '#FF4040')
    Bonhomme((3 * longueur // 9), (5 * hauteur // 9), (longueur // 9) // 4, '#4C5EFF')
    Bonhomme((4 * longueur // 9), (5 * hauteur // 9), (longueur // 9) // 4, '#FFCC43')

def Dessiner4Joueurs():
    '''Dessine quatre pictogrammes de personnages'''
    for i in range(4):
        Bonhomme(((3 + 2 * i) * longueur // 18), (8 * hauteur // 9), (longueur // 9) // 4, CouleurJoueur[i])
####################################################################################################


################# Fonctions qui dessinent le ################################################
def Background():
    ''' Dessine le fond du plateau'''
    rectangle(0, 0, longueur, 2*hauteur//15, 'black', '#564267')
    rectangle(0, 2*hauteur//15, longueur, hauteur, 'black', '#323342')

def DessinerUneFabrique(lst, xInit, yInit):
    '''Dessine les quatres tuiles appartenant à une fabrique'''
    y = yInit-tailleC
    for i in range(len(lst) // 2):
        x = xInit +(i * tailleC)
        if lst[i] != None:
            rectangle(x, y, x + tailleC, y + tailleC, 'black', lst[i], 2)
        if lst[2 + i] != None:
            rectangle(x, y+tailleC, x + tailleC, y + 2*tailleC, 'black', lst[2 + i], 2)
            

def DessinerZoneFabrique():
    '''Dessine la ligne pour limiter la zone des fabriques'''
    ligne(0, 2 *(hauteur // 15), longueur, 2 *(hauteur // 15), 'white', 2)

def DessinerFabriques(M):
    '''Dessine la zone des fabriques entièrement (tuile, cercle, ligne)'''
    n = len(M)
    rayon = sqrt((tailleC ** 2) * 2) + 5
    xInit = longueur // n
    y = hauteur // 15
    for i in range(n):
        x =(xInit // 4) +(i * xInit)
        cercle(x + tailleC, y , rayon, 'white', '#323342', 2)
        DessinerUneFabrique(M[i], x, y)
    DessinerZoneFabrique()

def DessinerBoutons():
    '''Dessine les boutons confirmer et annuler'''
    x = 19 * longueur // 20
    y = 4 * hauteur // 15

    tableX = x +((longueur // 20) // 2)
    tableY = y +(2 * hauteur // 15)
    rayon =(longueur // 20) // 3

    rectangle(x, y, x + longueur // 10, 2 * y, 'white', J, 2)
    cercle(tableX, tableY, rayon, 'white', '', 4)

    y = 9* hauteur // 15
    tableY = 11*hauteur // 15
    rectangle(x, y, x + longueur // 10, y + 4 * hauteur//15, 'white', R, 2)
    ligne(tableX-rayon, tableY-rayon, tableX+rayon, tableY+rayon, 'white', 4)
    ligne(tableX-rayon, tableY+rayon, tableX+rayon, tableY-rayon, 'white', 4)

def DessinerTable(xInit, yInit, table):
    '''Dessine le table en fonction de la matrice fournie'''
    y = yInit
    x = xInit
    for i in range(len(table)):
        rectangle(x+tailleC, y+tailleC, x + 2*tailleC, y + 2*tailleC, '#212936', '#212936', 1)
        rectangle(x, y, x + tailleC, y + tailleC, 'white', table[i], 2)   
        x += 7*tailleC//6
        if i%7 == 6:
            x = xInit
            y += 7*tailleC//6

def DessinerUnMur(xInit,yInit,M):
    '''Dessine un mur, en partant du coin supérieur gauche de coordonnées (xInit, yInit) et de la matrice fournie'''
    longueurMur = len(M[0])
    for i in range(len(M)):
        y = yInit + i*tailleC + i*tailleC/6
        for j in range(longueurMur):
            x = xInit + j*tailleC + j*tailleC/6
            rectangle(x, y, x+tailleC, y+tailleC, "white", M[i][j], 2) 

def DessinerUnEscalier(xInit, yInit, M):
    '''Dessine un escalier, en partant du coin supérieur gauche de coordonnées (xInit, yInit) et de la matrice fournie'''
    for i in range(len(M)):
        y = yInit + i*tailleC + i*tailleC/6
        for j in range(len(M[i])):
            x = xInit + (4-i+j)*tailleC + (4-i+j)*tailleC/6
            if M[i][j] == 'FlecheR':
                polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#FF3B3B', '#F95330', 2)
            elif M[i][j] == 'FlecheV':
                polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#68EA87', '#80FF9E', 2)
            else:
                rectangle(x, y, x+tailleC, y+tailleC, "white", M[i][j], 2)

def DessinerUnPlancher(xInit,yInit, Lst):
    '''Dessine un plancher, en partant du coin supérieur gauche de coordonnées (xInit, yInit) et de la liste fournie'''
    for i in range(len(Lst)):
        x = xInit + i*tailleC + i*tailleC/6
        rectangle(x, yInit, x+tailleC, yInit+tailleC, "white", Lst[i], 2)
        if i < 2:
                TextePoints = '-1 pt'
        elif i < 5:
            TextePoints = '-2 pts'
        else:
            TextePoints = '-3 pts'
        texte(x, yInit, TextePoints, 'white', 'sw', "Arial", int(tailleC//3))

def EcrireScore(xInit, yInit, lst, numJoueur):
    '''Ecrit le score du joueur fournie en partant du coin supérieur gauche de coordonnées (xInit , yInit)'''
    AffichageScore = 'Score '+ str(lst[numJoueur])
    texte(xInit,yInit, AffichageScore, 'white', 'nw', "Arial", int(tailleC/2))

def DessinerUneFeuilleJoueur(xInit, yInit, murs, planchers, escaliers, lstScore, numJoueur):
    '''Dessine la feuille d'un joueur à partir des matrices et listes fournies'''
    x = xInit + 7*tailleC
    y = yInit + 7/6*tailleC + 5*tailleC
    DessinerOmbre(x + tailleC, yInit + tailleC, murs[numJoueur])
    DessinerOmbreEscaliers(xInit + tailleC, yInit + tailleC, escaliers[numJoueur])
    DessinerOmbrePlancher(xInit + tailleC, y + tailleC, planchers[numJoueur])
    DessinerUnEscalier(xInit, yInit, escaliers[numJoueur])
    DessinerUnMur(x, yInit,murs[numJoueur])
    DessinerUnPlancher(xInit, y, planchers[numJoueur])
    x += 2*tailleC
    EcrireScore(x, y, lstScore, numJoueur)

def DessinerLePlateauEntier(nbJoueur,murs, planchers, escaliers, table,fabriques, Score, numjoueur):
    '''Dessine les feuilles de tout les joueurs, la zone de fabrique et le table de table à partir des matrices et listes fournies'''
    DessinerFabriques(fabriques)
    DessinerTable(4 * longueur//10, 7 * hauteur//15, table)
    for i in range(nbJoueur):
        if i%2 == 0:
            x = longueur//10
        else:
            x = 6*longueur//10
        if i<2:
            y = 3*hauteur//15
        else:
            y = 10*hauteur//15
        DessinerUneFeuilleJoueur(x,y,murs, planchers, escaliers, Score, i)
        if numjoueur == i:
            Cadre(x - tailleC, y - tailleC, CouleurJoueur[numjoueur])

def UpdateEcran(NbJoueur, murs, planchers, escaliers, table, fabriques, lstScore, numjoueur):
    '''Mets à jour le plateau entier, à partir des matrices et listes fournies'''
    efface_tout()
    Background()
    DessinerLePlateauEntier(NbJoueur,murs, planchers, escaliers, table, fabriques, lstScore, numjoueur)
    Logo()
    mise_a_jour()

def Cadre(xInit, yInit, clr):
    rectangle(xInit, yInit, xInit + 15 * tailleC, yInit + 9 * tailleC, clr, '', 2)


###################################################################################################


######################## Ombres du plateau ########################################################
def DessinerOmbre(xInit, yInit, M):
    '''Dessine l'ombre d'une matrice'''
    longueurLigne =len(M[0])
    for i in range (len(M)):
        y = yInit + i * tailleC + i * tailleC/6
        for j in range (longueurLigne):
            x = xInit + j * tailleC + j * tailleC/6
            if M[i][j] == 'FlecheR' or M[i][j] == 'FlecheV':
                polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#212936', '#212936', 1)
            else:
                if M[i][j] == '':
                    rectangle(x, y, x + tailleC, y + tailleC, '#212936', '', 2)
                else:
                    rectangle(x, y, x + tailleC, y + tailleC, '#212936', '#212936', 1)

def DessinerOmbreEscaliers(xInit, yInit, M):
    '''Dessine l'ombre d'une matrice'''
    for i in range (len(M)):
        y = yInit + i * tailleC + i * tailleC/6
        for j in range (len(M[i])):
            x = xInit + (4-i+j)*tailleC + (4-i+j)*tailleC/6
            if M[i][j] == 'FlecheR' or M[i][j] == 'FlecheV':
                polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#212936', '#212936', 1)
            else:
                if M[i][j] == '':
                    rectangle(x, y, x + tailleC, y + tailleC, '#212936', '', 2)
                else:
                    rectangle(x, y, x + tailleC, y + tailleC, '#212936', '#212936', 1)

def DessinerOmbrePlancher(xInit, yInit, lst):
    '''Dessine l'ombre d'une liste'''
    for i in range (len(lst)):
        x = xInit + i * tailleC + i * tailleC/6
        if lst[i]=='':
            rectangle(x, yInit, x + tailleC, yInit + tailleC, '#212936', '', 2)
        else:
            rectangle(x, yInit, x + tailleC, yInit + tailleC, '#212936', '#212936', 1)
##################################################################################################

################### Surbrillance #################################################################
def SurbrillanceFabrique(fabriques, numfabriques, tuile):
    '''Met les tuiles sélectionnées dans la fabrique en surbrillance'''
    if tuile == None:
        return
    yInit = hauteur//15
    xInit = longueur//len(fabriques)
    y = yInit-tailleC
    for i in range(len(fabriques[numfabriques]) // 2):
        x =(xInit // 4) +(numfabriques * xInit) +i*tailleC
        if fabriques[numfabriques][i] == tuile:
            rectangle(x, y, x+tailleC, y+tailleC, '#F3FE62', '', 4)
        if fabriques[numfabriques][2+i] == tuile:
            rectangle(x, y+tailleC, x+tailleC, y+2*tailleC, '#F3FE62', '', 4)


def SurbrillanceTable(table, tuile):
    '''Met les tuiles sélectionnées dans le table en surbrillance'''
    if tuile == None:
        return
    xInit = 4*longueur//10
    y = 7*hauteur//15
    x = xInit
    for i in range(len(table)):
        if table[i] == tuile:
                rectangle(x, y, x+tailleC, y+tailleC, '#F3FE62', '', 4)
        x += 7*tailleC//6
        if i %7 == 6:
            x = xInit
            y += 7*tailleC//6

def SurbrillanceEscalier(escalier, numLigneEscalier, numJoueur):
    '''Met la ligne d'escalier sélectionné en surbrillance'''
    if numJoueur == 1 or numJoueur == 3:
        xInit = 6*longueur//10
    else:
        xInit = longueur//10

    if numJoueur == 0 or numJoueur == 1:
        yInit = 3*hauteur//15
    else:
        yInit = 10*hauteur//15

    y = yInit + numLigneEscalier*tailleC + numLigneEscalier*tailleC//6
    FinRectangle = xInit + 5*tailleC + 4*tailleC//6
    for i in range(len(escalier[numLigneEscalier])):
        x = xInit + (5-i)*tailleC + (5-i)*tailleC//6
    rectangle(x, y, FinRectangle, y+tailleC, '#F3FE62', '', 4)

def SurbrillancePlancher(numJoueur):
    '''Met le plancher en surbrillance s'il est sélectionné'''
    if numJoueur == 1 or numJoueur == 3:
        x = 6*longueur//10
    else:
        x = longueur//10

    if numJoueur == 0 or numJoueur == 1:
        y = 3*hauteur//15 + 5*tailleC + 4*tailleC//6 + tailleC//2
    else:
        y = 10*hauteur//15 + 5*tailleC + 4*tailleC//6 + tailleC//2
    rectangle(x, y, x+8*tailleC, y+tailleC, '#F3FE62', '', 4)

def BoutonNew():
    rectangle(longueur//4, 2*hauteur//6, 3*longueur//4, 3*hauteur//6, '#564267','#564267')
    texte(longueur//2, 2.5*hauteur//6 ,"Nouvelle Partie", 'white','center' , "arial", longueur//40)

def BoutonContinuer():
    rectangle(longueur//4, 4*hauteur//6, 3*longueur//4, 5*hauteur//6, '#564267','#564267')
    texte(longueur//2, 4.5*hauteur//6 ,"Continuer", 'white','center' , "arial", longueur//40)


def DebutPartie():
    '''Dessine et anime l'ecran de debut'''
    AnimationDebut()
    Titre()
    Bonhomme(3 * longueur // 25, 4 *  hauteur // 6, (2.5 * tailleC), R)
    Bonhomme(22 * longueur // 25, 4 *  hauteur // 6, (2.5 * tailleC), J)
    BoutonNew()
    BoutonContinuer()
    Logo()

def DessinerEcranFin(score, nbJoueurs, condition):
    ''' Dessine l'écran de fin avec les scores et les délais entre chaque apparition de texte'''
    rectangle(0, 0, longueur, hauteur, 'black', '#323342')
    Logo()
    y = hauteur // 12
    x = longueur // 50

    texte(x, y, 'Statistiques de jeu :', "white", 'nw', 'Arial', 40)

    lstG = ListeGagnant(score)
    lenLstG = len(lstG)
    prem = str(lstG[0][0] + 1) + ' avec ' + str(lstG[0][1]) + ' points.'
    deux = str(lstG[1][0] + 1) + ' avec ' + str(lstG[1][1]) + ' points.'
    if lenLstG >= 3:
        trois = str(lstG[2][0] + 1) + ' avec ' + str(lstG[2][1]) + ' points.'
    if lenLstG == 4:
        quat = str(lstG[3][0] + 1) + ' avec ' + str(lstG[3][1]) + ' points.'


    texte(x, 3 * y, '   Première place, joueur numéro ' + prem, CouleurJoueur[lstG[0][0]])
    sleep(1)
    mise_a_jour()
    texte(x, y * 4, '   Seconde place, joueur numéro ' + deux, CouleurJoueur[lstG[1][0]])
    sleep(1)
    mise_a_jour()
    if lenLstG >= 3:
        texte(x, y * 5, '   Troisième place, joueur numéro ' + trois, CouleurJoueur[lstG[2][0]])
        sleep(1)
        mise_a_jour()
    if lenLstG == 4:
        texte(x, y * 6, '   Quatrième place, joueur numéro ' + quat, CouleurJoueur[lstG[3][0]])
        sleep(1)
        mise_a_jour()

    texte(x, 8 * y, 'Le joueur numéro ' + str(condition + 1) + ' est le joueur ayant stoppé la partie', "white")
    sleep(1)
    mise_a_jour()

    texte(25 * x, 12 * (hauteur // 13), "Cliquez n'importe où", "gray", 'center', 'Arial', 15)
    sleep(1)
    mise_a_jour()

def Logo():
    '''Dessine le logo du jeu'''
    y = hauteur // 12
    x = longueur // 50
    for i in range(4):
        Bonhomme((i + 3) * (x // 3), (y // 3) * 35, (longueur // 20) // 4, CouleurJoueur[i])

def Titre():
    '''Dessine le titre du jeu et la ligne en dessous'''
    rectangle(0, 0, longueur, hauteur, 'black', '#323342')
    texte(longueur//2, hauteur//6 ,"Azul : The game", 'white','center' , "arial", longueur//30)
    ligne(0,  3 * hauteur//12, longueur,  3 * hauteur//12, "white", 3)

def ListeGagnant(lst):
    ''' renvoie une liste trié dans l'ordre décroissant'''
    lstG = []
    for i in range(len(lst)):
        lstG.append((i,lst[i]))

    lstG = sorted(lstG, key=lambda personne:personne[1], reverse=True)
    return lstG

def AnimationDebut():
    '''Anime la ligne au lancement du jeu'''
    rectangle(0, 0, longueur, hauteur, '#323342', '#323342')
    texte(longueur//2, hauteur//6 ,"Azul : The game", 'white','center', "arial", longueur//30)
    for i in range(50):
        x = longueur // 50
        ligne(x * i, 3 * hauteur//12, (i + 1) * x, 3 * hauteur//12, "white", 3)
        sleep(0.007)
        mise_a_jour()
    rectangle(0, 0, longueur, hauteur, "white", "white")
    mise_a_jour()
    sleep(0.02)

###################################################################################################
if __name__ == '__main__':
    cree_fenetre(longueur, hauteur)
    DebutPartie()
    attente_clic()
    ferme_fenetre()
