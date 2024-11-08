import pandas as pd
import plotly.express as px
import streamlit as st
        
data = pd.read_csv("vehicles_us.csv") # leer los datos

print(data)

st.header('Analisis sobre las preferencias vacaiones en playa o montaña en personas de USA')

st.write('En esta página analizaremos el comportamiento de más de 500,000 residentes americanos y sus preferencias para lugares para descansar, según diferentes criterios.')


hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de la preferencia del lugar vacacional')
            
# crear un histograma
    fig = px.histogram(data, x="Preference")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


#Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión. 

hist_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un gráfico de dispersion para el conjunto de datos de la preferencia del lugar vacacional')
            
# crear un histograma
    fig = px.scatter(data, x="Preference")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

# crear un histograma
    fig= px.histogram(data, x="Preference")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)