import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("amazon.csv")



st.set_page_config(layout="wide")
st.markdown("""
    <h1 style='text-align: center; padding-top: 10px; margin-bottom: 40px;'>
        Amazon Data Analysis
    </h1>
    """, unsafe_allow_html=True)
col1,col2,col3 = st.columns([3,3,2])


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


with col2 :

    st.subheader("Rating vs Discounted Price")
    df['main_category'] = df['category'].str.split('|').str[0]
    fig = px.scatter(
        df,
        x="rating",
        y="discounted_price",
        size='rating_count',
        color='main_category',
        title="do higher-rated products get better discounts ?"
    )
    fig.update_layout(height=600, )
    st.plotly_chart(fig, use_container_width=True)
    df['discount_percentage']=pd.to_numeric(
        df['discount_percentage'].astype(str).str.replace('%',''),
        errors='coerce'
    )
    category_discounts = df.groupby('main_category')['discount_percentage'].mean().reset_index()
    category_discounts = category_discounts.sort_values(by='discount_percentage',ascending=False).reset_index(drop=True)
    st.subheader("Average Discount by Category (%)")
    st.dataframe(category_discounts)


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
    fig_discount = px.bar(
        category_discounts,
        x='main_category',
        y='discount_percentage',
        title="Where are the best deals? (Avg Discount %)",
        labels={'discount_percentage': 'Average Discount (%)', 'main_category': 'Category'},
        color='discount_percentage',
        color_continuous_scale='Viridis'
    )

    st.plotly_chart(fig_discount, use_container_width=True)





    df['discount_percentage']=pd.to_numeric(
        df['discount_percentage'].astype(str).str.replace("%",""),
        errors='coerce'
    )




with st.expander ("View Raw Data processing and Schema"):
    col4,col5,col6 = st.columns([3,2,2])
    with col5:
        st.subheader("My Dataset Columns")
        st.write(df.columns)
        st.subheader("After dropping duplicate values")
        st.write("Duplicate rows:", df.duplicated().sum())
        st.dataframe(df['discount_percentage'])
    with col4:
        st.subheader("Data Preview")
        st.dataframe(df[['actual_price', 'discounted_price', 'savings']].head(50))
        st.subheader("Null Values")
        st.write(df.isnull().sum())





