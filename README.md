# Manuel d'utilisation de l'algorithme au service de la classification du texte.

# Description:
Cet API permet de réaliser une classification de textes en utilisant l'algorithme KNN (K-nearest neighbors). Cet algorithme se compose de trois classes, TextVect, KNNClass, Main. Dans le ficher, "TextVect.py", il est responsable de transforme des textes en vecteurs au format TF-IDF, et de les stoker dans les données(data), et puis le ficher "KNNClass.py" fait appel aux données contenues dans data pour ajouter ou supprimer des classes, ajouter des vecteurs, les stocker ou les télécharger sous forme de fichiers json et classer le ficher texte. Et la fonction du ficher "Main.py" est mettre en œuvre les méthodes des deux fichiers précédents selon les instructions entrées par l'utilisateur. L'utilisateur peut saisir un fichier et choisir ce qu'il veut en faire, à savoir ajouter ou supprimer une classe, ajouter un vecteur, enregistrer ou télécharger des fichiers au format json, et classer le fichier. Si l'utilisateur choisit de classer le fichier, il continue à décider de la méthode à utiliser pour calculer la similarité des vecteurs, c'est-à-dire sim_cosinus, euclidean_distance ou manhattan_distance. Enfin, l'utilisateur doit déterminer le nombre de K pour déterminer le type de fichier.

# Utilisation
Lorsque nous exécutons le fichier "Main.py", on reçoit des instructions. D'abored, c'est "veillez taper le nom de documents："  mais ici on n'a qu'un choix "test", si on saisit quelque chose d'autre que "test", une exception sera levée, a savoir FileNotFoundError.

Ensuite, c'est "veillez donner votre ordonnance: (Choix parmi 'classify','add_class','add_vector','del_class','save','laod'): ",
['add_class'→"Veillez donner le label: " → "Veillez donner les vecteurs (sous forme de liste de dictionnaires): "  ](http://blog.csdn.net/guodongxiaren)  
             On va donner un type de ficher, tels que poésie, roman, article... Si le label existe dans le data, on renouvelle le vecteur, si il n'existe    pas, on ajouter cette classe dans le data. Mais quand on saisi les vecteurs, il faut respecter le format suivant, sinon l'ajout est un échec:

[  
{ "key_1_1_1": float_1_1_1, "key_1_1_2": float_1_1_2,... },  
{ "key_1_2_1": float_1_2_1, "key_1_2_2": float_1_2_2,... },  
...  
]  

'add_vector'
