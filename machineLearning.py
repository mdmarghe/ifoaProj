import numpy as np
import pandas as pd
import streamlit as st

def main():
    wine_dataset = pd.read_csv("data/winequality-red.csv")
    st.dataframe(wine_dataset)



if __name__ == "__main__":
    main()