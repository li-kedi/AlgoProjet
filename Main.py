from TextVect import TextVect
from KNNClass import KNNClass 

"""
Cet API permet de réaliser une classification de textes en utilisant l'algorithme KNN (K-nearest neighbors). 
Le principe est de représenter les textes sous forme de vecteurs TF-IDF, puis de mesurer les similarités entre 
ces vecteurs pour déterminer les K textes les plus proches d'un texte donné. La classe KNNClass implémentée 
permet de stocker les vecteurs TF-IDF des différents textes dans différentes classes, et de réaliser des 
opérations telles que l'ajout ou la suppression de classes ou de vecteurs selon le choix de l'utilisateur.
"""
class Main:
    if __name__ == "__main__":
        # Création des vecteurs TF-IDF
        vectors_1=TextVect.doc2tf_idf()
        # print(vectors_1)
        # Initialisation de la classe KNN
        knn=KNNClass("description",vectors_1 )
        # Si l'ordre est "classify", effectuer la classification
        order = input("veillez donner votre ordonnance: (Choix parmi 'classify','add_class','add_vector','del_class','save','laod'): ")
        if order == "classify":
            vectors_1=TextVect.doc2tf_idf()
            choice = int(input("Veuillez indiquer la méthode de calcul. (cosinus=1,euclidean_distance=2, manhattan_distance=3): "))
            k = int(input("Veuillez indiquer la valeur de k: "))
            if choice == 1:
                resultat_classify = knn.classify(vectors_1,k=k,sim_func=TextVect.sim_cosinus)
            elif choice == 2:
                resultat_classify = knn.classify(vectors_1,k=k,sim_func=TextVect.euclidean_distance)
            elif choice == 3:
                resultat_classify = knn.classify(vectors_1,k=k,sim_func=TextVect.manhattan_distance)
            else:
                print("choix invalidé")
                resultat_classify = None

        # Si l'ordre est "add_class", ajouter une nouvelle classe
        if order == "add_class":
            label=input("Veillez donner le label: ")
            vectors_str = input("Veillez donner les vecteurs (sous forme de liste de dictionnaires): ")
            vectors = eval(vectors_str)
            knn.add_class(label, vectors)
            # print(knn.data)

        # Si l'ordre est "add_vector", ajouter un nouveau vecteur à une classe existante
        if order == "add_vector":
            label=input("Veillez donner le label: ")
            vectors_str = input("Veillez donner les vecteurs (sous forme de liste de dictionnaires): ")
            vectors = eval(vectors_str)
            knn.add_vector(label, vectors)
            # print(knn.data)

        # Si l'ordre est "del_class", supprimer une classe
        if order == "del_class":
            label=input("Veillez donner le label: ")
            knn.del_class(label)
            # print(knn.data)

        # Si l'ordre est "save", sauvegarder les données dans un fichier JSON
        if order == "save":
            filename = input("Veillez donner le nom du fichier  de sauvegarde: ")
            knn.save_as_json(filename)
            

        # Si l'ordre est "load", charger les données depuis un fichier JSON
        if order == "load":
            filename = input("Veillez donner le nom du fichier JSON de chargement: ")
            knn.load_as_json(filename)
            

    

    
