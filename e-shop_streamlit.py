import matplotlib as mpl
import matplotlib.pyplot as plt
import mysql.connector as mysql
import numpy as np
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import streamlit as st
import random
import json
import pickle
import matplotlib.patches as mpatches
from IPython.display import clear_output
from sklearn import datasets
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# Charge le modèle enregistré et test à partir du fichier chargé
import cloudpickle as cp
from urllib.request import urlopen
mydict = cp.load(urlopen("https://github.com/Dimitri-J/Cars_Seller/raw/main/cars.pkl")) 

# mydict = pickle.load(pick)         # load file content as mydict
# f.close()                       
# test = np.array([6.7, 3.1, 5.6, 2.4])
# test = test.reshape(1, -1)
print(mydict)
# mydict["model"].predict(mydict["stand"].transform(test))



# with open('fl.pkl', 'rb') as f: # 'r' for reading; can be omitted
#     mydict = pickle.load(f)         # load file content as mydict
#     f.close()                       
#     # test = np.array([6.7, 3.1, 5.6, 2.4])
#     # test = test.reshape(1, -1)
#     print(mydict)
#     # mydict["model"].predict(mydict["stand"].transform(test))


# Déclaration de variable formulaire

# 'marque', 'fuelsystem', 'doornumber', 'carwidth', 'curbweight','enginesize', 'horsepower'

marque= "marque"
fuelsystem= "fuelsystem"
doornumber= "doornumber"
carwidth="carwidth"
curbweight="curbweight"
enginesize="enginesize"
horsepower="horsepower"
test= []
y_pred= []


# Config page Streamlit

st.set_page_config(page_title="e-Shop Car Predictor", layout="wide")
st.markdown(
         f"""
         <style>
         .stApp {{
            background-image: url("https://w0.peakpx.com/wallpaper/440/206/HD-wallpaper-black-background-car-cars-vehicles.jpg");
            background-color: black;
            background-attachment: local;
            background-position: center;
            background-size: 35%;
            background-repeat: no-repeat;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.title("E-Shop Car predictor")
st.write("[Clique-ici >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

# Formulaire de dimentions iris

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Marque")
    marque = st.selectbox(label = "Indiquer la marque", options =('Nissan', 'alfa-romero', 'audi', 'bmw', 'buick', 'chevrolet',
       'dodge', 'honda', 'isuzu', 'jaguar', 'maxda', 'mazda', 'mercury',
       'mitsubishi', 'nissan', 'peugeot', 'plymouth', 'porcshce',
       'porsche', 'renault', 'saab', 'subaru', 'toyota', 'toyouta',
       'vokswagen', 'volkswagen', 'volvo', 'vw'), key=marque)
    st.write('La marque choisi est ', marque)
    marque = mydict["le_9"].transform([marque])
    
with col2:
    st.header("Fuelsystem")
    fuelsystem = st.selectbox(label = "Indiquer le système d'injection", options =('1bbl', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi', 'spdi', 'spfi'), key=fuelsystem)
    st.write('Le type de motorisation est ', str(fuelsystem))
    fuelsystem = mydict["le_8"].transform([fuelsystem])
    
with col3:
    st.header("Doors")
    doornumber = st.selectbox(label = "Indiquer le nombre de portes", options =('four', 'two'), key=doornumber)
    st.write('Le nombre de porte est ', str(doornumber))
    doornumber = mydict["le_2"].transform([doornumber])

col4, col5, col6, col7 = st.columns(4)
    
with col4:
    st.header("Largeur véhicule")
    carwidth = st.slider("Indiquer la largeur de la voiture", key=carwidth, min_value = 55, max_value = 75, value = 65)
    st.write('La largeur de la voiture fait', str(carwidth))

with col5:
    st.header("Poid véhicule")
    curbweight = st.slider("Indiquer le poid de la voiture", key=curbweight, min_value = 1400, max_value = 4100, value = 2000)
    st.write('La largeur de la voiture fait', str(curbweight))

with col6:
    st.header("Dimension moteur")
    enginesize = st.slider("Indiquer la cylindré de la voiture", key=enginesize, min_value = 55, max_value = 350, value = 120)
    st.write('La largeur de la voiture fait', str(enginesize))
    print(type)

with col7:
    st.header("Puissance moteur")
    horsepower = st.slider("Indiquer la puissance de la voiture", key=horsepower, min_value = 55, max_value = 350, value = 120)
    st.write('La largeur de la voiture fait', str(horsepower))

if st.button("Estimation d'achat"):
    import time

    col_b1, col_b2 = st.columns([2,1])

    test = np.array([marque, fuelsystem, doornumber,carwidth,curbweight,enginesize,horsepower])
    print(test)
    test = test.reshape(1, -1)
    print(test)
    predic = mydict["model"].predict(test)
    print(predic)
    st.write("Le prix est estimé à ",str(round(float(predic), 2))," $")

        