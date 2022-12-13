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
mydict = cp.load(urlopen("https://github.com/Dimitri-J/Social_Network_Brief/raw/main/Files/fl.pkl")) 

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

age= "age"
sex= "sex"
salaire= "salaire"
test= []
y_pred= []


# Config page Streamlit

st.set_page_config(page_title="e-Shop Predictor", layout="wide")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://4kwallpapers.com/images/wallpapers/macos-monterey-stock-purple-dark-mode-layers-5k-3840x2160-5896.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.subheader('Bonjour,')
st.title("E-Shop simulator")
st.write("[Clique-ici >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

# Formulaire de dimentions iris

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sex")
    sex = st.radio(label = "Indiquer le sex", options =('Homme', 'Femme'), key=sex)
    st.write('Le sex est ', sex)
    if sex=='Homme':
        sex=1
    else:
        sex=0

with col2:
    st.header("Age")
    age = st.slider("Indiquer l'âge", key=age, min_value = 18, max_value = 130, value = 25)
    st.write('The current number is ', age, 'ans')

with col3:
    st.header("Salaire")
    salaire = st.number_input('Indiquer le salaire potentiel', key=salaire,value = 10, min_value=10, step = 1)
    st.write('Le salaire potentiel est de ', salaire, 'k €')


if st.button("Estimation d'achat"):
    import time

    col_b1, col_b2 = st.columns([2,1])
    test = np.array([sex, age, salaire])

    print(test)
    test = test.reshape(1, -1)
    print(test)
    predic = mydict["model"].predict(mydict["stand"].transform(test))
    print(predic)
    if predic==1 :
        st.metric("Estimation d'achat : ", "Oui",)
        html_string = """
                <audio autoplay>
                <source src="https://www.myinstants.com/media/sounds/donate-sound-here-comes-the-money.mp3" type="audio/mp3">
                </audio>
                """

        sound = st.empty()
        sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
        time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
        sound.empty()  # optionally delete the element afterwards
    else:
        st.metric("Estimation d'achat : ", "Non",)
        html_string = """
                <audio autoplay>
                <source src="https://www.myinstants.com/media/sounds/engineer_no01_1.mp3" type="audio/mp3">
                </audio>
                """

        sound = st.empty()
        sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
        time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
        sound.empty()  # optionally delete the element afterwards
        