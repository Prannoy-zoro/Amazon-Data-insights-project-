import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from pandas import wide_to_long
from streamlit import subheader

# Clean prices first
df = pd.read_csv(r"C:\Users\prann\Desktop\Data Visualizationswebsite\Data-Visualizationswebsite\amazon.csv")
# Clean the price columns first

# Create savings column
st.set_page_config(layout="wide")

col1,col2,col3 = st.columns([3,2,2])

with col1 :
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['main_category'] = df['category'].str.split('|').str[0]
    category_rating = df.groupby('main_category')['rating'].mean().reset_index()
    fig = px.bar(
        category_rating,
        x='main_category',
        y='rating',
        title="Average Rating by Category",
        color='rating'
    )

    fig.update_layout(
        xaxis_tickangle=-30,
        height=600,
        yaxis_title="Average Rating",
        xaxis_title="Category"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Data Preview")
    st.dataframe(df[['actual_price','discounted_price','savings']].head(50))

with col2 :
    st.subheader("Null Values")
    st.write(df.isnull().sum())
    df = df.dropna()



with col3:
    cat_dist=df['main_category'].value_counts().reset_index()
    cat_dist.columns=['category','count']
    fig = px.pie(
        cat_dist,
        names='category',
        values='count',
        title="Product Distribution by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("My Dataset Columns")
    st.write(df.columns)
    st.subheader("Rating vs Discounted Price")
    df['main_category'] = df['category'].str.split('|').str[0]
    fig = px.scatter(
        df,
        x="rating",
        y="discounted_price",
        size='rating_count',
        color='main_category',
        title = "do higher-rated products get better discounts ?"
    )
    fig.update_layout(height=600,)
    st.plotly_chart(fig,use_container_width=True)

    st.dataframe(df['discount_percentage'])

    df['discount_percentage']=pd.to_numeric(
        df['discount_percentage'].astype(str).str.replace("%",""),
        errors='coerce'
    )

    st.subheader("After dropping duplicate values")
    st.write("Duplicate rows:", df.duplicated().sum())
