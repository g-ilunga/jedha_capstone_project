# Analyse de la pollution de l'air en région PACA (France)
## <ins>Contexte et objectif</ins>
La qualité de l’air est un fort enjeu de santé publique car la dégradation de la qualité de l’air peut entrainer des effets négatifs sur la santé des populations. En particulier les personnes les plus vulnérables. D’où l’intérêt de constamment surveiller l’évolution de la qualité de l’air.
Les données de qualité de l’air sont de plus en plus accessibles. A partir de ces données, on peut facilement étudier les tendances de qualité de l’air des villes. A l’échelle européenne, l’une des bases des données les plus utilisées est Copernicus Atmosphere Data store.
L’objectif poursuivi par ce projet est de grouper les communes de la région PACA sur la base des concentrations des polluants émis par chacune d’elle en utilisant des méthodes de machine learning non supervisé.
Les polluants d’intérêt sont le dioxyde d’azote (NO2), l’ozone (O3), les particules fines (PM2.5 et PM10) ainsi que le dioxyde de soufre. 

## <ins>Collecte des données  et pretraitement</ins>
Les données de qualité de l’air ont été collectées sur la plateforme Copernicus Atmosphere Data store. Les caractéristiques du jeu des données sont présentées ci-dessous :
* Nom du jeu de donnée : CAMS European air quality reanalyses
* Couverture géographique : Europe
* Résolution temporaire : donnée horaire
* Polluants sélectionnés pour le projet : NO2, O3, PM2.5, PM10 et SO2
* Année sélectionnée pour le projet : 2022

Les données sont livrées au format NetCDF. C’est un format utilisé pour le stockage et le partage des données scientifiques et environnementale. Ce format permet d’ajouter une composante spatiale aux données. 
Pour plus d’information sur les données utilisées : https://ads.atmosphere.copernicus.eu/datasets/cams-europe-air-quality-reanalyses?tab=overview

Le prétraitement a donc consisté à :
* Extraire les concentrations de polluants pour les communes de la région PACA
* Transformer les données de concentration horaires en moyenne annuelle pour chacune commune
* Enregistrer les données traitées dans un classeur Excel

## <ins>Développement des modèles</ins>
Deux modèles d'apprentissage non supervisé ont été utilisé pour ce projet. A savoir Kmean et DBSCAN. Ces deux modèles sont utilisés pour faire du clustering. Ce qui est l'objectif poursuivi par ce projet. La librairie Python Scikit-Learn a été utilisé pour développer ces modèles.

L'un des paramètres qui a été optimisé pour ameliorer la performance du model ***Kmean*** est le nombre de cluster. Pour cela, nous avons utilisé la method "Elbow" pour determiner le nombre de cluster optimal.

Les paramêtres suivants ont été optimisé pour ameliorer les performances du model ***DBSCAN***. Les valeurs retenues sont presentées ci-dessous

Les résultats des deux modèles ont été comparés sur la base de 3 méthodes afin de determiner celui offrant la meilleure performance. Les resultats sont présentés dans le tableau ci-dessous.

|  Modèles  | Optimal n_cluster | Silhouete score | Davies Boulding score | Calinski Harabasz score |
|-----------|-------------------|-----------------|-----------------------|-------------------------|
| Kmean     | 5                 | 0.43            | 0.81                  | 846.31                  |
| DBSCAN    |                   |                 |                       |                         |

## <ins>Resultats</ins>
Kmean et DBSCAN ont produit respectivement XX clusters.

Les deux modèles ont été comparés sur la base de 3 metrics. Les resultats sont presentés dans le tableau ci-dessous.

## <ins>Deployement</ins>
Les modèles ont été déployé en local en utilisant strimlit.

## <ins>Perspectives</ins>
En termes des perspectives, chaque cluster peut faire l'objet d'une analyse approfondie afin de determiner les similarités de chaque commune composant le cluster. Les élements qui peuvent être comparé sont la taille de la commune, taille de la population, l'activité économique dominante, la presence d'industrie, l'utilisation des transport en commun (ou voiture individuelle), etc.

Les modèles peuvent être plus optimisé afin d'être deployé en ligne. Cette version pourra inclure des options plus avancées.

## <ins>Infos utiles</ins>
Le  repository de ce projet contient les dossiers suivants:
* Data: les données utilisées pour entrainer le modèle.
* Scripts: tous les scripts dévéloppés pour mener à bien le projet.
* Models: les fichiers contenants les modèles developpés.
* docker: les fichiers docker pour facilement permettre la reproduction du projet.
