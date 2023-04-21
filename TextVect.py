import copy
import math
import re
import os
import codecs

"""
Le code comprend plusieurs méthodes de classe pour effectuer des tâches de traitement 
de texte telles que la tokenisation, la vectorisation et le filtrage.
"""

tok_grm=re.compile(r"""
    (?:etc.|p.ex.|cf.|M.)|
    \w+(?=(?:-(?:je|tu|ils?|elles?|nous|vous|leur|lui|les?|ce|t-|même|ci|là)))|
    [\w\-]+'?| .""",re.X)

class TextVect:
    """
    Cette méthode lit un fichier de liste de stop words et renvoie un ensemble de stop words
    stoplist_filename : nom du fichier de stop words
    return : un ensemble de stop words
    """
    def read_dict(stoplist_filename):
        # Ouverture du fichier de stop words en mode lecture
        dict_file = open(stoplist_filename, "r", encoding="utf-8")
        # Lecture du fichier de stop words
        dict_content = dict_file.read()
        # Fermeture du fichier de stop words
        dict_file.close()
        # Création d'un ensemble de stop words à partir du fichier
        stoplist = set(dict_content.split("\n"))
        # Renvoie de l'ensemble de stop words
        return stoplist
    
    """
    Cette méthode tokenize un texte avec une expression régulière 
    Text :texte à tokenizer
    Tok_grm : expression régulière pour tokenizer le texte
    Return : liste des tokens
    """ 
    def tokenize(text,tok_grm):
        return tok_grm.findall(text)
    
    """
    Cette méthode transforme une liste de tokens en un dictionnaire avec leur fréquence associée
    Tokens : liste des tokens à transformer en dictionnaire
    Return : dictionnaire contenant les fréquences des tokens
    """
    def vectorise(tokens):
        # initialisation du hachage
        token_freq={}  
        # parcours des tokens
        for token in tokens:
            # si le token n'est pas  présent dans le dictionnaire, on l'ajoute avec une fréquence 
            if token not in token_freq.keys():   
                token_freq[token]=0 
            # on incrémente la fréquence du token dans le dictionnaire
            token_freq[token]+=1 
        # on renvoie le dictionnaire de fréquences des tokens
        return token_freq
    
    """
    Cette méthode convertit tous les fichiers textes d'un dossier en vecteurs en utilisant la méthode de vectorisation
    Label : nom du dossier contenant les fichiers textes
    Return : un dictionnaire contenant le nom du dossier et la liste des vecteurs de chaque fichier texte
    """
    @classmethod  
    def doc2vec(cls,label:str)-> dict:
        # initialisation de la liste de vecteurs de mots
        vectors=[]
        # liste des fichiers dans le dossier du label
        file_names = os.listdir("test/"+label)
        for file_name in file_names :
            # on ne traite que les fichiers avec l'extension .txt
            if file_name[-4:]==".txt":
                # ouverture du fichier en lecture
                input_file=codecs.open("./test/"+label+"/"+file_name,mode="r",encoding="utf-8")
                # initialisation de la liste de tokens
                tokens=[]
                # lecture de chaque ligne du fichier
                for line in input_file:
                    #on supprime les retours à la ligne
                    line=line.strip()
                    # découpage de la ligne en tokens
                    toks=cls.tokenize(line,tok_grm)
                    # ajout des tokens à la liste de tous les tokens du fichier
                    tokens.extend(toks)
                # fermeture du fichier
                input_file.close()
                # conversion des tokens en vecteur de mots
                vector=cls.vectorise(tokens)
                # ajout du vecteur de mots à la liste de tous les vecteurs de mots des fichiers du label
                vectors.append(vector)
        return {'label':label,'vector':vectors}
    
    
    """
    Cette méthode convertit un fichier texte en un vecteur de mots
    File_name (str): Le nom du fichier texte à convertir.
    Return:Un dictionnaire contenant le label du fichier et sa représentation sous forme de vecteur de mots.
    """
    @classmethod  
    def txt2vec(cls,file_name:str):
         # initialisation de la liste de vecteurs de mots
        vectors=[]
        # ouverture du fichier en lecture
        input_file=codecs.open(file_name,mode="r",encoding="utf-8")
        # initialisation de la liste de tokens
        tokens=[]
        # lecture de chaque ligne du fichier
        for line in input_file:
            #on supprime les retours à la ligne
            line=line.strip() 
            # découpage de la ligne en tokens
            toks=cls.tokenize(line,tok_grm)
            # ajoute les tokens à la liste complète
            tokens.extend(toks)
        # fermeture du fichier
        input_file.close()
        # conversion des tokens en vecteur de mots
        vector=cls.vectorise(tokens)
        # ajout du vecteur de mots à la liste de tous les vecteurs de mots des fichiers du label
        vectors.append(vector)
        return {'label':file_name,'vector':vectors}
    
    """
    Cette méthode effectue le filtrage des tokens d'un document
    stoplist_filename : nom du fichier de stop words
    documents : dictionnaire contenant les informations du document
    non_hapax : booléen pour déterminer si on élimine les hapax ou non
    return : dictionnaire contenant les informations du document filtré
    """
    @classmethod 
    def filtrage(cls,stoplist_filename, documents, non_hapax):
        # Lecture de la stoplist depuis le fichier spécifié
        stoplist = cls.read_dict(stoplist_filename)
        # Création d'un dictionnaire contenant le résultat du filtrage
        document_filtre = {}
        document_filtre["label"] = documents["label"]
        # Récupération des tokens à filtrer
        tokens = documents["vector"]
        # Initialisation d'un dictionnaire qui contiendra les tokens filtrés pour chaque document
        tokens_filtre = {}
        document_filtre["vector"]=[]
        # Itération sur tous les tokens de chaque document
        for element in tokens:
            tokens_filtre = {}
            for token in element.keys():
                # Si le token n'est pas dans la stoplist et si la condition non_hapax est respectée 
                # on ajoute le token filtré au dictionnaire tokens_filtre
                if token.lower() not in stoplist and (not non_hapax or tokens[token]>1):
                    tokens_filtre[token]=element[token]
            # Ajout du dictionnaire tokens_filtre à document_filtre
            document_filtre["vector"].append(tokens_filtre)
        return document_filtre
    
    """
    Cette méthode effectue le calcul du poids tf-idf de chaque mot dans chaque document
    Documents: une liste de documents contenant les vecteurs de mots et les libellés.
    return : une liste de documents modifiés avec les poids tf-idf pour chaque mot
    """
    def tf_idf(documents:list)->list:
        # Créer une copie profonde de la liste de documents pour ne pas modifier l'original
        documents_new=copy.deepcopy(documents)
        # Créer un ensemble vide pour stocker les mots
        mots=set()
         # Parcourir chaque document
        for vector in documents["vector"]:
            # Parcourir chaque mot dans le vecteur
            for word in vector:
                # Ajouter le mot à l'ensemble
                mots.add(word)
        # Créer un dictionnaire vide pour stocker la fréquence de chaque mot dans les documents
        freq_doc={}
        # Parcourir chaque mot dans l'ensemble de mots
        for word in mots:
            # Parcourir chaque document
            for vector in documents["vector"]:
                # Si le mot est présent dans le document
                if word in vector:
                     # Si le mot n'est pas déjà dans le dictionnaire, l'ajouter avec une fréquence de 1
                    if word not in freq_doc:
                        freq_doc[word]=1
                    # Sinon, incrémenter la fréquence
                    else :
                        freq_doc[word]+=1
        # Parcourir tous les docs mot par mot pour mettre à jour la fréquence
        for vector in documents_new["vector"]:
            # Parcourir chaque mot dans le vecteur
            for word in vector:
                 # Diviser la fréquence brute par le logarithme de la fréquence du mot dans tous les documents
                vector[word]=vector[word] / math.log(1+freq_doc[word])
        return documents_new
    
    def scalaire(vector1,vector2)->float:
        liste_scalaire=[]
        # Pour chaque clé dans le premier vecteur, si cette clé est présente dans le deuxième vecteur, on multiplie les valeurs associées
        for key in vector1:
            if key in vector2:
                liste_scalaire.append(vector1[key]*vector2[key])
        # On somme les scalaires pour obtenir le scalaire total
        produit_scalaire=sum(liste_scalaire)
        return produit_scalaire
    
    """
    Cette fonction calcule la norme d'un vecteur donné.
    vector : un dictionnaire représentant le vecteur dont on souhaite calculer la norme.
    return : la norme du vecteur donné. 
    """
    def norme(vector)-> float:
        norme_carre=0
        # Pour chaque clé dans le vecteur, on ajoute le carré de la valeur associée
        for key in vector:
            norme_carre+=vector[key]*vector[key]
        # On prend la racine carrée de la somme pour obtenir la norme
        norme=math.sqrt(norme_carre)
        return norme
    
    """
    Cette méthode calcule la similarité cosinus entre deux vecteurs
    vector1 : un dictionnaire représentant le premier vecteur.
    vector2 : un dictionnaire représentant le deuxième vecteur.
    return : la similarité cosinus entre les deux vecteurs donnés.
    """
    @classmethod   
    def sim_cosinus(cls,vector1,vector2)-> float:
        # On calcule les normes des deux vecteurs
        norme1=cls.norme(vector1)
        norme2=cls.norme(vector2)
        # On calcule le scalaire des deux vecteurs
        scal=cls.scalaire(vector1,vector2)
        # On calcule le cosinus
        cosinus=(scal/(norme1*norme2))
        return cosinus
    

    """
    Cette fonction calcule la distance euclidienne entre deux vecteurs donnés.
    vec1 : un dictionnaire représentant le premier vecteur.
    vec2 : un dictionnaire représentant le deuxième vecteur.
    return : la distance euclidienne entre les deux vecteurs donnés.
    """
    def euclidean_distance(vec1: dict, vec2: dict) -> float:
        # Determiner le vec1 et vec2 est une vector ou pas
        distance = 0
        # Parcourir toutes les clés des deux dictionnaires
        for key in set(vec1.keys()).union(vec2.keys()):
            # Récupérer la valeur de la clé dans dict1, sinon retourner 0
            value1 = vec1.get(key, 0)
            # Récupérer la valeur de la clé dans dict2, sinon retourner 0
            value2 = vec2.get(key, 0)
            # Calculer la somme des différences au carré
            distance += (value1 - value2) ** 2
        if distance < 0:
            # Si la distance est négative, lever une exception ValueError avec un message d'erreur correspondant
            raise ValueError("La distance euclidienne ne peut pas être négative.")
        # Retourner la racine carrée de la distance
        return math.sqrt(distance)

    """
    Cette fonction calcule la distance manhattan entre deux vecteurs donnés.
    vec1 : un dictionnaire représentant le premier vecteur.
    vec2 : un dictionnaire représentant le deuxième vecteur.
    return : la distance manhattan entre les deux vecteurs donnés.
    """
    # Définition de la fonction manhattan_distance pour calculer la distance de Manhattan entre deux vecteurs
    @staticmethod
    def manhattan_distance(vec1: dict, vec2: dict) -> float:
        # Determiner le vec1 et vec2 est une vector ou pas
        distance = 0
        # Parcourir toutes les clés des deux dictionnaires
        for key in set(vec1.keys()).union(vec2.keys()):
            # Récupérer la valeur de la clé dans dict1, sinon retourner 0
            value1 = vec1.get(key, 0)
            # Récupérer la valeur de la clé dans dict2, sinon retourner 0
            value2 = vec2.get(key, 0)

            # Calculer la somme des différences absolues
            distance += abs(value1 - value2)
        return distance
    
 
    """
    Cette fonction calcule le score tf-idf pour chaque document d'un corpus donné.
    entrée : 
    documents_input (str): le nom d'un document ou "test" si l'on veut traiter plusieurs documents.
    return :
    resultat_tfidf (list de dicts): une liste de dictionnaires contenant le vecteur TF-IDF de chaque document si l'entrée est "test".
    autre_doc_filtres_tfidf (dict): un dictionnaire contenant le vecteur TF-IDF du document saisi par l'utilisateur si l'entrée n'est pas "test".
    """
    @classmethod 
    def doc2tf_idf(cls):
        vectors = []
        # On demande à l'utilisateur de donner le nom du document ou du dossier contenant les documents à traiter
        documents_input = input("veillez taper le nom de documents：")
        # Si l'utilisateur saisit "test", on traite tous les documents contenus dans le dossier "test"
        if documents_input == "test":
            path = documents_input
            names = os.listdir(path)
            labels = [name for name in names if os.path.isdir(os.path.join(path, name))]
            resultat_tfidf=[]
            # Pour chaque dossier de documents, on extrait les vecteurs tf-idf des documents
            for label in labels:
                data=cls.doc2vec(label)
                doc_filtres = cls.filtrage("stop_words_french.txt",data, non_hapax=False)
                doc_filtres_tfidf = cls.tf_idf(doc_filtres)
                resultat_tfidf.append(doc_filtres_tfidf)
            return resultat_tfidf
        # Sinon, on traite le document saisi par l'utilisateur
        else:
            autre_data=cls.txt2vec(documents_input)
            autre_doc_filtres = cls.filtrage("stop_words_french.txt",autre_data, non_hapax=False)
            autre_doc_filtres_tfidf = cls.tf_idf(autre_doc_filtres)
            return autre_doc_filtres_tfidf['vector'][0]





        
   

        





