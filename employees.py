import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Employees.csv')


st.title('Empleados')

# Sidebar

st.sidebar.title("Luis Enrique Romero Pérez")

st.sidebar.write("Matricula: zs21004524.")
st.sidebar.write("zs21004524@estudiantes.uv.mx")

st.sidebar.image("https://firebasestorage.googleapis.com/v0/b/paradigmas-luigi196362.appspot.com/o/javascript%2Fimages%2Fcredencial.jpg?alt=media&token=ffba3513-0c65-4540-8bdf-140a9ba8f468")

st.sidebar.title('Controles de la Aplicación')

# Checkbox para mostrar/ocultar el dataframe
show_df = st.sidebar.checkbox('Mostrar/Ocultar DataFrame Completo')
if show_df:
    st.dataframe(df)


# Búsqueda por Id de empleado
employee_id = st.sidebar.text_input('Buscar por Id de empleado')
if employee_id:
    st.subheader("Filtro por id")
    filtered_employee = df[df['Employee_ID'] == employee_id]
    st.write(f"Total de empleados con Id {employee_id}: {filtered_employee.shape[0]}")
    st.dataframe(filtered_employee)

# Filtro por Nivel Educativo
st.subheader("Filtro por Nivel Educativo")
education_level = st.sidebar.selectbox('Filtrar por Nivel Educativo', df['Education_Level'].unique())
filtered_education = df[df['Education_Level'] == education_level]
st.write(f"Total de empleados con nivel educativo {education_level}: {filtered_education.shape[0]}")
st.dataframe(filtered_education)

# Filtro por Ciudad (Hometown)
st.subheader("Filtro Ciudad")
hometown = st.sidebar.selectbox('Filtrar por Ciudad', df['Hometown'].unique())
filtered_hometown = df[df['Hometown'] == hometown]
st.write(f"Total de empleados en {hometown}: {filtered_hometown.shape[0]}")
st.dataframe(filtered_hometown)

# Filtro por Unidad (Unit)
st.subheader("Filtro por Unidad Funcional")
unit = st.sidebar.selectbox('Filtrar por Unidad Funcional', df['Unit'].unique())
filtered_unit = df[df['Unit'] == unit]
st.write(f"Total de empleados en la unidad {unit}: {filtered_unit.shape[0]}")
st.dataframe(filtered_unit)

# Gráfica de Histograma por Edad
st.subheader('Histograma de empleados por edad')
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df['Age'], bins=10, edgecolor='black')
ax.set_title('Histograma de Edad de Empleados')
ax.set_xlabel('Edad')
ax.set_ylabel('Número de empleados')
st.pyplot(fig)

# Gráfica de Frecuencia por Unidad Funcional
st.subheader('Frecuencia de empleados por Unidad Funcional')
fig, ax = plt.subplots(figsize=(8, 6))
df['Unit'].value_counts().plot(kind='bar', edgecolor='black', ax=ax)
ax.set_title('Frecuencia de Empleados por Unidad Funcional')
ax.set_xlabel('Unidad Funcional')
ax.set_ylabel('Número de empleados')
st.pyplot(fig)

# Gráfica de Deserción por Ciudad (Hometown)
st.subheader('Deserción por Ciudad')
desertion_by_city = df.groupby('Hometown')['Attrition_rate'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 6))
desertion_by_city.plot(kind='bar', edgecolor='black', ax=ax)
ax.set_title('Índice de Deserción por Ciudad')
ax.set_xlabel('Ciudad')
ax.set_ylabel('Índice de Deserción')
st.pyplot(fig)

# Gráfica de Edad vs Tasa de Deserción
st.subheader('Edad vs Tasa de Deserción')
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Age'], df['Attrition_rate'], edgecolor='black')
ax.set_title('Relación entre Edad y Tasa de Deserción')
ax.set_xlabel('Edad')
ax.set_ylabel('Tasa de Deserción')
st.pyplot(fig)

# Gráfica de Tiempo de Servicio vs Tasa de Deserción
st.subheader('Tiempo de Servicio vs Tasa de Deserción')
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Time_of_service'], df['Attrition_rate'], edgecolor='black')
ax.set_title('Relación entre Tiempo de Servicio y Tasa de Deserción')
ax.set_xlabel('Tiempo de Servicio')
ax.set_ylabel('Tasa de Deserción')
st.pyplot(fig)
