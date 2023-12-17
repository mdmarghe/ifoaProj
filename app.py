import streamlit as st
import pandas as pd
import numpy as np
from numpy import dtype
from tensorflow import keras
import time
from NLP import main as  NLP
from machineLearning import main as ml

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






def main():# Read the image file
    background()

    
    #TEXT DISPLAY
    
    st.title('Benvenuti nel mio sito')
    st.header('Margherita Nuccio')

    with st.sidebar:
        add_radio = st.radio(
        "Opzioni",
        ("Machine Learning", "Natural Language Processing" , "Amavinos", "Generative Art")
        )
    
    if add_radio=="Amavinos":
        st.write("progetto stage")

    if add_radio=="Machine Learning":
        ml()

        
    if add_radio=="Natural Language Processing":
        NLP()
        
    if add_radio=="Pulizia dati":
        st.write('ehehehehhehe')
        
        st.subheader("Analysis type")
        model_type  =st.selectbox("select model type", {'linear regression':1, 'logistic regression':2}, index=0, 
                key=None, help=None, on_change=None, 
                args=None, kwargs=None, disabled=False)
        st.write(model_type)
        
        
        
            
                
        

if __name__ == "__main__":
    main()
    
#streamlit run app.py