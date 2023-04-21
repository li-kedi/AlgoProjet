import json
from TextVect import TextVect
"""
Ce code en Python définit une classe KNNClass qui implémente l'algorithme des k-plus 
proches voisins (KNN) pour la classification de vecteurs textuels. La classe possède 
plusieurs méthodes pour ajouter, supprimer et sauvegarder des classes de vecteurs, 
ainsi que pour effectuer la classification en utilisant la mesure de similarité cosinus 
comme fonction de similitude par défaut.
"""

class KNNClass:
	# Initialisation de la classe KNNClass avec les paramètres description et data
	"""Description: Constructeur qui initialise l'objet avec une description et une liste de données.
	   description : Description des données.
       data : Liste des classes et de leurs vecteurs.
	"""
	def __init__(self,description,data)->None:
		self.description=description
		self.data=data

	# Méthode permettant d'ajouter une classe à la base de données avec un label et une liste de vecteurs
	"""
	Description: Ajoute une classe aux données avec une étiquette et une liste de vecteurs.
	label : noms des classes
	vertors : Liste des vecteurs associés à la classe.
	"""	
	def add_class(self, label:str, vectors:list) -> None:
		 # Initialise la variable label_exists à False
		label_exists = False
		# Parcourt les éléments de la base de données
		for element in self.data:
			 # Si le label qu'on veut ajouter existe dans la base de données
			if element["label"] == label:
				# on ajoute les vecteurs à la liste de vecteurs de cet élément
				element["vectors"].extend(vectors)
				# Met à jour la variable label_exists à True
				label_exists = True
				print("Classe ajoutée avec succès!")
				# Sort de la boucle
				break
		# Si le label n'existe pas dans la base de données
		if not label_exists:
			# on ajoute un nouvel élément à la base de données avec le label et les vecteurs
			self.data.append({"label": label, "vectors": vectors})

	# Méthode permettant d'ajouter un vecteur à la base de données
	"""
	Description: Ajoute un vecteur aux données.
	label : noms des classes
	vertor : Liste des vecteurs associés à la classe.
	"""
	def add_vector(self,label:str,vector:dict)->None:
		# Parcourt les éléments de la base de données
		for element in self.data:
			# Si le label qu'on veut ajouter existe dans la base de données
			if element["label"] == label:
				# on ajoute le vecteur à la liste de vecteurs de cet élément
				element["vectors"].append(vector)
				print("vecteurs ajoutés avec succès!")
				# Sort de la boucle
				break
			# Si le label n'est pas trouvé dans la base de données
			else:
				# Lève une erreur de valeur avec le message informant que le label n'est pas trouvé dans la base de données
				raise ValueError(f"Label '{label}' not found in data.")
    
	# Méthode permettant de supprimer une classe de la base de données
	"""
	Description: Supprime une classe des données.
	label: Nom de la classe à supprimer
	"""
	def del_class(self,label:str)->None:
		try:
			# parcourt de la base de données en partant de la fin pour éviter de modofirt les index des élements
			for i in range(len(self.data) - 1, -1, -1):
				# si le label qu'on veut supprimer dans la base de données
				if self.data[i]["label"]==label:
					# on supprimer l'élément avec le label correspondant
					del self.data[i]
					# Sort de la boucle
					print("Classe suprimée avec succès!")
					break
				# Si le label n'a pas été trouvé dans les données, lever une exception ValueError
				else:
					raise ValueError(f"Label '{label}' not found in data.")
				
		# Traiter toutes les autres exceptions et les afficher dans la console
		except Exception as e:
			print(f"Error: {e}")

    # Méthode permettant de sauvegarder les données de l'objet dans un fichier JSON
	"""
	Description: Enregistre les données dans un fichier JSON.
	filename : Nom du fichier dans lequel on va sauvegarder les données.
	"""
	def save_as_json(self, filename: str) -> None:
		# Vérifier si le ficher est en format json, si il n'est pas, on le remplace en format json
		if not filename.endswith(".json"):
			filename += ".json"
		try:
			# Ouvrir le fichier en mode écriture
			with open(filename, "w") as f:
				# Écrire les données au format JSON dans le fichier
				json.dump(self.data, f)
				print("File enregistré avec succès!")
		# Traiter les exceptions concernant l'ouverture ou à l'écriture du fichier
		except FileNotFoundError as e:
			print(f"Error: file not found. {e}")
		except PermissionError as e:
			print(f"Error: permission denied. {e}")
		# Traiter l'exception concernant la sérialisation des données (si les données ne peuvent pas être converties en JSON)
		except TypeError as e:
			print(f"Error: data cannot be serialized. {e}")

    # Méthode permettant de les charger à partir d'un fichier JSON
	"""
	Description: Charge les données à partir d'un fichier JSON.
	filename : Nom du fichier à partir duquel on charge les données.
	"""
	def load_as_json(self, filename:str)->None:
		if not filename.endswith('.json'):
			print(f"Error: {filename} is not a JSON file.")
			return
		try:
			# Ouvrir le fichier en mode lecture
			with open(filename, "r") as f:
				# Charger les données JSON à partir du fichier et les enregistrer dans 'data'
				self.data = json.load(f)
				print("File téléchargé avec succès!")
		# Traiter toutes les exceptions concernant l'ouverture ou la lecture du fichier
		except Exception as e:
			print(f"Error loading file {filename}: {e}")

	"""
	Description: Effectue la classification à l'aide de l'algorithme des k-plus proches voisins.
	vector : Vecteur du ficher à classifier
	k : Nombre de voisins le plus proche à considérer.
	"""
	def classify(self, vector_1: dict, k: int, sim_func=None) -> None:
		# création d'un dictionnaire pour stocker les résultats
		results_dic = {}
		# si on ne fournit pas sim_function, sim_cosinus est la fonction par défaut
		if sim_func is None:
			sim_func=TextVect.sim_cosinus
		# itération sur les données stockées
		for element in self.data:
			# créer une liste pour stocker les similarités 
			results_list = []
			for vector_2 in element['vector']:
				# calcul de la similarité entre les deux vecteurs
				sims = sim_func(vector_1, vector_2)
				results_list.append(sims)
			# ajout de la liste des similarités pour la classe au dictionnaire
			results_dic[element['label']] = results_list

		# fusion de toutes les listes de similarités pour chaque classe
		merged_list = []
		for lst in results_dic.values():
			merged_list.extend(lst)
		# tri de la liste de similarités fusionnée en fonction de la fonction de calcul
		if sim_func == TextVect.euclidean_distance or sim_func == TextVect.manhattan_distance:
			sorted_list = sorted(merged_list, reverse=False)
		else:
			sorted_list = sorted(merged_list, reverse=True)
		# sélection des k premières similarités 
		top_k = sorted_list[:int(k)]
		# créer un dictionnaire pour stocker les résultats finaux triés par classe
		res_dic = {}
		# itération sur chaque similarité sélectionnée
		for sim_top_k in top_k:
			# itération sur chaque classe pour trouver laquelle contient cette similarité
			for label in results_dic:
				if sim_top_k in results_dic[label]:
					# ajout de la similarité à la liste de similarités pour cette classe dans le dictionnaire de résultats
					if label not in res_dic:
						res_dic[label] = []
					res_dic[label].append(sim_top_k)
		# affichage des résultats triés par classe
		for label in res_dic:
			print("label: " + label + " n: " + str(len(res_dic[label])) + " average similarity: " + str(sum(res_dic[label]) / len(res_dic[label])))

				
	
		
		
