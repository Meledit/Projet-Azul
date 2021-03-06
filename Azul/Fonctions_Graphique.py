from Variable import *
from Fonctions_Actualisation import *
from Fonctions_Initialisation import *
from Fonctions_Sauvegarde import *
from time import *
from upemtk import *
from math import *
from random import randint


########################################################################################################
def quadrillage():
    '''Fonction temporaire, permettant de repérer la position de chaque élément en s'adaptant à la taille de la fenêtre'''
    for i in range(11):
        ligne(i*longueur//10,0, i*longueur//10, hauteur, 'silver', 2)
    for i in range(16):
        ligne(0, i*hauteur//15, longueur,i*hauteur//15, 'silver', 2)


################### Ecran Nb Joueur ###################################################################
def EcranChoixNbJoueur():
    ''' Affiche l'écran de selection du nombre de joueur ( les rectangles à gauche désignent les modes de jeu contenant uniquement des joueurs humains, et le rectangle à droite le mode Humain vs Ordi)'''
    Dessine_ecran()
    dessine_2joueur()
    dessine_3joueur()
    dessine_4joueur()
    dessine_ordi ()
    NbJoueur, ListeTypejoueur, test = Choix_Nb_Joueur()
    return NbJoueur, ListeTypejoueur, test

def Dessine_ecran():
    '''Dessine les rectangles contenant les personnages et les écrans d'ordinateur sur l'écran de choix de nb de joueurs'''
    for i in range (3):
        y = i * hauteur // 3
        rectangle (0, y, longueur, y + hauteur //3, 'white', '#323342', 4)
    rectangle ((6 * longueur // 9), 0, longueur, hauteur, 'white', '#323342', 4)

def dessine_ordi():
    '''Desssine un pictogramme d'écran d'ordinateur'''
    x = (13 * longueur // 18)
    y = (hauteur // 2)
    rectangle (x + (longueur // 9) // 8, y - (hauteur // 12), x + 16 * ((longueur // 9) // 8), y + (hauteur // 12), 'white', '', 4)
    rectangle (x + 2 * (longueur // 9) // 8, y - hauteur // 18, x + 15 * ((longueur // 9) // 8),  y + hauteur // 18, 'white', 'white', 4)
    rectangle (x + 4 * (longueur // 9) // 8, y + hauteur // 10, x + 13 * ((longueur // 9) // 8), y + hauteur // 9, 'white', 'white')


def bonhomme (xInit, yInit, rayon, clr):
    '''Dessine un pictogramme de bonhomme au point d'encrage xInit, yInit le milieu de son corps'''
    rectangle (xInit - rayon, yInit - 1.5 * rayon, xInit + rayon, yInit + 1.5 * rayon, clr, '#323342', 4)
    cercle (xInit, yInit - 2.5 * rayon, 0.85 * rayon, clr, '#323342', 4 )
    ligne (xInit - rayon // 4, yInit - 2.8 * rayon, xInit - rayon // 4, yInit - 2.3 * rayon, clr, 4)
    ligne (xInit + rayon // 4, yInit - 2.8 * rayon, xInit + rayon // 4, yInit - 2.3 * rayon, clr, 4)

def dessine_2joueur():
    '''Dessine deux pictogrammes de personnages'''
    bonhomme ((5 * longueur // 18), (2 * hauteur // 9), (longueur // 9) // 4, '#FF4040')
    bonhomme ((7 * longueur // 18), (2 * hauteur // 9), (longueur // 9) // 4, '#4C5EFF')

def dessine_3joueur():
    '''Dessine trois pictogrammes de personnages'''
    bonhomme ((2 * longueur // 9), (5 * hauteur // 9), (longueur // 9) // 4, '#FF4040')
    bonhomme ((3 * longueur // 9), (5 * hauteur // 9), (longueur // 9) // 4, '#4C5EFF')
    bonhomme ((4 * longueur // 9), (5 * hauteur // 9), (longueur // 9) // 4, '#FFCC43')

def dessine_4joueur():
    '''Dessine quatre pictogrammes de personnages'''
    for i in range(4):
        bonhomme (((3 + 2 * i) * longueur // 18), (8 * hauteur // 9), (longueur // 9) // 4, CouleurJoueur[i])
####################################################################################################


################# Fonctions qui dessinent le ################################################
def Background():
    ''' Dessine le fond du plateau'''
    rectangle(0, 0, longueur, 2*hauteur//15, 'black', '#564267')
    rectangle(0, 2*hauteur//15, longueur, hauteur, 'black', '#323342')

def Dessine_une_fabrique(lst, xInit, yInit):
    '''Dessine les quatres tuiles appartenant à une fabrique'''
    for i in range(len(lst) // 2):
        x = xInit +(i * tailleC)
        y = yInit-tailleC
        if lst[i] != None:
            rectangle(x, y, x + tailleC, y + tailleC, 'black', lst[i], 2)
    for i in range(len(lst) // 2):
        x = xInit +(i * tailleC)
        y = yInit
        if lst[2 + i] != None:
            rectangle(x, y, x + tailleC, y + tailleC, 'black', lst[2 + i], 2)

def Dessine_zone_fabrique():
    '''Dessine la ligne pour limiter la zone des fabriques'''
    ligne(0, 2 *(hauteur // 15), longueur, 2 *(hauteur // 15), 'white', 2)

def Dessine_MatF(M):
    '''Dessine la zone des fabriques entièrement (tuile, cercle, ligne)'''
    n = len(M)
    rayon = sqrt((tailleC ** 2) * 2) + 5
    xInit = longueur // n
    y = hauteur // 15
    for i in range(n):
        x =(xInit // 4) +(i * xInit)
        cercle(x + tailleC, y , rayon, 'white', '#323342', 2)
        Dessine_une_fabrique(M[i], x, y)
    Dessine_zone_fabrique()

def Dessine_boutons():
    '''Dessine les boutons confirmer et annuler'''
    x = 19 * longueur // 20
    y = 4 * hauteur // 15

    centrex = x +((longueur // 20) // 2)
    centrey = y +(2 * hauteur // 15)
    rayon =(longueur // 20) // 3

    rectangle(x, y, x + longueur // 10, 2 * y, 'white', J, 2)
    cercle(centrex, centrey, rayon, 'white', '', 4)

    y = 9* hauteur // 15
    centrey = 11*hauteur // 15
    rectangle(x, y, x + longueur // 10, y + 4 * hauteur//15, 'white', R, 2)
    ligne(centrex-rayon, centrey-rayon, centrex+rayon, centrey+rayon, 'white', 4)
    ligne(centrex-rayon, centrey+rayon, centrex+rayon, centrey-rayon, 'white', 4)

def Dessine_table(xInit, yInit, matT):
    '''Dessine le centre de table en fonction de la matrice fournie'''
    for i in range(len(matT)):
        y = yInit + i * tailleC + i * tailleC//6
        for j in range(len(matT[0])):
            x = xInit + j*tailleC + j * tailleC//6
            if matT[i][j] != None:
                rectangle(x, y, x + tailleC, y + tailleC, 'white', matT[i][j], 2)

def Dessine_Un_Mur(xInit,yInit,M):
    '''Dessine un mur, en partant du coin supérieur gauche de coordonnées (xInit, yInit) et de la matrice fournie'''
    for i in range(len(M)):
        y = yInit + i*tailleC + i*tailleC/6
        for j in range(len(M[0])):
            x = xInit + j*tailleC + j*tailleC/6
            rectangle(x, y, x+tailleC, y+tailleC, "white", M[i][j], 2)

def Dessine_Un_Escalier(xInit, yInit, M):
    '''Dessine un escalier, en partant du coin supérieur gauche de coordonnées (xInit, yInit) et de la matrice fournie'''
    for i in range(len(M)):
        y = yInit + i*tailleC + i*tailleC/6
        for j in range(len(M[0])):
            x = xInit + j*tailleC + j*tailleC/6
            if M[i][j] != None:
                if M[i][j] == 'FlecheR':
                    polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#FF3B3B', '#F95330', 2)
                elif M[i][j] == 'FlecheV':
                    polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#68EA87', '#80FF9E', 2)
                else:
                    rectangle(x, y, x+tailleC, y+tailleC, "white", M[i][j], 2)

def Dessine_Un_Plancher(xInit,yInit, Lst):
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

def EcrireScore(xInit, yInit, Lst, NumJoueur):
    '''Ecrit le score du joueur fournie en partant du coin supérieur gauche de coordonnées (xInit , yInit)'''
    AffichageScore = 'Score '+ str(Lst[NumJoueur])
    texte(xInit,yInit, AffichageScore, 'white', 'nw', "Arial", int(tailleC/2))

def Dessine_Une_Feuille_Joueur(xInit, yInit, MatM, MatP, MatE, LstScore, numJoueur):
    '''Dessine la feuille d'un joueur à partir des matrices et listes fournies'''
    x = xInit + 7*tailleC
    y = yInit + 7/6*tailleC + 5*tailleC
    dessine_ombre(x + tailleC, yInit + tailleC, MatM[numJoueur])
    dessine_ombre(xInit + tailleC, yInit + tailleC, MatE[numJoueur])
    dessine_ombre_P(xInit + tailleC, y + tailleC, MatP[numJoueur])
    Dessine_Un_Escalier(xInit, yInit, MatE[numJoueur])
    Dessine_Un_Mur(x, yInit,MatM[numJoueur])
    Dessine_Un_Plancher(xInit, y, MatP[numJoueur])
    x += 2*tailleC
    EcrireScore(x, y, LstScore, numJoueur)

def Dessine_Le_Plateau_Entier(nbJoueur,MatM, MatP, MatE, MatT,MatF, Score, numjoueur):
    '''Dessine les feuilles de tout les joueurs, la zone de fabrique et le centre de table à partir des matrices et listes fournies'''
    Dessine_MatF(MatF)
    dessine_ombre((4 * longueur//10) + tailleC,(7 * hauteur//15) + tailleC, MatT)
    Dessine_table(4 * longueur//10, 7 * hauteur//15, MatT)
    for i in range(nbJoueur):
        if i%2 == 0:
            x = longueur//10
        else:
            x = 6*longueur//10
        if i<2:
            y = 3*hauteur//15
        else:
            y = 10*hauteur//15
        Dessine_Une_Feuille_Joueur(x,y,MatM, MatP, MatE, Score, i)
        if numjoueur == i:
            Cadre(x - tailleC, y - tailleC, CouleurJoueur[numjoueur])

def update_ecran(NbJoueur, matM, matP, matE, matT, matF, LstScore, numjoueur):
    '''Mets à jour le plateau entier, à partir des matrices et listes fournies'''
    efface_tout()
    Background()
    Dessine_Le_Plateau_Entier(NbJoueur,matM, matP, matE, matT, matF, LstScore, numjoueur)
    logo()
    mise_a_jour()

def Cadre(xInit, yInit, clr):
    rectangle(xInit, yInit, xInit + 15 * tailleC, yInit + 9 * tailleC, clr, '', 2)


###################################################################################################


######################## Ombres du plateau ########################################################
def dessine_ombre(xInit, yInit, M):
    '''Dessine l'ombre d'une matrice'''
    for i in range (len(M)):
        y = yInit + i * tailleC + i * tailleC/6
        for j in range (len(M[0])):
            x = xInit + j * tailleC + j * tailleC/6
            if M[i][j] != None:
                if M[i][j] == 'FlecheR' or M[i][j] == 'FlecheV':
                    polygone([x, y ,x + tailleC, y + tailleC/2, x, y + tailleC], '#212936', '#212936', 1)
                else:
                    rectangle(x, y, x + tailleC, y + tailleC, '#212936', '#212936', 1)

def dessine_ombre_P(xInit, yInit, lst):
    '''Dessine l'ombre d'une liste'''
    for i in range (len(lst)):
        x = xInit + i * tailleC + i * tailleC/6
        if lst[i] != None:
            rectangle(x, yInit, x + tailleC, yInit + tailleC, '#212936', '#212936', 1)
##################################################################################################

################### Surbrillance #################################################################
def SurbrillanceFabrique(MatF, numMatF, tuile):
    '''Met les tuiles sélectionnées dans la fabrique en surbrillance'''
    if tuile == None:
        return
    yInit = hauteur//15
    xInit = longueur//len(MatF)
    for i in range(len(MatF[numMatF]) // 2):
        x =(xInit // 4) +(numMatF * xInit) +i*tailleC
        y = yInit-tailleC
        if MatF[numMatF][i] == tuile:
            rectangle(x, y, x+tailleC, y+tailleC, '#F3FE62', '', 4)
    for i in range(len(MatF[numMatF]) // 2):
        x =(xInit // 4) +(numMatF * xInit) +i*tailleC
        y = yInit
        if MatF[numMatF][2+i] == tuile:
            rectangle(x, y, x+tailleC, y+tailleC, '#F3FE62', '', 4)

def SurbrillanceCentre(Centre, tuile):
    '''Met les tuiles sélectionnées dans le centre en surbrillance'''
    if tuile == None:
        return
    xInit = 4*longueur//10
    yInit = 7*hauteur//15
    for i in range(len(Centre)):
        y = yInit + i*tailleC + i*tailleC//6
        for j in range(len(Centre[i])):
            x = xInit + j*tailleC + j*tailleC//6
            if Centre[i][j] == tuile:
                rectangle(x, y, x+tailleC, y+tailleC, '#F3FE62', '', 4)

def SurbrillanceEscalier(Escalier, NumLigneEscalier, NumJoueur):
    '''Met la ligne d'escalier sélectionné en surbrillance'''
    if NumJoueur == 1 or NumJoueur == 3:
        xInit = 6*longueur//10
    else:
        xInit = longueur//10

    if NumJoueur == 0 or NumJoueur == 1:
        yInit = 3*hauteur//15
    else:
        yInit = 10*hauteur//15

    y = yInit + NumLigneEscalier*tailleC + NumLigneEscalier*tailleC//6
    FinRectangle = xInit + 5*tailleC + 4*tailleC//6
    for i in range(len(Escalier[NumLigneEscalier])):
        x = xInit + i*tailleC + i*tailleC//6
        if Escalier[NumLigneEscalier][i] != None:
            rectangle(x, y, FinRectangle, y+tailleC, '#F3FE62', '', 4)
            break

def SurbrillancePlancher(NumJoueur):
    '''Met le plancher en surbrillance s'il est sélectionné'''
    if NumJoueur == 1 or NumJoueur == 3:
        x = 6*longueur//10
    else:
        x = longueur//10

    if NumJoueur == 0 or NumJoueur == 1:
        y = 3*hauteur//15 + 5*tailleC + 4*tailleC//6 + tailleC//2
    else:
        y = 10*hauteur//15 + 5*tailleC + 4*tailleC//6 + tailleC//2
    rectangle(x, y, x+8*tailleC, y+tailleC, '#F3FE62', '', 4)

def bouton_new():
    rectangle(longueur//4, 2*hauteur//6, 3*longueur//4, 3*hauteur//6, '#564267','#564267')
    texte(longueur//2, 2.5*hauteur//6 ,"Nouvelle Partie", 'white','center' , "arial", longueur//40)

def bouton_continuer():
    rectangle(longueur//4, 4*hauteur//6, 3*longueur//4, 5*hauteur//6, '#564267','#564267')
    texte(longueur//2, 4.5*hauteur//6 ,"Continuer", 'white','center' , "arial", longueur//40)


def DebutPartie():
    '''Dessine et anime l'ecran de debut'''
    animation_debut()
    titre()
    bonhomme(3 * longueur // 25, 4 *  hauteur // 6, (2.5 * tailleC), R)
    bonhomme(22 * longueur // 25, 4 *  hauteur // 6, (2.5 * tailleC), J)
    bouton_new()
    bouton_continuer()
    logo()

def Dessine_ecran_fin(score, NbJoueurs, condition):
    ''' Dessine l'écran de fin avec les scores et les délais entre chaque apparition de texte'''
    rectangle(0, 0, longueur, hauteur, 'black', '#323342')
    logo()
    y = hauteur // 12
    x = longueur // 50

    texte(x, y, 'Statistiques de jeu :', "white", 'nw', 'Arial', 40)

    lst_g = liste_gagnant(score)
    prem = str(lst_g[0][0] + 1) + ' avec ' + str(lst_g[0][1]) + ' points.'
    deux = str(lst_g[1][0] + 1) + ' avec ' + str(lst_g[1][1]) + ' points.'
    if len(lst_g) >= 3:
        trois = str(lst_g[2][0] + 1) + ' avec ' + str(lst_g[2][1]) + ' points.'
    if len(lst_g) == 4:
        quat = str(lst_g[3][0] + 1) + ' avec ' + str(lst_g[3][1]) + ' points.'


    texte(x, 3 * y, '   Première place, joueur numéro ' + prem, CouleurJoueur[lst_g[0][0]])
    sleep(1)
    mise_a_jour()
    texte(x, y * 4, '   Seconde place, joueur numéro ' + deux, CouleurJoueur[lst_g[1][0]])
    sleep(1)
    mise_a_jour()
    if len(lst_g) >= 3:
        texte(x, y * 5, '   Troisième place, joueur numéro ' + trois, CouleurJoueur[lst_g[2][0]])
        sleep(1)
        mise_a_jour()
    if len(lst_g) == 4:
        texte(x, y * 6, '   Quatrième place, joueur numéro ' + quat, CouleurJoueur[lst_g[3][0]])
        sleep(1)
        mise_a_jour()

    texte(x, 8 * y, 'Le joueur numéro ' + str(condition + 1) + ' est le joueur ayant stoppé la partie', "white")
    sleep(1)
    mise_a_jour()

    texte(25 * x, 12 * (hauteur // 13), "Cliquez n'importe où", "gray", 'center', 'Arial', 15)
    sleep(1)
    mise_a_jour()

def logo():
    '''Dessine le logo du jeu'''
    y = hauteur // 12
    x = longueur // 50
    for i in range(4):
        bonhomme ((i + 3) * (x // 3), (y // 3) * 35, (longueur // 20) // 4, CouleurJoueur[i])

def titre():
    '''Dessine le titre du jeu et la ligne en dessous'''
    rectangle(0, 0, longueur, hauteur, 'black', '#323342')
    texte(longueur//2, hauteur//6 ,"Azul : The game", 'white','center' , "arial", longueur//30)
    ligne(0,  3 * hauteur//12, longueur,  3 * hauteur//12, "white", 3)

def liste_gagnant(lst):
    ''' renvoie une liste trié dans l'ordre décroissant'''
    lst_g = []
    lst_verif = []
    for rep in range(len(lst)):
        max = -10000
        pos = 3
        for i in range(len(lst)):
            if i not in lst_verif:
                if lst[i] >= max:
                    max = lst[i]
                    pos = i

        lst_g.append((pos, max))
        lst_verif.append(pos)
    return lst_g

def animation_debut():
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
