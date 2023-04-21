# Manuel d'utilisation de l'algorithme au service de la classification du texte.

## Description:
Cet API permet de réaliser une classification de textes en utilisant l'algorithme KNN (K-nearest neighbors). Cet algorithme se compose de trois classes, TextVect, KNNClass, Main. Dans le ficher, "TextVect.py", il est responsable de transforme des textes en vecteurs au format TF-IDF, et de les stoker dans les données(data), et puis le ficher "KNNClass.py" fait appel aux données contenues dans data pour ajouter ou supprimer des classes, ajouter des vecteurs, les stocker ou les télécharger sous forme de fichiers json et classer le ficher texte. Et la fonction du ficher "Main.py" est mettre en œuvre les méthodes des deux fichiers précédents selon les instructions entrées par l'utilisateur. L'utilisateur peut saisir un fichier et choisir ce qu'il veut en faire, à savoir ajouter ou supprimer une classe, ajouter un vecteur, enregistrer ou télécharger des fichiers au format json, et classer le fichier. Si l'utilisateur choisit de classer le fichier, il continue à décider de la méthode à utiliser pour calculer la similarité des vecteurs, c'est-à-dire sim_cosinus, euclidean_distance ou manhattan_distance. Enfin, l'utilisateur doit déterminer le nombre de K pour déterminer le type de fichier.

