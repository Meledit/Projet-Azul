longueur = 1200
hauteur = 600

R = '#FF4040'
Bl = '#4C5EFF'
V = '#80C324'
Bc = '#E1E1E1'
J = '#FFCC43'


RP = '#6B5C5F'
BlP = '#6C6E7F'
VP = '#616956'
BcP = '#808080'
JP = '#766D59'

VJeton = '#96FABA'
Ombre = '212936'

CouleurTuile = [R, Bl, V, Bc, J]
CouleurJoueur = [R, Bl, J, V]
Vide = ""

HautCase =  (4*(hauteur//15)) // (43/6)           #38/3 et 43/6 correspond au nb de case à rentrer avec les espaces
LongCase = (3*(longueur//10)) // (38/3)
if HautCase <= LongCase:
    tailleC = HautCase
else:
    tailleC = LongCase
