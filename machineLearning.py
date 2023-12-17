import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import plotly.express as px
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

    
def main():
    
    wine_dataset = pd.read_csv("data/winequality-red.csv")
    st.dataframe(wine_dataset)
    

    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.image("data/quality_count.png")
        st.subheader("Numero di vini per ciascuna qualità")
   
    with col2:
        st.bar_chart(x = "quality", y = "volatile acidity", data = wine_dataset)
        st.subheader("acidità volatile e qualità")
    with col3:
        st.bar_chart(x = "quality", y = "citric acid", data = wine_dataset)
        st.subheader("acido citrico e qualità")

    st.image("data/corrML.png")
###### 
    
    st.title("prediciamo vini")
    myPca=joblib.load("models/PCA.pkl")
    model = joblib.load("models/wine_model.pkl")
    #prediction = model.predict(input_data_reshaped)
    #metti slide bars
    data = {
    "min": {},
    "max": {},
    "mean": {},}
    input_wine=[]

    for label in wine_dataset.columns[:-1]:
        # Access the column using square brackets
        df = wine_dataset[label]
        
        # Populate data dictionary
        data["min"][label] = df.min()
        data["max"][label] = df.max()
        data["mean"][label] = df.mean()
        selected_value = st.slider(label, float(df.min()), float(df.max()), float(df.mean()))
        input_wine.append(selected_value)


    input_wine_array = np.array(input_wine)
    input_wine_2d = input_wine_array.reshape(1, -1)

    trans = myPca.transform(input_wine_2d)
    st.write(trans)

    prediction = model.predict(trans)

    if(prediction[0] == 0):
        st.text("Poor Quality Wine.")
        
    else:
        st.text("Good Quality Wine.")
        st.balloons()
    




if __name__ == "__main__":
    main()