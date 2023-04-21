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
     
     
  *  ['laod'→ "Veillez donner le nom du fichier JSON de chargement: "](http://blog.csdn.net/guodongxiaren)



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



## API
### TextVect.py
* **def read_dict(stoplist_filename)**
  * Description: Cette méthode lit un fichier de liste de stop words et renvoie un ensemble de stop words
  * stoplist_filename : nom du fichier de stop words
* **def tokenize(text,tok_grm)**
  * Description: Cette méthode tokenize un texte avec une expression régulière 
  * Text: Ficher texte à tokenizer
  * Tok_grm : Les expressions régulières pour tokenizer le texte
* **def vectorise(tokens)**
  * Description: Cette méthode transforme une liste de tokens en un dictionnaire avec leur fréquence associée
  * Liste des tokens à transformer en dictionnaire
* **def doc2vec(cls,label:str)**
  * Description: Cette méthode convertit tous les fichiers textes d'un dossier en vecteurs en utilisant la méthode de vectorisation
  * Label : nom du dossier contenant les fichiers textes
* **def txt2vec(cls,file_name:str)**
  * Description: Cette méthode convertit un fichier texte en un vecteur de mots
  * File_name (str): Le nom du fichier texte à convertir.
* **def filtrage(cls,stoplist_filename, documents, non_hapax)**
  * Description: Cette méthode effectue le filtrage des tokens d'un document
  * stoplist_filename : nom du fichier de stop words
  * documents : dictionnaire contenant les informations du document
  * non_hapax : booléen pour déterminer si on élimine les hapax ou non
* **def tf_idf(documents:list)->list**
  * Description: Cette méthode effectue le calcul du poids tf-idf de chaque mot dans chaque document
  * Documents: une liste de documents contenant les vecteurs de mots et les libellés
* **def scalaire(vector1,vector2)**
  * Description: 
* **def norme(vector)**
  * Description: Cette fonction calcule la norme d'un vecteur donné.
  * Vextor: Un dictionnaire représentant le vecteur dont on souhaite calculer la norme.
* **def sim_cosinus(cls,vector1,vector2)**
  * Description: Cette méthode calcule la similarité cosinus entre deux vecteurs
  * vector1 : un dictionnaire représentant le premier vecteur.
  * vector2 : un dictionnaire représentant le deuxième vecteur
* **def euclidean_distance(vec1: dict, vec2: dict) -> float**
  * Description: Cette fonction calcule la distance euclidienne entre deux vecteurs donnés
  * vec1 : un dictionnaire représentant le premier vecteur.
  * vec2 : un dictionnaire représentant le deuxième vecteur
* **def manhattan_distance(vec1: dict, vec2: dict) -> float**
  * Description: Cette fonction calcule la distance manhattan entre deux vecteurs donnés
  * vec1 : un dictionnaire représentant le premier vecteur
  * vec2 : un dictionnaire représentant le deuxième vecteur
* **def doc2tf_idf(cls)**
  * Description: Cette fonction calcule le score tf-idf pour chaque document d'un corpus donné.
  * documents_input (str): le nom d'un document ou "test" si l'on veut traiter plusieurs documents.
  * Retour: <br />
    resultat_tfidf (list de dicts): une liste de dictionnaires contenant le vecteur TF-IDF de chaque document si l'entrée est "test".<br />
    autre_doc_filtres_tfidf (dict): un dictionnaire contenant le vecteur TF-IDF du document saisi par l'utilisateur si l'entrée n'est pas "test".<br />

### KNNClass.py
* **def __init__(self,description,data)->None**
* **def add_class(self, label:str, vectors:list) -> None**
* **def add_vector(self,label:str,vector:dict)->None**
* **def del_class(self,label:str)->None**
* **def save_as_json(self, filename: str) -> None**
* **def load_as_json(self, filename:str) -> None**
* **def classify(self, vector_1: dict, k: int, sim_func=None) -> None**

### Main.py
    * Description: il permet de réaliser une classification de textes en utilisant l'algorithme KNN (K-nearest neighbors). Le principe est de représenter les textes sous forme de vecteurs TF-IDF, puis de mesurer les similarités entre ces vecteurs pour déterminer les K textes les plus proches d'un texte donné. La classe KNNClass implémentée permet de stocker les vecteurs TF-IDF des différents textes dans différentes classes, et de réaliser des opérations telles que l'ajout ou la suppression de classes ou de vecteurs selon le choix de l'utilisateur.




         
          
       
    
