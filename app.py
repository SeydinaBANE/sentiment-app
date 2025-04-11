import streamlit as st
from textblob import TextBlob

st.title("Analyse de sentiment")

st.write("Taper un text , un commentaire ou un tweet, et je te dis si c'est positif, neutre ounegatif")

#Entrer de l'untilisateur
text =st.text_area("Ton text ic")

if st.button("Analyse"):
    if text.strip() =="":
        st.warning("Ecris quelque chose d'abord")
    else :
        blob =TextBlob(text)
        polarite =blob.sentiment.polarity
        st.write(f"**Polarité :** {polarite:.2f}")
        if polarite >0.1:
            st.success("Sentiment :**POSITIF**")
        elif polarite <0.1:
            st.success("Sentiment :**NEGATIF**")
            
        else:
            st.info("Sentiment :**Neutre**")    
                