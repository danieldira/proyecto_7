# Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header('Vehículos en EUA')

# Crear un botón
if __name__ == "__main__":
    car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
    hist_button = st.button('Construir histograma')  # crear un botón
    disp_check = st.checkbox('Dispersión: odometer vs price')  # otro botón

    if hist_button:  # al hacer clic en el botón
        # escribir un mensaje
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches.')
        # crear un histograma
        fig = px.histogram(car_data, x="odometer")
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

    if disp_check:
        st.write(
            'Creación de un diagrama de disperción que compara odómetro vs precio.')
        # crear un gráfico de dispersión
        fig = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig, use_container_width=True)
