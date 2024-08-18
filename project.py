from turtle import home
import streamlit as st
import pandas as pd
import time as ts 
from streamlit_option_menu import option_menu
import mysql.connector
from PIL import Image

location1=pd.read_csv(r"D:\project\andra_routes.csv")
andra=[]
for i,k in location1.iterrows():
    andra.append(k["andra_routes"])

location2=pd.read_csv(r"D:\project\astc_routes.csv")
astc=[]
for i,l in location2.iterrows():
    astc.append(l["astc_routes"])

location3=pd.read_csv(r"D:\project\hrtc_routes.csv")
hrtc=[]
for i,m in location3.iterrows():
    hrtc.append(m["hrtc_routes"])

location4=pd.read_csv(r"D:\project\kerala_routes.csv")
kerala=[]
for i,n in location4.iterrows():
    kerala.append(n["kerala_routes"])

location5=pd.read_csv(r"D:\project\ktcl_routes.csv")
ktcl=[]
for i,o in location5.iterrows():
    ktcl.append(o["ktcl_routes"])

location6=pd.read_csv(r"D:\project\rsrtc_routes.csv")
rsrtc=[]
for i,p in location6.iterrows():
    rsrtc.append(p["rsrtc_routes"])

location7=pd.read_csv(r"D:\project\sbstc_routes.csv")
sbstc=[]
for i,q in location7.iterrows():
    sbstc.append(q["sbstc_routes"])

location8=pd.read_csv(r"D:\project\tsrtc_routes.csv")
tsrtc=[]
for i,r in location8.iterrows():
    tsrtc.append(r["tsrtc_routes"])

location9=pd.read_csv(r"D:\project\upsrtc_routes.csv")
upsrtc=[]
for i,s in location9.iterrows():
    upsrtc.append(s["upsrtc_routes"])

location10=pd.read_csv(r"D:\project\wbtc_routes.csv")
wbtc=[]
for i,t in location10.iterrows():
    wbtc.append(t["wbtc_routes"])

option=option_menu(
menu_title="Menu",
options=["Home","🚌Search buses"],
icons=["house","location"],
orientation="horizondal")

if option == "Home":
    st.title("REDBUS")
    st.markdown("---")
    st.header("welcome to Redbus")
    st.subheader("India's No. 1 Online Bus Ticket Booking Site..")
    image=Image.open(r"D:\total project\REDBUS.PNG")
    st.image(image)

if option == "🚌Search buses":
    route_selection=st.selectbox("select the city name",options=["Andra","Assam","Himachal","Kerala","Kadamba","Rajasthan","South bengal","Telangana","Uttar pradesh","West bengal"])
    price_filter=st.radio("price set",options=["100 - 500","500 - 1000","1000 - 1500","1500 - 2000","2000 above"])
    if route_selection=="Andra":
        filter=st.selectbox("list of routes",andra)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)
    elif route_selection == "Assam":
        filter=st.selectbox("list of routes",astc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "Himachal":
        filter=st.selectbox("list of routes",hrtc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "Kerala":
        filter=st.selectbox("list of routes",kerala)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "Kadamba":
        filter=st.selectbox("list of routes",ktcl)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "Rajasthan":
        filter=st.selectbox("list of routes",rsrtc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "South bengal":
        filter=st.selectbox("list of routes",sbstc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "Telangana":
        filter=st.selectbox("list of routes",tsrtc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "Uttar pradesh":
        filter=st.selectbox("list of routes",upsrtc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        
    elif route_selection == "West bengal":
        filter=st.selectbox("list of routes",wbtc)
        sql=mysql.connector.connect(host="localhost",user="root",password="",database="project")
        mycursor=sql.cursor(buffered=True)
        if price_filter=="100 - 500":
            query="select * from red_bus where price between 100 and 500 and route_name=%s "
        elif price_filter == "500 - 1000":
            query=("select * from red_bus where Price between 500 and 1000 and route_name=%s")
        elif price_filter == "1000 - 1500":
            query=("select * from red_bus where price between 1000 and 1500 and route_name =%s")
        elif price_filter == "1500 - 2000":
            query=("select * from red_bus where price between 1500 and 2000 and route_name=%s")
        else:
            query=("select * from red_bus where price >2000 and route_name=%s")
        mycursor.execute(query,(filter,))
        output=mycursor.fetchall()
        df=pd.DataFrame(output,columns=["Id","Route_name","Route_link","Bus_name","Bus_type","price","Seat_availability","Departing_time","Duration","Reaching_time","Star_rating"])            
        st.write(df)        






