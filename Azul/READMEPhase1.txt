[Ce qui a été implementé]

- Un mode deux, trois, quatres joueur humains
- Un mode 1v1 contre l'ordinateur
- La selection des tuiles dans les fabriques et le table
- La selection d'une ligne de l'escalier ou du plancher
- Les tuiles vont automatiquement dans le plancher s'il n'y a plus de place dans les lignes
- La tuile verte va automatiquement dans le plancher du joueur ayant pioché dans le table en premier
- Selection du nombre de joueur dans un écran
- Le système de tour (le jeton vert n'as aucune incidence pour l'instant)


[L'oganisation du programme] 

-Le programme est séparé dans trois fichiers : 
	- Fonctions_Graphique qui contient toutes les fonctions liées à l'affichage (notamment le plateau, les fabriques, l'ecran de selection du nombre de joueur...)
	- Fonctions_Initialisation qui contient les fonctions créant les matrices, listes représentant les fabriques, planchers, table de table, score etc...
	- Fonctions_Actualisation qui contient les fonctions qui mettent à jour les matrices et listes en fonctions des actions des joueurs. Ce fichier contient aussi la boucle principale du jeu.


[Les choix techniques]

Dans le cas de la sélection/déselection, nous avons choisi de mettre en place deux boutons : Confirmer et Annuler, afin de confirmer ou
d'annuler le choix, car nous trouvions cela plus simple à mettre en place et plus intuitif pour le joueur.

Toujours dans le cas de la sélection, nous avons choisi de mettre en surbrillance les éléments sélectionnés, afin de permettre à l'utilisateur
de savoir ce qu'il a sélectionné, et qu'il ne se sentent pas perdu.

Nous avons également mis en surbrillance l'action de l'ordi, afin de permettre aux joueurs humains de mieux visualiser les choix de l'ordi.
A cette surbrillance s'ajoute un délai, pour laisser à l'utilisateur le temps de comprendre, le tour de l'ordinateur.

De plus quand une ligne d'escalier est complétée, la flèche au bout de cette ligne devient verte, afin de mieux visualiser les lignes complètes.

Nous avons également fait en sorte, que chaque fonctionnalités du jeu s'adapte à la taille de fenêtre choisie par l'utilisateur.
/!\ Cependant si l'utilisateur veut changer la taille de la fenêtre, il doit la changer dans tout les fichier

L'ordinateur ne possède pas à proprement parler d'IA, il joue de manière aléatoire, dans les limites qu'on lui autorise. (Par exemple, il arrive qu'il place volontairement les tuiles dans le plancher alors qu'il aurait pu les mettre dans l'escalier)


[Problèmes rencontrés] 

Un des problèmes rencontrés, a été la séparation des fonctions dans différents fichiers, car certaines fonctions apparaissaient comme non définies, alors qu'elles l'étaient. A certains moment celà faisait planter le programme
et à certains moment non. Il a été compliqué de déterminer si ce problème empéchait l'éxécution du programme, à l'heure actuelle ça n'est pas le cas sur nos machines. 



