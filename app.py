import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
df.columns = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
st.dataframe(df)

st.title("Edades de sobrevivientes")
plt.figure()
df[df['Survived']==1]['Age'].hist(alpha=0.5, label='Survived')
df[df['Survived']==0]['Age'].hist(alpha=0.5, label='Not Survived')
plt.legend()
st.pyplot()
st.markdown("De esto puedo ver que la gran mayoría de personas a bordo eran relativamente jóvenes, de entre 20 y 40 años de edad. La falta de personas mayores es entendible ya que antes la esperanza de vida generalmente era menor, y aparte las personas mayores estaban menos interesadas en aventuras como viajar en el Titanic. Como dato adicional, vemos que hubo un número un poco mayor de personas mayores que murieron a quienes sobrevivieron, posiblemente por dificultades motoras, y un grupo grande de jóvenes que sobrevivió, un resultado de la costumbre de que los niños tenían prioridad para salir")

st.title("Sobrevivientes por Género")
plt.figure()
df.groupby(["Sex"]).sum()['Survived'].plot(kind="pie", autopct="%1.0f%%", title="Titanic survivors by Gender")
st.pyplot()
st.markdown("Esta gráfica nos muestra que la gran mayoría de personas que sobrevivieron eran mujeres, lo cuál tiene mucho sentido considerando la costumbre de que mujeres y niños saldrían del barco antes que el resto de las personas a bordo")

st.title("Sobrevivientes por Clase")
plt.figure()
df[df['Survived']==1]['Pclass'].hist(alpha=0.5, bins=3, label='Survived')
df[df['Survived']==0]['Pclass'].hist(alpha=0.5, bins=3, label='Not Survived')
plt.legend()
st.pyplot()
st.markdown("En estos histogramas podemos ver que la mayoría de personas en primera clase sobrevivió, pero en las clases 2 y 3 este ya no es el caso. Particularmente en la 3ra clase, donde 3/4 de las personas que tenían este tipo de boletos terminaron muriendo.")

st.title("Familiares de pasajeros")
plt.figure()
df[df['Survived']==1]['SibSp'].hist(alpha=0.5, label='Survived')
df[df['Survived']==0]['SibSp'].hist(alpha=0.5, label='Not Survived')
plt.legend()
st.pyplot()
st.markdown("Algo interesante que se puede apreciar de estas gráficas es que las personas que sobrevivieron tenían máximo 4 familiares a bordo, mientras que hubieron pasajeros fallecidos con hasta 8 familiares")

st.title("Hijos de pasajeros")
plt.figure()
df[df['Survived']==1]['Parch'].hist(alpha=0.5, label='Survived')
df[df['Survived']==0]['Parch'].hist(alpha=0.5, label='Not Survived')
plt.legend()
st.pyplot()
st.markdown("Estas gráficas muestran que la gran mayoría de quienes murieron no tenían hijos. Esto también es cierto en la que muestra a los sobrevivientes, pero en este caso la diferencia no es tan abrupta, reflejando el hecho de que la mayoría de niños a bordo, en general, sobrevivió")

st.title("Costo de boletos")
plt.figure()
df[df['Survived']==1]['Fare'].hist(alpha=0.5, label='Survived')
df[df['Survived']==0]['Fare'].hist(alpha=0.5, label='Not Survived')
plt.legend()
st.pyplot()
st.markdown("Estos histogramas verifican lo que se ve arriba de que aquellas personas en las clases más lujosas sobrevivieron en mayores números, ya que la proporción de personas con boletos más caros de $200 que sobrevivieron supera a quienes no sobrevivieron, donde este número es casi inexistente")
