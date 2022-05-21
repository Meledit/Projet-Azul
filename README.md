# Azul-Project
Dans le contexte d'un projet étudiant, moi et un de mes camarades avons programmé en python une version du jeu de société Azul.

# Comment jouer ?
Lancer le fichier Fonctions_Actualisation et cliquez sur "nouvelle partie". Ensuite, entrez dans votre terminal le nom d'un des fichier txt qui va représenter le mur sur lequel vous jouerez (exemple : MatriceC.txt ou MatriceOndule.txt). Vous pouvez quitter la partie à tout moment, la partie sera sauvegarder automatiquement.

#Comment utiliser mes propres murs ?
Pour créer votre propre mur, il faut respecter les règles suivantes :
- Seules les couleurs de bases peuvent être utilisées (Bc pour blanc, R pour rouge, Bl pour bleu, V pour vert et enfin J pour jaune)
- Chaque couleur ne doit apparaître qu'une fois maximum par ligne.
- De plus pour déclarer votre mur, vous devez écrire | au début de chaque ligne du mur, et _ après chaque couleur, comme ci dessous.
|Bl_J_R_V_Bc_|Bc_Bl_J_R_V_|V_Bc_Bl_J_R_|R_V_Bc_Bl_J_|J_R_V_Bc_Bl_

- Le mur doit être écrit dans un fichier txt
- Pour utiliser ce mur, il suffit de rentrer le nom du fichier (ne pas oublier le .txt à la fin) dans le terminal au début de la partie.

#Comment l'IA fonctionne t-elle ?

Un tour d'IA se divise en plusieurs étapes:
	- Étape 1: 
		L'IA choisit la ligne nécssitant le plus de tuiles pour être remplie (5->4->3 ...)		
	- Étape 2:
		L'IA détermine les couleurs qui peuvent servir à remplir la ligne, si la ligne d'escalier possède déja une couleur de 
		tuile, alors l'IA cherchera cette même couleur. Sinon elle déterminera une liste de couleurs qui ne sont pas encore remplie 
		dans cette ligne du mur.
	- Étape 3:
		L'IA détermine le nombre de cases qu'elle doit chercher, en fonction du nombre de cases vides dans la ligne d'escalier.
	- Étape 4:
		L'IA parcourt ensuite les fabriques et le centre jusqu'à trouver un endroit contenant le bon nombre de cases de la bonne couleur.
	- Étape 5:
		Si l'IA à trouver à un endroit les tuiles dont elle a besoin, elle les joue. Sinon elle passe à la ligne d'escalier suivante, et recommence à l'étape 2.
	- Étape 6: 
		Dans le cas où l'IA n'a trouver aucune ligne pouvant être entièrement remplie, sans mettre de tuile dans le plancher, elle retourne à l'étape 1, en acceptant une marge d'erreur.
Les marges d'erreurs sont examinées dans l'ordre suivant : 
-1 -> -2 -> 1 -> 2 -> -3 -> -4 -> 3 -> 4

Un nombre négatif signifie qu'on accepte qu'il y ai ce nombre de cases vides dans l'escalier (par exemple la ligne 5, avec la marge -2, ne sera remplie que par 3 tuiles)
Un nombre positif signifie qu'on accepte que ce nombre de cases finisse dans le plancher (par exemple la ligne 3, avec la marge 1, sera entièrement remplie, mais une tuile ira dans le plancher)
	- Étape 7:
		Dans le cas où l'IA ne peut remplir de lignes, malgré les différentes marges d'erreurs possibles, elle cherchera dans les fabriques et dans le centre, comment placer le moins de 
		tuiles possibles dans le plancher.
