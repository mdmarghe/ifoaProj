import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
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

if __name__ == "__main__":
    main()