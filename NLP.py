import streamlit as st
import pandas as pd
import numpy as np
import joblib
import spacy
import re

sentiment_lexicon = {
    "excellent": 3.0,
    "wonderful": 2.5,
    "fantastic": 2.5,
    "amazing": 2.5,
    "great": 2.0,
    "good": 1.5,
    "positive": 1.5,
    "awesome": 2.5,
    "superb": 2.0,
    "outstanding": 2.0,
    "terrific": 2.0,
    "delicious": 2.0,
    "tasty": 1.5,
    "yum": 1.5,
    "satisfying": 1.5,
    "enjoyable": 1.5,
    "love": 2.0,
    "like": 1.5,
    "enjoy": 1.5,
    "pleasant": 1.0,
    "neutral": 0.0,
    "average": 0.0,
    "mediocre": -1.0,
    "disappointing": -1.5,
    "bad": -2.0,
    "horrible": -2.5,
    "terrible": -2.5,
    "awful": -2.5,
    "unappetizing": -1.5,
    "inedible": -2.0,
    "disgusting": -2.5,
    "hate": -2.5,
    "loathe": -2.5,
    "despise": -2.5,
    "abhor": -2.5,
    "displeasing": -1.5,
    "unpleasant": -1.5,
    "unappetizing": -1.5,
    "bland": -1.0,
    "tasteless": -1.0,
    "disgust": -2.0,
    "repulsive": -2.5,
    "eccellente": 3.0,
    "meraviglioso": 2.5,
    "fantastico": 2.5,
    "straordinario": 2.5,
    "ottimo": 2.0,
    "buono": 1.5,
    "positivo": 1.5,
    "impressionante": 2.5,
    "superbo": 2.0,
    "eccezionale": 2.0,
    "terrificante": 2.0,
    "fresco": 2.0,
    "gustoso": 1.5,
    "delizioso": 1.5,
    "soddisfacente": 1.5,
    "incantevole": 1.5,
    "amato": 2.0,
    "piace": 1.5,
    "godere": 1.5,
    "piacevole": 1.0,
    "neutro": 0.0,
    "medio": 0.0,
    "mediocre": -1.0,
    "deludente": -1.5,
    "cattivo": -2.0,
    "orribile": -2.5,
    "terribile": -2.5,
    "atroce": -2.5,
    "non appetitoso": -1.5,
    "immangiabile": -2.0,
    "disgustoso": -2.5,
    "rancido": -2.5,
    "marcio ": -2.5,
    "vecchio": -2.5,
    "brutto": -2.5,
    "sgradevole": -1.5,
    "spiacevole": -1.5,
    "sporco": -1.5,
    "insipido": -1.0,
    "insapore": -1.0,
    "disgusto": -2.0,
    "ripugnante": -2.5,
    "mosca":-3,


}

nlp=spacy.load("en_core_web_md")

pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, sentiment_lexicon.keys())) + r')\b', flags=re.IGNORECASE)

def analyze_sentiment(text):
    matches = pattern.findall(text)
    sentiment_score = sum(sentiment_lexicon[match.lower()] for match in matches)
    return sentiment_score
    
#def analyze_sentiment(text):
    doc = nlp(text)
    sentiment_score = 0.0

    for token in doc:
        if token.text.lower() in sentiment_lexicon:
            sentiment_score += sentiment_lexicon[token.text.lower()]

    return sentiment_score
    
code='''{
    "excellent": 3.0,
    "wonderful": 2.5,
    "fantastic": 2.5,
    "amazing": 2.5,
    "great": 2.0,
    "good": 1.5,
    "positive": 1.5,
    "awesome": 2.5,
    "superb": 2.0,
    "outstanding": 2.0,
    "terrific": 2.0,
    "delicious": 2.0,
    "tasty": 1.5,
    "yum": 1.5,
    "satisfying": 1.5,
    "enjoyable": 1.5,
    "love": 2.0,
    "like": 1.5,
    "enjoy": 1.5,
    "pleasant": 1.0,
    "neutral": 0.0,
    "average": 0.0,
    "mediocre": -1.0,
    "disappointing": -1.5,
    "bad": -2.0,
    "horrible": -2.5,
    "terrible": -2.5,
    "awful": -2.5,
    "unappetizing": -1.5,
    "inedible": -2.0,
    "disgusting": -2.5,
    "hate": -2.5,
    "loathe": -2.5,
    "despise": -2.5,
    "abhor": -2.5,
    "displeasing": -1.5,
    "unpleasant": -1.5,
    "unappetizing": -1.5,
    "bland": -1.0,
    "tasteless": -1.0,
    "disgust": -2.0,
    "repulsive": -2.5,
    "eccellente": 3.0,
    "meraviglioso": 2.5,
    "fantastico": 2.5,
    "straordinario": 2.5,
    "ottimo": 2.0,
    "buono": 1.5,
    "positivo": 1.5,
    "impressionante": 2.5,
    "superbo": 2.0,
    "eccezionale": 2.0,
    "terrificante": 2.0,
    "fresco": 2.0,
    "gustoso": 1.5,
    "delizioso": 1.5,
    "soddisfacente": 1.5,
    "incantevole": 1.5,
    "amato": 2.0,
    "piace": 1.5,
    "godere": 1.5,
    "piacevole": 1.0,
    "neutro": 0.0,
    "medio": 0.0,
    "mediocre": -1.0,
    "deludente": -1.5,
    "cattivo": -2.0,
    "orribile": -2.5,
    "terribile": -2.5,
    "atroce": -2.5,
    "non appetitoso": -1.5,
    "immangiabile": -2.0,
    "disgustoso": -2.5,
    "rancido": -2.5,
    "marcio ": -2.5,
    "vecchio": -2.5,
    "brutto": -2.5,
    "sgradevole": -1.5,
    "spiacevole": -1.5,
    "sporco": -1.5,
    "insipido": -1.0,
    "insapore": -1.0,
    "disgusto": -2.0,
    "ripugnante": -2.5,
    "mosca":-3,

}'''


def show_footer():
    st.markdown("*ciao*")


def main():
    st.button("Re-run")
    st.title("Natural Language Processing")
    st.markdown("***")
    st.code(code,language="python")
    user_input = st.text_input("Metti qui la una recensione", "ins")
    model=joblib.load("models/nlp_modelGradient_Boosting.pkl")
    if user_input is not None:
        sentiment_val=analyze_sentiment(user_input)
        if sentiment_val>1.5:
            sentiment_class=1
        else:
            sentiment_class=0
        
        pred_sentiment = model.predict(([[sentiment_val,sentiment_class]]))
        if pred_sentiment==0:
            st.write(sentiment_val)
            st.write("purtroppo hai ricevuto una brutta recensione :/")
        else:
            st.write("un'altra ottima recensione")           


    show_footer()

if __name__ == "__main__":
    main()