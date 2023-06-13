import streamlit as st
import pandas as pd
import numpy as np
from numpy import dtype
import time

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-photo/banner-starry-outer-space-background-texture_78899-4532.jpg");
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
    
    st.title(':red[Benvenuto nel mio sito]')
    st.header(':red[analizza i tuoi dati]')
    st.subheader(':orange[basta un click]')
    
    st.write("nessuno fa tutto da solo")
    csv=st.file_uploader("drag your file here")
    with st.sidebar:
        add_radio = st.radio(
        "Opzioni",
        ("Pulizia dati", "EDA","Analisi","Report")
        )
    if csv is not None:
        df=pd.read_csv(csv)
        
    if add_radio=="Pulizia dati":
        st.write('soocs')


    



   
    
        #DATA DISPLAY
    
        st.dataframe(df)
        #st.table(df.iloc[:,10])
        #st.json({1:'b'})
        #st.metric()
    
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