from Fonctions_Actualisation import *
from Fonctions_Graphique import *
from Fonctions_Initialisation import *
from Variable import *

def SauvegardeListe(Fichier, Lst):
    with open(Fichier, 'a') as f:
        for elem in Lst:
            f.write(str(elem) + '_')
        f.write('\n')

def SauvegardeMat(Fichier, Mat):
     with open(Fichier, 'a') as f:
        for ligne in Mat:
            f.write('|')
            for elem in ligne:
                f.write(str(elem) + '_')
        f.write('\n')

def SauvegardeMat3Niveau(Fichier, Mat):
     with open(Fichier, 'a') as f:
        for matrice in Mat:
            f.write(':')
            for ligne in matrice:
                f.write('|')
                for elem in ligne:
                    f.write(str(elem) + '_')
        f.write('\n')

def LectureListe(ligne):
    Liste = []
    tmp = ''
    for lettre in ligne:
        if lettre != '_':
            tmp += lettre
        else:
            Liste.append(tmp)
            tmp=''
    for i in range(len(Liste)):
        if Liste[i].isnumeric()or '-' in Liste[i]:
            Liste[i] = int(Liste[i])
        elif Liste[i] =='None':
            Liste[i] = None
    return Liste

def LectureMatPart1(ligne):
    Mat=[]
    tmp = ''
    for lettre in ligne:
        if lettre == '_':
            Mat[-1].append(tmp)
            tmp = ''
        elif lettre == '|':
            Mat.append([])
        else:
            tmp += lettre
    return Mat

def LectureElem(ligne):
    tmp = ''
    for lettre in ligne:
        tmp+= lettre
    Elem = int(tmp)
    return Elem

def LectureMat(ligne):
    Mat = LectureMatPart1(ligne)
    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            if Mat[i][j].isnumeric() or '-' in Mat[i][j]:
                Mat[i][j] = int(Mat[i][j])
            elif Mat[i][j] =='None':
                Mat[i][j] = None
    return Mat

def LectureMatNiv3(ligne):
    GrandeMat=[]
    tmp = ''
    for lettre in ligne:
        if lettre == ':':
            GrandeMat.append([])
        elif lettre == '_':
            GrandeMat[-1][-1].append(tmp)
            tmp = ''
        elif lettre == '|':
            GrandeMat[-1].append([])
        else:
            tmp += lettre

    for i in range(len(GrandeMat)):
        for j in range(len(GrandeMat[i])):
            for k in range(len(GrandeMat[i][j])):
                if GrandeMat[i][j][k].isnumeric() or '-' in GrandeMat[i][j][k]:
                    GrandeMat[i][j][k] = int(GrandeMat[i][j][k])
                elif GrandeMat[i][j][k] =='None':
                    GrandeMat[i][j][k] = None
    return GrandeMat

def LectureFichierSauvegarde(Save):
    with open(Save, 'r') as Save:
        NbJoueur = LectureElem(Save.readline())
        ListeTypeJoueur = LectureListe(Save.readline())
        sac = LectureListe(Save.readline())
        matF = LectureMat(Save.readline())
        matM = LectureMatNiv3(Save.readline())
        matP = LectureMat(Save.readline())
        matE = LectureMatNiv3(Save.readline())
        matT = LectureMat(Save.readline())
        score = LectureListe(Save.readline())
        murCoeff = LectureMatNiv3(Save.readline())
        murExemple = LectureMat(Save.readline())
        joueur_act = LectureElem(Save.readline())
        test = LectureElem(Save.readline())
        return NbJoueur,ListeTypeJoueur,sac,matF,matM,matP,matE,matT,score,murCoeff,murExemple,joueur_act, test


def EcritureFichierSauvegarde(Save,NbJoueur,ListeTypeJoueur,sac,matF,matM,matP,matE,matT,score,murCoeff,murExemple,num_joueur,test):
    with open(Save, 'w') as Fichier:
        Fichier.write(str(NbJoueur) + '\n')
    SauvegardeListe(Save,ListeTypeJoueur)
    SauvegardeListe(Save,sac)
    SauvegardeMat(Save,matF)
    SauvegardeMat3Niveau(Save,matM)
    SauvegardeMat(Save,matP)
    SauvegardeMat3Niveau(Save,matE)
    SauvegardeMat(Save,matT)
    SauvegardeListe(Save,score)
    SauvegardeMat3Niveau(Save,murCoeff)
    SauvegardeMat(Save,murExemple)
    with open(Save, 'a') as Fichier:
        Fichier.write(str(num_joueur) + '\n')
        Fichier.write(str(test) + '\n')

def TransfoMat(mat):
    MatJoueur=[]
    MatExemple=[]
    for i in range(len(mat)):
        MatJoueur.append([])
        MatExemple.append([])
        for j in range(len(mat[i])):
            if mat[i][j] == 'R':
                MatJoueur[-1].append(RP)
                MatExemple[-1].append(R)
            elif mat[i][j] =='Bc':
                MatJoueur[-1].append(BcP)
                MatExemple[-1].append(Bc)
            elif mat[i][j] =='V':
                MatJoueur[-1].append(VP)
                MatExemple[-1].append(V)
            elif mat[i][j] =='Bl':
                MatJoueur[-1].append(BlP)
                MatExemple[-1].append(Bl)
            elif mat[i][j] =='J':
                MatJoueur[-1].append(JP)
                MatExemple[-1].append(J)
    return MatExemple,MatJoueur

def LectureMatDepart(FichierMat):
    with open(FichierMat, 'r') as Fichier:
        Mat = Fichier.readline()
        MatString = LectureMatPart1(Mat)
        MatExemple, MatJoueur = TransfoMat(MatString)

        return MatExemple, MatJoueur
