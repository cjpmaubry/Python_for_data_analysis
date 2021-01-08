# Python_for_data_analysis
Repository for Python for data analysis course

------------------------------------------------------

# Sommaire
 - [Information Générale](#information-générale)
 - [Auteurs](#auteurs)
 - [Démarrage](#démarrage)
 - [Conclusion](#conclusion)
 - [Comment utiliser l'API](#comment-utiliser-lapi)

------------------------------------------------------

# Information Générale 
## Introduction
Ce projet s'inscrit dans le cadre du cour intitulé Python for data analysis. 

## L'objectif
L'objectif de ce projet est d'étudier le dataset :"Estimation of obesity levels based on eating habits and physical condition Data Set". 
Ce dataset a pour vocation de présenter les différents niveaux d'obésité en fonction de plusieurs paramètres.
Nous avons donc choisit de nous interrésser à un moyen de prédire la corpulence d'un individu suivant les différentes variables présentées dans le dataset.
(Ce dataset à d'ailleur été consu dans ce sens)  
Nous avons pour cela décidé de procéder en 3 temps :  
*  Dans un premier temps étudié les différents variables de ce dataset.  
*  Dans un second temps nous avons réalisé plusieurs modèles de machine learning  
*  Dans un dernier temps nous avons expoter le meilleur modèle afin de créer une API permettant de prévoir la corpulence d'un individu suivant les meme variable que celle du dataset.  

## Les différents fichiers
Les différents fichiers utilisés sont les suivants:
*  AUBRY_BAROUX_IBO1_notebook.ipynb: Il s'agit du notebook en python
*  api.py: Il s'agit de l'API
*  request.py: Il s'agit du script permettant d'interroger l'API
*  randomforest.pickle : Il s'agit du modèle de machine learnig créé dans le notebook et enregistré sous le format .pkl
*  AUBRY_BAROUX_IBO1_powerpoint.pdf : Il s'agit du powerpoint expliquant les tenants et les aboutissants du projet

Note : le dataset utilisé est disponible au format .csv à l'adresse suivante :   
https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+

## Le Dataset
**Titre** : Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico  
**Source** : https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+  
**Documentation** : https://www.sciencedirect.com/science/article/pii/S2352340919306985?via%3Dihub  
**Structure** : Document au format .csv se composant de 17 colonnes et de 2111 lignes  
**Liste des Colonnes** :  
*   Gender : Le sexe de l'individu (homme ou femme)
*   Age : L'age de l'individu
*   Height : La taille de l'individu
*   Weight : Le poid de l'individu
*   family_history_with_overweight : L'individu à t'il dans sa famille des antécédent avec l'obésité
*   FAVC : Est ce que la personne mange souvent de la nourriture calorique
*   FCVC : Est ce que la personne mange des légumes pendant ses repas
*   NCP : Le nombre de repas quotidiens
*   CAEC : Est ce que la personne mange entre les repas
*   SMOKE : Est ce que l'individu fume
*   CH2O : Consommation quotidienne d'eau
*   SCC : Est ce que la personne surveille le nombre de calories qu'elle mange quotidiennement
*   FAF : Fréquence moyenne de la pratique d'une activité physique
*   TUE : Temps d'utilisation d'objets électroniques
*   CALC : Consommation d'alcool
*   MTRANS : Moyen de transport usuel
*   NObeyesdad :La corpulence (suivant l'imc)
    * Insufficient weight : Moins de 19.0
    * Normal: 19.0–24.9
    * Overweight stage 1: 25.0–27.4
    * Overweight stage 2: 27.5–29.9
    * Obese stage 1: 30.0–34.9
    * Obese stage 2: 35.0–39.9
    * (Morbidly) obese stage 3: 40.0 ou plus

Les réponses possible (selon l'étude réalisé par les auteurs) :
**Questions et réponses possible dans l'enquête :**

¿What is your gender?	

* • Female
* • Male

¿what is your age?	Numeric value

¿what is your height?	Numeric value in meters

¿what is your weight?	Numeric value in kilograms

¿Has a family member suffered or suffers from overweight?	

* Yes
* No

¿Do you eat high caloric food frequently?	

* Yes
* No

¿Do you usually eat vegetables in your meals?	

* Never
* Sometimes
* Always

¿How many main meals do you have daily?	

* Between 1 y 2
* Three
* More than three

¿Do you eat any food between meals?	

* No
* Sometimes
* Frequently
* Always

¿Do you smoke?	

* Yes
* No

¿How much water do you drink daily?	

* Less than a liter
* Between 1 and 2 L
* More than 2 L

¿Do you monitor the calories you eat daily?	

* Yes
* No

¿How often do you have physical activity?	

* I do not have
* 1 or 2 days
* 2 or 4 days
* 4 or 5 days

¿How much time do you use technological devices such as cell phone, videogames, television, computer and others?	

* 0–2 hours
* 3–5 hours
* More than 5 hours

¿how often do you drink alcohol?	

* I do not drink
* Sometimes
* Frequently
* Always

¿Which transportation do you usually use?	

* Automobile
* Motorbike
* Bike
* Public Transportation
* Walking

------------------------------------------------------

# Auteurs
## Du Dataset
**Titre** : Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Colombia, Peru and Mexico  
**Les auteurs de ce dataset sont :**  
*   Fabio Mendoza Palechor  
*   Alexis de la Hoz Manotas  

**Plus d'inforamtion à ce lien :**  
https://www.sciencedirect.com/science/article/pii/S2352340919306985?via%3Dihub  

## Du Notebook et de l'API

Le notebook et l'API ont été réalisé dans le cadre du cour intitulé Python for data analysis.  
Ce dépot présente donc le travail de :
*  AUBRY Corentin
*  BAROUX Alexandre  

------------------------------------------------------

# Démarrage
## Téléchargement
Le dataset utilisé est disponible au format .csv à l'adresse suivante :   
https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+  

## Import préalable
Afin de pouvoir lire et utiliser le notebook vous devez utiliser jupyter-notebook ou utiliser Google Collab.  
Lien installation jupyter-notebook : https://jupyter.org/  
Lien Google Collab : https://colab.research.google.com  

Note : Le notebook de ce projet à été réalisé avec Google Collab.  

Eventuellement au besoin réaliser c'est installation python :
*  pip install pandas  
*  pip install seaborn  
*  pip install numpy  
*  pip install sklearn  
*  pip install matplotlib  

------------------------------------------------------

# Conclusion
## Data-Analys
## Modélisation
## API
Nous avons réussi à créer une API utilisant le modèle RandomForest afin de prédire la corpulence d'un individu suivant les différentes variables qui étaient présentes dans le dataset. Cette API est ecrite en Python et utilise Flask.
Le fonctionnement de l'API est défini dans la partie suivante.

------------------------------------------------------

# Comment utiliser l'API
## Mise en place
Dans un premier temps créé un dossier contenant le dossier models (contenant randomforest.pickle) et le fichier api.py
Puis ouvrir un terminal et executer le api.py  
(par ex : python3 api.py )
Une fois exécuté l'API tourne à l'adresse indiqué dans le fichier (par défaut: http://0.0.0.0:5000)  

## Requetage
Pour requeter l'api il faut lui envoyer au format json ce genre d'information : [[1,50,1,1,1,2,1,1,3,0,0,2,1,2]]  
Chaque chiffre présent dans le tableau correspond à une variable.
Dans le cas de l'utilisation du script la création du tableau est automatique, il suffit de chosir les valeurs souhaitez en changemant les valeurs des variables.  
Au cas ou on souhait construire le tableau à la main voici l'ordre des valeurs et leur correspondance avec la variable :  

| Position | Reference                      | type  | Description                                                                    |
|----------|--------------------------------|-------|--------------------------------------------------------------------------------|
| 1        | Gender                         | int   | 1 = homme ; 0 = femme                                                          |
| 2        | Age                            | int   |  entrer un entier pour l'age                                                   |
| 3        | Family_history_with_overweight | int   | 1 = oui  ; 0 = non                                                             |
| 4        | FAVC                           | int   | 1 = oui  ; 0 = non                                                             |
| 5        | FCVC                           | int   | 1 = never ; 2 = sometimes ; 3 = always                                         |
| 6        | NCP                            | int   | Nombre de repas                                                                |
| 7        | CAEC                           | int   | 0 = no; 1 = sometimes; 2 = frequently; 3 = always                              |
| 8        | SMOKE                          | int   | 1 = oui  ; 0 = non                                                             |
| 9        | CH2O                           | int   | nombre de litre d'eau bu par jour                                              |
| 10       | SCC                            | int   | 1 = oui  ; 0 = non                                                             |
| 11       | FAF                            | int   | 0 = non; 1 = 1-2; 2 = 2-4; 3 = 5 ou plus  (par semaine)                        |
| 12       | TUE                            | int   | 0 = 0-2h/j; 1 = 3-5h/j; 2 = plus de 5h/j                                       |
| 13       | CALC                           | int   | 0 = no; 1 = sometimes; 2 = frequently; 3 = always                              |
| 14       | MTRANS                         | int   | 0 = Automobile; 1 = Bike; 2 = Motorbike; 3 =Public Transportation; 4 = Walking |


### En utilisant request.py
La première facon de requéter l'API est d'utiliser le script python proposer dans ce dépot. Intitulé "request.py" il permet d'interroger le modèle créé au préalable dans le notebook. Le processus de requetage est le suivant :  
* 1) Ouvir le fichier request.py
* 2) Définir dans ce dernier les paramètres voulue (age,sexe,etc...)
* 3) Executer le fichier dans la console (python3 request.py), le résultat de la prédiction apparait alors dans la console.

### En utilisant Postman
La deuxième facon de requéter l'API est d'utiliser par exemple un logiciel prevu à cette effet tel que Postman.   
Le processus de requetage est le suivant :  
*  1) Télécharger et installer Postman
*  2) Lancer le logiciel
*  3) Paramétrer comme montré si dessous et appuyer sur send :  

![Image](https://github.com/cjpmaubry/Python_for_data_analysis/blob/main/src/postman_conf.PNG)

Au besoin suivre ce tuto : https://www.toolsqa.com/postman/post-request-in-postman/
