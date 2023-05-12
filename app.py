import streamlit as st
import pandas as pd
import numpy as np
from numpy import dtype



def main():
    
    #TEXT DISPLAY
    
    st.title('titolo')
    st.header('analisi dati')
    st.subheader('basta un click')
    st.code('nessuno fa tutto da solo')
    st.write("descrizione")
    st.markdown('_Markdown_')
    st.caption('lol')
    st.write('lol')
    csv=st.file_uploader("drag your file here")
    if csv is not None:
        df=pd.read_csv(csv)
   
    
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