## Utilisation
Lorsque nous exécutons le fichier "Main.py", on reçoit des instructions. D'abored, c'est ["veillez taper le nom de documents："](http://blog.csdn.net/guodongxiaren) mais ici on n'a qu'un choix "test", si on saisit quelque chose d'autre que "test", une exception sera levée, a savoir FileNotFoundError.

Ensuite, c'est ["veillez donner votre ordonnance: (Choix parmi 'classify','add_class','add_vector','del_class','save','laod'): "](http://blog.csdn.net/guodongxiaren),

  * ['add_class'→"Veillez donner le label: " → "Veillez donner les vecteurs (sous forme de liste de dictionnaires): "  ](http://blog.csdn.net/guodongxiaren)  

    On va donner un type de ficher, tels que poésie, roman, article... Si le label existe dans le data, on renouvelle le vecteur, si il n'existe    pas, on ajouter cette classe dans le data. Mais quand on saisi les vecteurs, il faut respecter le format suivant, sinon l'ajout est un échec:

    [  
    { "key_1_1_1": float_1_1_1, "key_1_1_2": float_1_1_2,... },  
    { "key_1_2_1": float_1_2_1, "key_1_2_2": float_1_2_2,... },  
    ...  
    ]  

  * ['add_vector'→"Veillez donner le label: "→"Veillez donner les vecteurs (sous forme de liste de dictionnaires): "](http://blog.csdn.net/guodongxiaren)


     Il faut s'assurer que le label saisi existe bien dans les données, sinon une exception sera levée, ValueError. Et le format des vecteurs est la même que précédemment.
     
  * [‘del_class’→"Veillez donner le label: "](http://blog.csdn.net/guodongxiaren) 
  

     Il faut s'assurer que le label saisi existe bien dans les données, sinon une exception sera levée, ValueError.
     
  *  ['save'→"Veillez donner le nom du fichier JSON de sauvegarde: "](http://blog.csdn.net/guodongxiaren)
     
     Il vaut mieux entrer un fichier json, mais même si ce n'est pas le cas, il sera modifié en fichier json.
     
     
  *  ['laod'→ "Veillez donner le nom du fichier JSON de chargement: "](http://blog.csdn.net/guodongxiaren)

     Veillez que le fichier d'entrée existe et qu'il s'agit d'un fichier json, sinon une exception sera levée.

  *  ['classify'→“ veillez taper le nom de documents” → " Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): " → "Veuillez indiquer la valeur de k: "](http://blog.csdn.net/guodongxiaren)


      * “veillez taper le nom de documents” 
    
          Notez ici que le type de fichier d'entrée est un fichier txt.
          
      * "Veuillez indiquer la méthode de calcul"

         Notez que des méthodes de calcul différentes donneront des résultats différents.
         
         Cosinus: La valeur est proche de 1, plus les deux vecteurs sont similaires.
         
         Euclidean_distance & manhattan_distance : Plus la valeur est élevée, plus les deux vecteurs sont similaires.
         
      * "Veuillez indiquer la valeur de k: "
 
         C'est-à-dire le nombre de résultats à conserver.
         
        
## La structure de fichier et donnée：


  ### Dossiers
  
     Document - Test

Il s'agit d'un dossier contenant plusieurs sous-dossiers destinés à tester le programme. Les sous-dossiers sont intitulés 'romen','article','pièce de théâtre','poésie', et chacun contient huit fichiers. Les noms de sous-dossiers sont des labels enregistrés dans les données alors que les fichers sont des vecteurs des labels correspondants dans les données.

Il est possible de créer de nouveaux sous-dossiers et leurs fichiers, ou d'ajouter des fichiers à des sous-dossiers correspondants agrandir le document Test.


     Fichers.py
    

* **TextVect.py**

  * Transforme des textes en vecteurs au format TF-IDF, et de les stoker dans les données(data)

* **KNNClass.py**

  * Fait appel aux données contenues dans data pour ajouter ou supprimer des classes, ajouter des vecteurs, les stocker ou les télécharger sous forme de fichiers json et classer le ficher texte. 
  
* **Main.py**

  * Mettre en œuvre les méthodes des deux fichiers précédents selon les instructions entrées par l'utilisateur.
  
* **stop_words_french.txt**

  * Il est utilisé pour filtrer les documents.
  
* **BOU.txt**
* **LM.txt**

  * Les deux fichers sont utilisés pour tester la classification.



## API
### TextVect.py
Description:</br>
Le code comprend plusieurs méthodes de classe pour effectuer des tâches de traitement de texte telles que la tokenisation, la vectorisation et le filtrage.

* **def read_dict(stoplist_filename)**
  * Description: Cette méthode lit un fichier de liste de stop words et renvoie un ensemble de stop words
  * stoplist_filename : nom du fichier de stop words
  * return : un ensemble de stop words
* **def tokenize(text,tok_grm)**
  * Description: Cette méthode tokenize un texte avec une expression régulière 
  * Text: Ficher texte à tokenizer
  * Tok_grm : Les expressions régulières pour tokenizer le texte
  * Return : liste des tokens
* **def vectorise(tokens)**
  * Description: Cette méthode transforme une liste de tokens en un dictionnaire avec leur fréquence associée
  * Liste des tokens à transformer en dictionnaire
  * Return : dictionnaire contenant les fréquences des tokens
* **def doc2vec(cls,label:str)**
  * Description: Cette méthode convertit tous les fichiers textes d'un dossier en vecteurs en utilisant la méthode de vectorisation
  * Label : nom du dossier contenant les fichiers textes
  * Return : un dictionnaire contenant le nom du dossier et la liste des vecteurs de chaque fichier texte
* **def txt2vec(cls,file_name:str)**
  * Description: Cette méthode convertit un fichier texte en un vecteur de mots
  * File_name (str): Le nom du fichier texte à convertir.
  * Return: Un dictionnaire contenant le label du fichier et sa représentation sous forme de vecteur de mots.
* **def filtrage(cls,stoplist_filename, documents, non_hapax)**
  * Description: Cette méthode effectue le filtrage des tokens d'un document
  * stoplist_filename : nom du fichier de stop words
  * documents : dictionnaire contenant les informations du document
  * non_hapax : booléen pour déterminer si on élimine les hapax ou non
  * return : dictionnaire contenant les informations du document filtré
* **def tf_idf(documents:list)->list**
  * Description: Cette méthode effectue le calcul du poids tf-idf de chaque mot dans chaque document
  * Documents: une liste de documents contenant les vecteurs de mots et les libellés
  * une liste de documents modifiés avec les poids tf-idf pour chaque mot
* **def scalaire(vector1,vector2) -> float**
  * Description: Cette fonction calcule le produit scalaire
  * vector1: un dictionnaire représentant le premier vecteur
  * vector2: un dictionnaire représentant le deuxième vecteur
* **def norme(vector)-> float**
  * Description: Cette fonction calcule la norme d'un vecteur donné.
  * Vector: Un dictionnaire représentant le vecteur dont on souhaite calculer la norme.
  * return : la norme du vecteur donné. 
* **def sim_cosinus(cls,vector1,vector2)-> float**
  * Description: Cette méthode calcule la similarité cosinus entre deux vecteurs
  * vector1 : un dictionnaire représentant le premier vecteur.
  * vector2 : un dictionnaire représentant le deuxième vecteur
  * Return : la similarité cosinus entre les deux vecteurs donnés.
* **def euclidean_distance(vec1: dict, vec2: dict) -> float**
  * Description: Cette fonction calcule la distance euclidienne entre deux vecteurs donnés
  * vec1 : un dictionnaire représentant le premier vecteur.
  * vec2 : un dictionnaire représentant le deuxième vecteur
  * return : la distance euclidienne entre les deux vecteurs donnés.
* **def manhattan_distance(vec1: dict, vec2: dict) -> float**
  * Description: Cette fonction calcule la distance manhattan entre deux vecteurs donnés
  * vec1 : un dictionnaire représentant le premier vecteur
  * vec2 : un dictionnaire représentant le deuxième vecteur
  * return : la distance manhattan entre les deux vecteurs donnés.
* **def doc2tf_idf(cls)**
  * Description: Cette fonction calcule le score tf-idf pour chaque document d'un corpus donné.
  * documents_input (str): le nom d'un document ou "test" si l'on veut traiter plusieurs documents.
  * Retour: <br />
    resultat_tfidf (list de dicts): une liste de dictionnaires contenant le vecteur TF-IDF de chaque document si l'entrée est "test".<br />
    autre_doc_filtres_tfidf (dict): un dictionnaire contenant le vecteur TF-IDF du document saisi par l'utilisateur si l'entrée n'est pas "test".<br />

### KNNClass.py
Description:
Ce code en Python définit une classe KNNClass qui implémente l'algorithme des k-plus proches voisins (KNN) pour la classification de vecteurs textuels. La classe possède plusieurs méthodes pour ajouter, supprimer et sauvegarder des classes de vecteurs, ainsi que pour effectuer la classification en utilisant la mesure de similarité cosinus comme fonction de similitude par défaut.
* **def __init__(self,description,data)->None**
  * Description: Constructeur qui initialise l'objet avec une description et une liste de données.
  * description : Description des données.
  * data : Liste des classes et de leurs vecteurs.
* **def add_class(self, label:str, vectors:list) -> None**
  * Description: Ajoute une classe aux données avec une étiquette et une liste de vecteurs.
  * label : noms des classes
  * vertors : Liste des vecteurs associés à la classe.
* **def add_vector(self,label:str,vector:dict)->None**
  * Description: Ajoute un vecteur aux données.
  * label : noms des classes
  * vertor : Liste des vecteurs associés à la classe.
* **def del_class(self,label:str)->None**
  * Description: Supprime une classe des données.
  * label: Nom de la classe à supprimer
* **def save_as_json(self, filename: str) -> None**
  * Description: Enregistre les données dans un fichier JSON.
  * filename : Nom du fichier dans lequel on va sauvegarder les données.
* **def load_as_json(self, filename:str) -> None**
  * Description: Charge les données à partir d'un fichier JSON.
  * filename : Nom du fichier à partir duquel on charge les données.
* **def classify(self, vector_1: dict, k: int, sim_func=None) -> None**
  * Description: Effectue la classification à l'aide de l'algorithme des k-plus proches voisins.
  * vector : Vecteur du ficher à classifier
  * k : Nombre de voisins le plus proche à considérer.

### Main.py
* Description: il permet de réaliser une classification de textes en utilisant l'algorithme KNN (K-nearest neighbors).Le principe est de représenter les textes sous forme de vecteurs TF-IDF, puis de mesurer les similarités entre ces vecteurs pour déterminer les K textes les plus proches d'un texte donné. La classe KNNClass implémentée permet de stocker les vecteurs TF-IDF des différents textes dans différentes classes, et de réaliser des opérations telles que l'ajout ou la suppression de classes ou de vecteurs selon le choix de l'utilisateur.

## Les bougues
veillez taper le nom de documents：test</br>
veillez donner votre ordonnance: (Choix parmi 'classify','add_class','add_vector','del_class','save','laod'): classify</br>
veillez taper le nom de documents：BOU.txt</br>
Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): 1</br>
Veuillez indiquer la valeur de k: 5</br>
label: roman n: 3 average similarity: 0.9995566455617556</br>
label: poésie n: 2 average similarity: 0.9994010729002618</br>
kedi@KedideMacBook-Air python % /usr/bin/python3 /Users/kedi/Downloads/M1/python/Main.py</br>
veillez taper le nom de documents：test</br>
veillez donner votre ordonnance: (Choix parmi 'classify','add_class','add_vector','del_class','save','laod'): classify</br>
veillez taper le nom de documents：BOU.txt</br>
Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): 1</br>
Veuillez indiquer la valeur de k: 11</br>
label: roman n: 8 average similarity: 0.9993879411416243</br>
label: poésie n: 3 average similarity: 0.999368047283594</br>

***J'ai testé "classer" avec un poème pour lequel j'ai donné des valeurs K de 5 et 11, mais les résultats ont tous eu tendance à le classer comme roman.***

Veuillez indiquer la valeur de k: 5</br>
label: roman n: 2 average similarity: 5283.684809030999</br>
label: poésie n: 1 average similarity: 4539.824016687306</br>
label: article n: 1 average similarity: 12332.47741120811</br>
label: pièce de théâtre n: 1 average similarity: 13558.77854114023</br>

Veuillez indiquer la valeur de k: 11</br>
label: roman n: 3 average similarity: 8110.784406143844</br>
label: poésie n: 2 average similarity: 10997.610117599866</br>
label: article n: 2 average similarity: 13090.301379082877</br>
label: pièce de théâtre n: 4 average similarity: 16155.05989731519</br>

***Ici, j'ai changé le méthode de calcul, 'euclidean_distance', quand k=11, il le clasee en roman, quand K=5, il le clasee en poésie***

Veuillez indiquer la valeur de k: 5</br>
label: roman n: 3 average similarity: 24731.536660835543</br>
label: poésie n: 1 average similarity: 26669.635271293613</br>
label: pièce de théâtre n: 1 average similarity: 30117.648519685958</br>

Veuillez indiquer la valeur de k: 11</br>
label: roman n: 3 average similarity: 24731.53666083544</br>
label: poésie n: 4 average similarity: 30085.40088810601</br>
label: pièce de théâtre n: 4 average similarity: 31479.586894157335</br>

***Dans le cas de manhattan_distance=3, il le clasee en roman, on n'a toujours pas trouvé la bonne réponse.***

Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): 1</br>
Veuillez indiquer la valeur de k: 5</br>
label: roman n: 4 average similarity: 0.9996885508381328</br>
label: poésie n: 1 average similarity: 0.9995243077265208</br>

Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): 3</br>
Veuillez indiquer la valeur de k: 7</br>
label: roman n: 6 average similarity: 178927.4426842699</br>
label: poésie n: 1 average similarity: 217871.26829574726</br>

Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): 2</br>
Veuillez indiquer la valeur de k: 11</br>
label: roman n: 7 average similarity: 100966.59592344206</br>
label: poésie n: 1 average similarity: 131750.83274455252</br>
label: article n: 2 average similarity: 140282.92981039645</br>
label: pièce de théâtre n: 1 average similarity: 140796.95321169504</br>

***J'ai testé "classer" avec un roman, quand K=5, méthode de calcul = cosinus, il le clasee en roman. Quand K=7, méthode de calcul = manhattan_distance, il le clasee en roman. Quand K=11, méthode de calcul = euclidean_distance, il le clasee en roman. La réponse est toujours bonne.***

***J'ai vérifié le fichier json stocké, et j'ai peut-être trouvé la raison pour laquelle les résultats des deux tests différaient autant. ***

***Les poèmes et les pièces de théâtre contiennent beaucoup de français archaïque, ou il y a des erreurs dans le processus de conversion de pdf en txt.***

***Deuxièmement, il n'a pas été constaté qu'il y avait un problème de décodage dans ce code, même s'il était entièrement défini en UTF-8.***




## Améliorations possibles

* Ce code parcourt tous les échantillons pour calculer les similarités, par conséquent, le prix de calcul est élevé. Si le dossier test est le ficher à classer est trop lourd, cela peut être très lent. Ainsi il est possible de choisir les meilleurs méthodes.
* Si l'utilisateur compte d'agrandir le document test, il n'existe qu'une méthode, à savoir créer de nouveux sous-dossiers dans le document test. Il est possible de créer une fonction consistant à ajouter directement les poids tf-idf de chaque mot dans les données de KNN.
* Il est possible de changer le doucument de Test pour améliorer la fonction de classification
* ...
         
          
       
    
