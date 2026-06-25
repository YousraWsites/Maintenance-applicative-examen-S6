import streamlit as st

st.title("Convertisseur de devises")

rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130
}

amount = st.number_input("Montant :", min_value=0.0, format="%.2f")
from_currency = st.selectbox("De :", rates.keys())
to_currency = st.selectbox("Vers :", rates.keys())


#AVANT
#if st.button("Convertir"):
    #result = amount * rates[to_currency] / rates[from_currency]
    #st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")


if st.button("Convertir"): #il s'execute quand user cliquise qur bouton
      if amount <= 0:      # on verifie que amount ne sois pas inferireur ou = à zero     
          st.error("Le montant doit être supérieur à zéro.")  #afficher message d'erreur rouge (st.error), STOP
      else:                                    # sinon
          result = amount * rates[to_currency] / rates[from_currency] #on ramene en euro ( devise de reference) puis on convertis en devise cible 
          st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}") #on affihce le resultat 


