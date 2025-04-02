# Qualité de l'air en France (projet en cours)
## <ins>Contexte et objectif</ins>
La qualité de l’air est un enjeu fort de santé publique car la dégradation de la qualité de l’air peut entrainer des effets négatifs sur la santé des populations (en particulier les personnes les plus vulnérables). D’où l’intérêt de surveiller l’évolution de la qualité de l’air et prendre des mesures en faveur du maintien d'un bon état de qualité de l'air.

Les données de qualité de l’air sont de plus en plus accessibles au grand public. A partir de ces données, on peut facilement étudier les tendances de qualité de l’air des communes. A l’échelle européenne, l’une des bases des données les plus utilisées est Copernicus Atmosphere Data store.

L’objectif poursuivi par ce projet est de grouper les communes de la France sur la base des concentrations des polluants émis par chacune d’elle en utilisant des méthodes de machine learning non supervisé.
Les polluants d’intérêt sont le dioxyde d’azote (NO2), l’ozone (O3), les particules fines (PM2.5 et PM10) ainsi que le dioxyde de soufre (SO2). 

## <ins>Collecte des données  et pretraitement</ins>
Les données de qualité de l’air ont été collectées sur la plateforme Copernicus Atmosphere Data store à partir d'un API. Les caractéristiques du jeu des données sont présentées ci-dessous :
* Nom du jeu de donnée : CAMS European air quality reanalyses
* Couverture géographique : Europe
* Résolution temporaire : donnée horaire
* Polluants sélectionnés pour le projet : NO2, O3, PM2.5, PM10 et SO2
* Année sélectionnée pour le projet : 2022

Les données sont livrées au format NetCDF. C’est un format utilisé dans la communauté scientifique pour faciliter le stockage et le partage des données environnementales. 
Pour plus d’information sur les données utilisées : https://ads.atmosphere.copernicus.eu/datasets/cams-europe-air-quality-reanalyses?tab=overview

Le prétraitement a consisté à :
* Extraire les concentrations de polluants pour chaque commune.
* Transformer les données de concentration horaire en moyenne annuelle pour chacune commune
* Enregistrer les données traitées dans un classeur Excel

## <ins>Développement des modèles</ins>
Deux modèles d'apprentissage non supervisé ont été utilisé pour ce projet. A savoir ***Kmean*** et ***DBSCAN***. Ces deux modèles sont utilisés pour faire du clustering. Ce qui est l'objectif poursuivi par ce projet. La librairie Python Scikit-Learn a été utilisé pour développer ces modèles.

***Kmean :*** Pour ameliorer la performance du modèle, le nombre de cluster a été optimisé grace à la « Elbow method ».
***DBSCAN :*** Les paramètres epsilon (eps) et nombre minimum d’échantillon (min_samples) ont été optimisé pour améliorer la performance du modèle. On a procédé par itération jusqu'à trouver la bonne combinaison eps/min_sample.

Les performances des deux modèles ont été comparés sur la base de 3 méthodes (Silhouete score, Davies Boulding score et Calinski Harabasz score) afin de determiner celui offrant la meilleure performance. Les resultats sont présentés dans le tableau ci-dessous.

|  Modèles  | Optimal n_cluster | Silhouete score | Davies Boulding score | Calinski Harabasz score |
|-----------|-------------------|-----------------|-----------------------|-------------------------|
| Kmean     | 3                | 0.35            | 0.95                  | 25822        |
| DBSCAN    |                   |                 |                       |                         |

## <ins>Resultats</ins>
La carte ci-dessous est une illustration du resultat obtenu avec le modèle Kmean

![Picture1](https://github.com/user-attachments/assets/6c0357ed-fcda-4a21-a225-5dd62fa8ba5f)

## <ins>Déploiement</ins>
Les modèles ont été déployé en local en utilisant streamlit. Une vidéo du deploiement est disponible dans le dossier : deployment

## <ins>Perspectives</ins>
* Chaque cluster peut faire l'objet d'une analyse approfondie afin de déterminer les similarités de chaque commune composant le cluster. Les éléments qui peuvent être comparé sont la taille de la population, l'activité économique dominante, la présence d'industries, l'utilisation des transports en commun (ou voiture individuelle), etc.
* Faire tourner le modèle pour les années antérieures et ainsi que pour les données futures (automatiser).
* Déployer en ligne pour le grand public avec une meilleure interface utilisateur.

## <ins>Infos utiles</ins>
Version de Python utilisée: Python 3.9
Le repository de ce projet contient les dossiers suivants:
* 01_data: les données utilisées pour entrainer les modèles.
* 02_scripts: tous les scripts dévéloppés pour mener à bien le projet.
* 03_EDA: Exploratory data analysis. Quelques graphs et stats pour mieux comprendre le jeu des données.
* 04_model_files: les fichiers relatifs au développement du model dont les resultats.
* 05_deployment: la vidéo du déploiement
* 06_presentation: le powerpoint de la présentation du projet lors du demo day.

