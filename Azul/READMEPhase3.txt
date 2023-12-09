[Ce qui a été implémenté]

- Une Intelligence Artificielle, capable de donner du fil à retordre (du moins elle nous a battu souvent)

[Organisation du programme]

L'organisation du programme est la même que pour la phase 2, les fonctions liées à l'IA 
ont été intégrées au fichier Fonction_Actualisation.

[Comment l'IA choisit-elle ses coups]

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
		L'IA parcourt ensuite les fabriques et le table jusqu'à trouver un endroit contenant le bon nombre de cases de la bonne couleur.

	- Étape 5:
		Si l'IA à trouver à un endroit les tuiles dont elle a besoin, elle les joue. Sinon elle passe à la ligne d'escalier suivante, et recommence à l'étape 2.

	- Étape 6: 
		Dans le cas où l'IA n'a trouver aucune ligne pouvant être entièrement remplie, sans mettre de tuile dans le plancher, elle retourne à l'étape 1, en acceptant une marge d'erreur.

Les marges d'erreurs sont examinées dans l'ordre suivant : 
-1 -> -2 -> 1 -> 2 -> -3 -> -4 -> 3 -> 4

Un nombre négatif signifie qu'on accepte qu'il y ai ce nombre de cases vides dans l'escalier (par exemple la ligne 5, avec la marge -2, ne sera remplie que par 3 tuiles)
Un nombre positif signifie qu'on accepte que ce nombre de cases finisse dans le plancher (par exemple la ligne 3, avec la marge 1, sera entièrement remplie, mais une tuile ira dans le plancher)

	- Étape 7:
		Dans le cas où l'IA ne peut remplir de lignes, malgré les différentes marges d'erreurs possibles, elle cherchera dans les fabriques et dans le table, comment placer le moins de 
		tuiles possibles dans le plancher.

[Les choix techniques]

Un des choix techniques que nous avons fait, est le fait que l'IA essaie d'avoir le moins de tuiles possibles dans le plancher quoiqu'il en coûte, quitte ne pas remplir certaines lignes. De même
nous n'avons le système de bonus de points en fonction des lignes et colonnes. Tout de fois l'IA obtient un nombre corrects de bonus, car priorise le remplissage des couleurs à gauche du mur.