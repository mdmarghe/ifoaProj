import streamlit as st
import pandas as pd
import numpy as np
from numpy import dtype
from tensorflow import keras
import time
from deepLearning import main as  dl

def add_bg_from_url():    #background
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://upload.wikimedia.org/wikipedia/commons/8/83/Solid_white_bordered.svg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )





def main():# Read the image file
    add_bg_from_url()

    
    #TEXT DISPLAY
    
    st.title('Benvenuti nel mio sito')
    st.header('Margherita Nuccio')

    with st.sidebar:
        add_radio = st.radio(
        "Opzioni",
        ("Machine Learning", "Deep Learning","Generative Art", "Amavinos")
        )
    
    if add_radio=="Amavinos":
        st.write("progetto stage")

        
    if add_radio=="Deep Learning":
        dl()
        
    if add_radio=="Pulizia dati":
        st.write('ehehehehhehe')

        #TARGET SELECTION
        headers=df.columns.to_list()
        target=st.selectbox("select target", headers, index=0, 
                key=None, help=None, on_change=None, 
                args=None, kwargs=None, disabled=False)
        target_index=headers.index(target)
        
        labels=headers.copy()
        labels.remove(target)
        st.write(labels)
        y=df.iloc[:,target_index]
        #st.dataframe(y)
        X=df.loc[:,labels]
        #st.dataframe(X)
        
        st.subheader("Analysis type")
        model_type  =st.selectbox("select model type", {'linear regression':1, 'logistic regression':2}, index=0, 
                key=None, help=None, on_change=None, 
                args=None, kwargs=None, disabled=False)
        st.write(model_type)
        
        
        
            
                
        

if __name__ == "__main__":
    main()
    
#streamlit run app.py