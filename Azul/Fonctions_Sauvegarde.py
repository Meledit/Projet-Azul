from Fonctions_Actualisation import *
from Fonctions_Graphique import *
from Fonctions_Initialisation import *
from Variable import *

def SauvegardeListe(Fichier, Lst):
    with open(Fichier, 'a') as f:
        for elem in Lst:
            f.write(str(elem) + '_')
        f.write('\n')

def SauvegardeDict(Fichier, Dico):
    with open(Fichier, 'a') as f:
        for key, value in Dico.items():
            f.write(str(key)+'_'+str(value)+'|')
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
    liste = []
    tmp = ''
    for lettre in ligne:
        if lettre != '_':
            tmp += lettre
        else:
            liste.append(tmp)
            tmp=''
    for i in range(len(liste)):
        if liste[i].isnumeric()or '-' in liste[i]:
            liste[i] = int(liste[i])
        elif liste[i] =='None':
            liste[i] = None
    return liste

def LectureDict(ligne):
    dico = dict()
    tmp = ''
    for lettre in ligne:
        if lettre == '|':
            tmpLst = tmp.split("_")
            dico[tmpLst[0]] = int(tmpLst[1])
            tmp=''
        else:
            tmp += lettre
    return dico

def LectureMatPart1(ligne):
    mat=[]
    tmp = ''
    for lettre in ligne:
        if lettre == '_':
            mat[-1].append(tmp)
            tmp = ''
        elif lettre == '|':
            mat.append([])
        else:
            tmp += lettre
    return mat

def LectureElem(ligne):
    tmp = ''
    for lettre in ligne:
        tmp += lettre
    elem = int(tmp)
    return elem

def LectureMat(ligne):
    mat = LectureMatPart1(ligne)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j].isnumeric() or '-' in mat[i][j]:
                mat[i][j] = int(mat[i][j])
            elif mat[i][j] =='None':
                mat[i][j] = None
    return mat

def LectureMatNiv3(ligne):
    grandeMat=[]
    tmp = ''
    for lettre in ligne:
        if lettre == ':':
            grandeMat.append([])
        elif lettre == '_':
            grandeMat[-1][-1].append(tmp)
            tmp = ''
        elif lettre == '|':
            grandeMat[-1].append([])
        else:
            tmp += lettre

    for i in range(len(grandeMat)):
        for j in range(len(grandeMat[i])):
            for k in range(len(grandeMat[i][j])):
                if grandeMat[i][j][k].isnumeric() or '-' in grandeMat[i][j][k]:
                    grandeMat[i][j][k] = int(grandeMat[i][j][k])
                elif grandeMat[i][j][k] =='None':
                    grandeMat[i][j][k] = None
    return grandeMat

def LectureFichierSauvegarde(save):
    with open(save, 'r') as save:
        nbJoueurs = LectureElem(save.readline())
        listeTypeJoueur = LectureListe(save.readline())
        sac = LectureDict(save.readline())
        fabriques = LectureMat(save.readline())
        murs = LectureMatNiv3(save.readline())
        planchers = LectureMat(save.readline())
        escaliers = LectureMatNiv3(save.readline())
        table = LectureListe(save.readline())
        score = LectureListe(save.readline())
        murExemple = LectureMat(save.readline())
        joueurAct = LectureElem(save.readline())
        test = LectureElem(save.readline())
        return nbJoueurs,listeTypeJoueur,sac,fabriques,murs,planchers,escaliers,table,score,murExemple,joueurAct, test


def EcritureFichierSauvegarde(save,nbJoueur,listeTypeJoueur,sac,fabriques,murs,planchers,escaliers,table,score,murExemple,numJoueur,test):
    with open(save, 'w') as fichier:
        fichier.write(str(nbJoueur) + '\n')
    SauvegardeListe(save,listeTypeJoueur)
    SauvegardeDict(save,sac)
    SauvegardeMat(save,fabriques)
    SauvegardeMat3Niveau(save,murs)
    SauvegardeMat(save,planchers)
    SauvegardeMat3Niveau(save,escaliers)
    SauvegardeListe(save,table)
    SauvegardeListe(save,score)
    SauvegardeMat(save,murExemple)
    with open(save, 'a') as fichier:
        fichier.write(str(numJoueur) + '\n')
        fichier.write(str(test) + '\n')

def TransfoMat(mat):
    matJoueur=[]
    matExemple=[]
    for i in range(len(mat)):
        matJoueur.append([])
        matExemple.append([])
        for j in range(len(mat[i])):
            if mat[i][j] == 'R':
                matJoueur[-1].append(RP)
                matExemple[-1].append(R)
            elif mat[i][j] =='Bc':
                matJoueur[-1].append(BcP)
                matExemple[-1].append(Bc)
            elif mat[i][j] =='V':
                matJoueur[-1].append(VP)
                matExemple[-1].append(V)
            elif mat[i][j] =='Bl':
                matJoueur[-1].append(BlP)
                matExemple[-1].append(Bl)
            elif mat[i][j] =='J':
                matJoueur[-1].append(JP)
                matExemple[-1].append(J)
    return matExemple,matJoueur

def LectureMatDepart(fichierMat):
    with open(fichierMat, 'r') as fichier:
        mat = fichier.readline()
        matString = LectureMatPart1(mat)
        matExemple, matJoueur = TransfoMat(matString)

        return matExemple, matJoueur
