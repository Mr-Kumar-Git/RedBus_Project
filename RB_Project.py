import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from itables import to_html_datatable
import mysql.connector as sql

st.set_page_config(page_title="RedBUS",
                   layout= "wide",
                   initial_sidebar_state= "expanded")
st.image("E:/Data Science/RedBus_Project/304315.png")
hide_streamlit_style = """ <html> <body><h1 style="font-family:Google Sans;font-size:40px"> Red Bus</h1></body>  </html>  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


Database=sql.connect(host='localhost',user='root',password='161121',database='redbus')
cursor=Database.cursor()


Col1,Col2=st.columns(2)
with Col1:
    st.image("E:/Data Science/RedBus_Project/about2.PNG")
    st.image("E:/Data Science/RedBus_Project/about3.PNG")
    st.image("E:/Data Science/RedBus_Project/about3.5.PNG")
with Col2:
    st.image("E:/Data Science/RedBus_Project/about4.PNG")
    st.image("E:/Data Science/RedBus_Project/about5.PNG")
    st.image("E:/Data Science/RedBus_Project/about6.PNG")



Col3,Col4=st.columns([0.2,0.5])
with Col3:
        components.html("""<html><body><h3 style="font-family:Google sans; font-size:40px"> Search For a Bus</h3></body></html>""",)
        hide_streamlit_style="""<html><h1 style="font-family:Google Sans; font-size:30px">Select a State</h1></html>"""
        st.markdown(hide_streamlit_style,unsafe_allow_html=True)
        States=['Andhra Pradesh','Karnataka','Kadamba','Rajasthan','South Bengal','Telangana','Uttar pradesh','West Bengal']
        State=st.selectbox('Select a State',States,label_visibility='hidden') 
        cursor.execute(f'''
                                SELECT From_point,To_point from busdetails where State='{State}';
        ''')
        df_1=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)
        hide_streamlit_style="""<html><h1 style="font-family:Google Sans; font-size:30px">Select a Source</h1></html>"""
        st.markdown(hide_streamlit_style,unsafe_allow_html=True)
        From=st.selectbox('Enter a Source',df_1['From_point'].unique(),label_visibility='hidden')
        hide_streamlit_style="""<html><h1 style="font-family:Google Sans; font-size:30px">Select a Destination</h1></html>"""
        st.markdown(hide_streamlit_style,unsafe_allow_html=True)
        To=st.selectbox('Enter a Destinaton',df_1['To_point'].unique(),label_visibility='hidden')
               
button=st.button('Submit')
if button:
    cursor.execute(f'''
                        SELECT Bus_name,Bus_type,Starting_time,Ending_time,Duration,Seats_available,Ratings,Price from busdetails where State='{State}' and From_point='{From}' and To_point='{To}' order by Ratings desc ;
        ''')
    df=pd.DataFrame(cursor.fetchall(),columns=cursor.column_names)  
    if len(df)!=0:
        components.html("""<html><body"><h3 style="font-family:Google sans; font-size:40px"> Bus Details in Table View</h3></body></html>""",)
        html(
            to_html_datatable(
                df,
            maxBytes=0,
            ),
            height=660,
        )
    else:
         st.markdown("No Buses to show")




hide_streamlit_style = """ <html> <body><h1 style="font-family:Google Sans; color:blue;font-size:40px"> About this Project </h1>
        <p style="font-family:Google Sans; font-size:20px",color:black>
        <b>Project_Title</b>: <br>Airbnb Analysis Using Streamlit and Plotly <br>
        <b>Technologies_Used</b> :<br> Web Scraping using Selenium, Python, Streamlit , SQL
        <br>
        <b>Website oF redbus</b>:  <a href="https://www.redbus.in/">Link</a><br>
        <b>Domain </b> : Transportation <br>
        <b>Problem Statement:</b>: <br>1.The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data<br>
                2.By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability.<br>
                3.By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.<br>
        <b>Author</b> : KUMARAGURUBARA.A <br>
        </p>
        </body>  </html>  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)