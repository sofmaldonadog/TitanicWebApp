import pandas as pd
import streamlit as st
import matplotlib

df = pd.read_csv("titanic.csv")
df.columns = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
st.dataframe(df)

st.title("Edades de sobrevivientes")
graph1 = df.hist(column="Age",by="Survived")
st.pyplot(graph1)
st.markdown("De esto puedo ver que la gran mayoría de personas a bordo eran relativamente jóvenes, de entre 20 y 40 años de edad. La falta de personas mayores es entendible ya que antes la esperanza de vida generalmente era menor, y aparte las personas mayores estaban menos interesadas en aventuras como viajar en el Titanic. Como dato adicional, vemos que hubo un número un poco mayor de personas mayores que murieron a quienes sobrevivieron, posiblemente por dificultades motoras, y un grupo grande de jóvenes que sobrevivió, un resultado de la costumbre de que los niños tenían prioridad para salir")

st.title("Sobrevivientes por Género")
graph2 =df.groupby(["Sex"]).sum().plot(kind="pie",y="Survived",autopct="%1.0f%%",title="Titanic survivors by Gender",)
st.pyplot(graph2)
st.markdown("Esta gráfica nos muestra que la gran mayoría de personas que sobrevivieron eran mujeres, lo cuál tiene mucho sentido considerando la costumbre de que mujeres y niños saldrían del barco antes que el resto de las personas a bordo")

st.title("Sobrevivientes por Clase")
graph3 =df.hist(column="Pclass",by="Survived",bins=3)
st.pyplot(graph3)
st.markdown("En estos histogramas podemos ver que la mayoría de personas en primera clase sobrevivió, pero en las clases 2 y 3 este ya no es el caso. Particularmente en la 3ra clase, donde 3/4 de las personas que tenían este tipo de boletos terminaron muriendo.")

st.title("Familiares de pasajeros")
graph4 =df.hist(column="SibSp",by="Survived")
st.pyplot(graph4)
st.markdown("Algo interesante que se puede apreciar de estas gráficas es que las personas que sobrevivieron tenían máximo 4 familiares a bordo, mientras que hubieron pasajeros fallecidos con hasta 8 familiares")

st.title("Hijos de pasajeros")
graph5 =df.hist(column="Parch",by="Survived")
st.pyplot(graph5)
st.markdown("Estas gráficas muestran que la gran mayoría de quienes murieron no tenían hijos. Esto también es cierto en la que muestra a los sobrevivientes, pero en este caso la diferencia no es tan abrupta, reflejando el hecho de que la mayoría de niños a bordo, en general, sobrevivió")

st.title("Costo de boletos")
graph6 = df.hist(column="Fare",by="Survived")
st.pyplot(graph6)
st.markdown("Estos histogramas verifican lo que se ve arriba de que aquellas personas en las clases más lujosas sobrevivieron en mayores números, ya que la proporción de personas con boletos más caros de $200 que sobrevivieron supera a quienes no sobrevivieron, donde este número es casi inexistente")
