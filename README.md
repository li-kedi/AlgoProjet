# Manuel d'utilisation de l'algorithme au service de la classification du texte.

# Description:
Cet API permet de réaliser une classification de textes en utilisant l'algorithme KNN (K-nearest neighbors). Cet algorithme se compose de trois classes, TextVect, KNNClass, Main. Dans le ficher, "TextVect.py", il est responsable de transforme des textes en vecteurs au format TF-IDF, et de les stoker dans les données(data), et puis le ficher "KNNClass.py" fait appel aux données contenues dans data pour ajouter ou supprimer des classes, ajouter des vecteurs, les stocker ou les télécharger sous forme de fichiers json et classer le ficher texte. Et la fonction du ficher "Main.py" est mettre en œuvre les méthodes des deux fichiers précédents selon les instructions entrées par l'utilisateur. L'utilisateur peut saisir un fichier et choisir ce qu'il veut en faire, à savoir ajouter ou supprimer une classe, ajouter un vecteur, enregistrer ou télécharger des fichiers au format json, et classer le fichier. Si l'utilisateur choisit de classer le fichier, il continue à décider de la méthode à utiliser pour calculer la similarité des vecteurs, c'est-à-dire sim_cosinus, euclidean_distance ou manhattan_distance. Enfin, l'utilisateur doit déterminer le nombre de K pour déterminer le type de fichier.

# Utilisation

