import streamlit as st
import pandas as pd
import joblib


def show_footer():
    st.markdown("*ciao*")


def main():
    st.button("Re-run")
    st.title("Natural Language Processing")
    st.markdown("***")
    user_input = st.text_input("Metti qui la una recensione", "")
    model=joblib.load("models/nlp_modelGradient Boosting")
    pred_sentiment = model.predict(user_input)
    

    show_footer()

if __name__ == "__main__":
    main()