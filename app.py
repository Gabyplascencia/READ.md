import pandas as pd
import plotly.express as px
import streamlit as st
        
data = pd.read_csv("vehicles_us.csv") # enlace para leer los datos del data a analizar


st.header('Visualización sobre los datos de los carros')

st.write("En esta página analizaremos la relacion entre los carros y sus precios y las condiciones en las cuales se encuentran actualmente para su venta")

#se crea un boton para construir un histograma
hist_button = st.button('Visualizar un histograma de la relación entre el precio y la condición del auto') # crear un botón
        
if hist_button: # indicación al hacer clic en el botón
# escribir un mensaje sobre de que trata el histograma
    st.write('Creación de un histograma para la relación precio y calidad')
            
# comdandos para crear un histograma
    fig = px.histogram(data, x="condition", y="price",
                       color="condition", 
                       title="HIstograma de la relació precio y condición de un automóvil")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



#Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión. 
scatter_button = st.button('Construir gráfico de dispersión') # nombre del botón
        
if scatter_button: # intrucción para hacer clic en el botón
# escribir un mensaje para visualiar la gráfica
    st.write('Creación de un gráfico de dispersion para los autos y sus modelos')
            
# comando para crear un gráfico de dispersión
    fig = px.scatter(data, x="price", y="model_year",
                     color="model", title= "Dispersión entre el modelo y el precio del auto")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# comando para crear una casilla de verificación
build_histogram = st.checkbox('Construir una caja de verificación')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Visualizar autos basados en su tipo de combbustible')

# crear un histograma
    fig= px.histogram(data, x="fuel")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)