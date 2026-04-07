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

df['discount_percentage']=pd.to_numeric(
        df['discount_percentage'].astype(str).str.replace('%',''),
        errors='coerce'
    )
df = df.dropna()
df['discount_percentage'] = pd.to_numeric(
    df['discount_percentage'].astype(str).str.replace("%", ""),
        errors='coerce'
    )
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['main_category'] = df['category'].str.split('|').str[0]

df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')


category_discounts = df.groupby('main_category')['discount_percentage'].mean().reset_index()
category_discounts = category_discounts.sort_values(by='discount_percentage',ascending=False).reset_index(drop=True)

best_product = df.nlargest(1,['rating','rating_count']).iloc[0]
worst_product = df.nsmallest(1,'rating').iloc[0]

best_deal = df[df['rating']>=4.0].nlargest(1,'discount_percentage').iloc[0]
top_customer = df['user_id'].value_counts().idxmax()
top_category = df.loc[df['user_id'] == top_customer, 'main_category'].mode()[0]







col1,col2,col3 = st.columns([3,3,3])



with col1 :



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
    st.subheader("Rating vs Discount (%) Price")
    df['main_category'] = df['category'].str.split('|').str[0]
    fig = px.scatter(
        df,
        x="rating",
        y="discount_percentage",
        size='rating_count',
        color='main_category',
        title="do higher-rated products get better discounts ?",

    )
    st.divider()

    fig.update_layout(yaxis_ticksuffix="%")
    fig.update_layout(height=600, )
    st.plotly_chart(fig, use_container_width=True)

    most_used_customer = df['user_name'].value_counts()



with col2 :

        avg_disc = df['discount_percentage'].mean()
        st.metric('Top Rated Product', best_product['product_name'] + '...', f"Rating:{best_product['rating']}")
        st.caption(best_product['product_name'])

        st.metric(
            label=" Average Product Discount",
            value=f"{avg_disc:.1f}%",
            delta="High Savings"
        )
        top_cat = df.groupby('main_category')['rating'].mean().idxmax()
        st.metric(
            label=" Top Selling Category",
            value=top_cat,
            delta="Customer Choice"
        )
        st.metric(
            label=" Total Products",
            value=f"{len(df):,}",
            delta="Total SKUs"
        )


        st.divider()

















with col3:
    cat_dist=df['main_category'].value_counts().reset_index()
    cat_dist.columns=['category','count']
    cat_dist = cat_dist.sort_values(by='count',ascending=True)
    fig_cat_dist = px.bar(
        cat_dist,
        x='count',
        y='category',
        orientation='h',
        title="Product Distribution by Category"
    )
    fig_cat_dist.update_layout(
        height = 510,


    )

    st.plotly_chart(fig_cat_dist, use_container_width=True)
    fig_discount = px.bar(
        category_discounts,
        x='main_category',
        y='discount_percentage',
        title="Where are the best deals? (Avg Discount %)",
        labels={'discount_percentage': 'Average Discount (%)', 'main_category': 'Category'},
        color='discount_percentage',
        color_continuous_scale='Viridis'
    )
    st.divider()

    st.plotly_chart(fig_discount, use_container_width=True)

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

    with col6:
        st.subheader("Average Discount by Category (%)")
        st.dataframe(category_discounts)
        st.write(most_used_customer)





