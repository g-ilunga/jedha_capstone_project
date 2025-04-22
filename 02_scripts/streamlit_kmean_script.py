#==========================================
# Libraries
#==========================================
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#================================
# Configuring the streamlit page
#================================

# Set Streamlit page configuration
st.set_page_config(layout="wide")

# Custom CSS to remove the top space
st.markdown(
    """
    <style>
    /* Adjust top padding to ensure the heading is fully visible */
    .block-container {
        padding-top: 1rem; /* Increase if needed */
    }
    
    .title {
        text-align: center;
        font-size: 36px; /* Slightly larger for visibility */
        font-weight: bold;
        color: #333333;
        margin-top: 20px; /* Ensure enough space above */
    }
    
    .subheader {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #555555;
    }
    
    .scrollable-summary {
        height: 420px;
        overflow-y: auto;
        border: 1px solid #ccc;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


#==================================================
# Loading the model and its dependencies
#==================================================
basedir = "C:/Users/ilung/Documents/Jedha_bootcamp/capstone_project/"
model_kmean = f"{basedir}/model/kmean/kmean_model.pkl"
model_scaler = f"{basedir}/model/kmean/scaler.pkl"
table_min = f"{basedir}/model/kmean/table_min.xlsx"
table_max = f"{basedir}/model/kmean/table_max.xlsx"
table_average = f"{basedir}/model/kmean/table_average.xlsx"
final_dataset = f"{basedir}/model/kmean/final_dataset.xlsx"

# Loading the pre-trained model and scaler
with open(model_kmean, "rb") as model_file:
    kmeans = pickle.load(model_file)

with open(model_scaler, "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Loading the results
dataset_df = pd.read_excel(final_dataset) # Load the final dataset from Excel
df_min = pd.read_excel(table_min) # Load the table of minimum from Excel
df_max = pd.read_excel(table_max) # Load the table of maximum from Excel
df_average = pd.read_excel(table_average) # Load the table of average from Excel


#=============================
# Setting up the page layout
#=============================

# Desiging the header
st.markdown("<h1 class='title'>Qualité de l'air en France</h1>", unsafe_allow_html=True) # Title

# Description text
st.markdown("""
La qualité de l'air peut être dégradée par des polluants qui peuvent être d’origine naturelle ou liés à l’activité humaine.  
La pollution de l’air a des effets significatifs sur la santé et l’environnement, qui engendrent des coûts importants pour la société.  

Les effets négatifs d’une mauvaise qualité de l’air sur la santé humaine incluent :
- Maladies cardiovasculaires  
- Cancers  
- Troubles respiratoires  

Parmi les effets sur l’environnement, on peut citer :
- La dégradation des bâtiments  
- La baisse des rendements agricoles (blé par exemple)  

Parmi les polluants suivis de près, on retrouve :  
- **Les particules ou poussières en suspension** (PM2.5 et PM10)  
- **Le dioxyde de soufre** (SO₂)  
- **L’ozone** (O₃)  
- **Le dioxyde d’azote** (NO₂)  

Cette plateforme permet de visualiser à quelle catégorie appartient chaque commune de France sur la base de leur émission de 2022.
""")

#==============================================
# Desiging the first section : Map with cluster
#=============================================

color_map = {
"Emissions importantes": "red", 
"Emissions moyennes": "orange", 
"Emissions faibles": "green"}
category_order = ["Emissions importantes", "Emissions moyennes", "Emissions faibles"]

st.markdown('<h2 class="subheader">Visualisation des classes</h2>', unsafe_allow_html=True)
data = {
"Latitude": dataset_df["latitude"].tolist(),
"Longitude": dataset_df["longitude"].tolist(),
"Cluster": dataset_df["cluster_name"].tolist()
}
cities_map = px.scatter_mapbox(
    data, 
    lat = "Latitude", 
    lon = "Longitude", 
    zoom = 3, 
    color = "Cluster",
    color_discrete_map = color_map,
    category_orders={"Cluster": category_order}, 
    mapbox_style='open-street-map'  # Choose map style (e.g., 'carto-positron', 'open-street-map')
)
# Display plot in Streamlit
st.plotly_chart(cities_map)

#==========================================
# Designing the second section
#==========================================
second_left_col, second_center_col, second_right_col = st.columns(3)

with second_left_col:
    st.subheader("Analyse rapide des catégories: Valeur minimales")
    # Display the cluster_analysis DataFrame with horizontal scrolling
    st.dataframe(df_min, height=212)

with second_center_col:
    st.subheader("Analyse rapide des catégories: Valeur moyennnes")
    # Display the cluster_analysis DataFrame with horizontal scrolling
    st.dataframe(df_average, height=212)

with second_right_col:
    st.subheader("Analyse rapide des catégories: Valeur maximales")
    # Display the cluster_analysis DataFrame with horizontal scrolling
    st.dataframe(df_max, height=212)

#======================================
# Defining the third section
#======================================
third_left_col, third_right_col = st.columns(2)

# Create a searchbox for the user to look for their city
third_left_col, third_right_col = st.columns(2)

# Create a searchbox for the user to look for their city
with third_left_col: 

    st.markdown('<h2 class="subheader">Trouver la classe à laquelle appartient votre commune</h2>', unsafe_allow_html=True)
    city_list = dataset_df["name"].dropna().unique().tolist()
    selected_city = st.selectbox("Select a city:", city_list) # Creating a searchable dropdown with a selectbox 
    st.write(f"You selected: {selected_city}")

    if selected_city:
        cluster_value = dataset_df[dataset_df["name"] == selected_city]["cluster_name"].iloc[0]  # Get the cluster value
      
        # Display the result
        st.success(f"🚀 **{selected_city} appartient à la catégorie : {cluster_value}**")

with third_right_col:
    filtered_df = dataset_df[dataset_df["name"] == selected_city]
    
    color_map = {
    "Emissions importantes": "red", 
    "Emissions moyennes": "orange", 
    "Emissions faibles": "green"}
    category_order = ["Emissions importantes", "Emissions moyennes", "Emissions faibles"]
    
    st.markdown('<h2 class="subheader">Localisation de votre commune</h2>', unsafe_allow_html=True)
    data = pd.DataFrame({
    "Latitude": [filtered_df["latitude"].values[0]], 
    "Longitude":[filtered_df["longitude"].values[0]],
    "Cluster": [filtered_df["cluster_name"].values[0]]
    })
    cities_map = px.scatter_mapbox(
        data, 
        lat = "Latitude", 
        lon = "Longitude", 
        zoom = 3, 
        color = "Cluster",
        color_discrete_map = color_map,
        category_orders={"Cluster": category_order}, 
        mapbox_style='open-street-map'  # Choose map style (e.g., 'carto-positron', 'open-street-map')
    )
    # Display plot in Streamlit
    st.plotly_chart(cities_map)
