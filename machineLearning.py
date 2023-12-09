import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import joblib
def background():
    st.markdown(
    """
    <style>
    .reportview-container {
        background-color:#800020
    }
   .sidebar .sidebar-content {
        background: #800021
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
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
    st.title("prediciamo vini")

    model = joblib.load("wine_model")
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


    #Ora facciamo il test
    input_wine_array=np.asarray(input_wine)
    input_wine_reshaped=input_wine_array.reshape(1,-1)
    prediction=model.predict(input_wine_reshaped)

    if(prediction[0] == 0):
        st.text("Poor Quality Wine.")
        
    else:
        st.text("Good Quality Wine.")
        st.balloons()
    




if __name__ == "__main__":
    main()