import streamlit as st 
import pandas as pd 
import numpy as np 
import psycopg2
from datetime import date, datetime, timedelta
import controllers.HoursController as HoursController
import models.Hours as hours 



#configurando o nome da página
st.set_page_config(page_title = 'MDGeo Controle de Horas')

#colocando título
st.title('Controle Semanal de Horas')


st.sidebar.title('Menu')

paginas = st.sidebar.selectbox('Selecione uma opção', ['Registro de Horas', 'Consultar'])


if paginas == 'Registro de Horas':
    st.header('Formulário de Registro')
    employees = ('Julio Yasbek', 'Roberto Delphim', 'Adrieli Thalia', 'Vitor Díaz','Matheus Fanelli','André Paes',
                'Clóvis Souza','Leonardo Pereira','Simone Pereira','Daniel Rezende','Pedro Xavier', 'Rodrigo Brust',
                'Jessica Katayama'

    )


    with st.form(key ='hours_input'):
        name = st.selectbox('Qual seu nome?', employees)

        cc = st.text_input('Centro de Custo')
        st.subheader('Selecione quantas horas foram investidas no projeto esta semana:')


        col1, col2 = st.columns(2)

        date_mon = col1.date_input('Segunda')
        hours_mon = col2.slider('Horas trabalhadas na Segunda', 0, 10)
        

        date_tue = col1.date_input('Terça')
        hours_tue = col2.slider('Horas trabalhadas na Terça', 0, 10)
        

        date_wed = col1.date_input('Quarta')
        hours_wed = col2.slider('Horas trabalhadas na Quarta', 0, 10)
        

        date_thu = col1.date_input('Quinta')
        hours_thu = col2.slider('Horas trabalhadas na Quinta', 0, 10)
        

        date_fri = col1.date_input('Sexta')
        hours_fri = col2.slider('Horas trabalhadas na Sexta', 0, 10)
        


        commentary = st.text_area('Comentários')


        send_btn = st.form_submit_button('Enviar!')

    if send_btn:
        hours.name = name
        hours.cc = cc
        hours.date_mon = date_mon
        hours.hours_mon = hours_mon
        hours.date_tue = date_tue
        hours.hours_tue = hours_tue
        hours.date_wed = date_wed
        hours.hours_wed = hours_wed
        hours.date_thu = date_thu
        hours.hours_thu = hours_thu
        hours.date_fri = date_fri
        hours.hours_fri = hours_fri
        hours.commentary = commentary

        HoursController.incluir(hours)

        st.success('Registrado!')
    

if paginas == 'Consultar':

    st.header("Consulta SQL")

    # Columns/Layout
    col1,col2 = st.columns(2)

    with col1:
        with st.form(key='query_form'):
            raw_code = st.text_area("Insira o código SQL aqui",
             value = "SELECT * FROM bd_horas"
            
            )
            
            submit_code = st.form_submit_button("Execute")
        
    # Results Layouts
    with col2:
        if submit_code:
            st.info("Query Enviada!")
            st.write("Você pode copiar o código abaixo, se desejar.")
            st.code(raw_code)
            query_results = HoursController.consultar(query = raw_code)
            query_df = pd.DataFrame(query_results)
    
    hoursList = []

    for item in HoursController.consultar(raw_code):
        hoursList.append([
            item.name, item.cc, item.date_mon, item.hours_mon,
            item.date_tue, item.hours_tue, item.date_wed,
            item.hours_wed, item.date_thu, item.hours_thu,
            item.date_fri, item.hours_fri
        ])

    query_df = pd.DataFrame(
        hoursList,
        columns=['employee_name', 'cc_number', 'mon', 'mon_h', 'tue', 'tue_h', 'wed', 'wed_h', 'thu', 'thu_h', 'fri', 'fri_h'  
        ]
    )
    st.header("Resultado")
    st.dataframe(query_df)
    
    csv = query_df.to_csv().encode('utf-8')
    st.download_button(
    "Baixar Tabela",
    csv,
    "controle_de_horas_mdgeo.csv",
    "text/csv",
    key="download-csv"
    )
