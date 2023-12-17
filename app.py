import streamlit as st
import pandas as pd
import numpy as np
from numpy import dtype
import time
from NLP import main as  NLP
from machineLearning import main as ml
from amavinos import main as amavinos

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
        ("Machine Learning", "Natural Language Processing" , "Amavinos")
        )
    
    if add_radio=="Amavinos":
        amavinos()

    if add_radio=="Machine Learning":
        ml()

        
    if add_radio=="Natural Language Processing":
        NLP()

            
                
        

if __name__ == "__main__":
    main()
    
#streamlit run app.py