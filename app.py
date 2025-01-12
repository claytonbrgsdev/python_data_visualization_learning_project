import streamlit as st
import pandas as pd
import plotly.express as px

#page layout configuration
st.set_page_config(layout='wide')

#csv variables
df_reviews = pd.read_csv("dataset/customer-reviews.csv")
df_top_100_books = pd.read_csv("dataset/top-100-trending-books.csv")

#price range - slider
price_max = df_top_100_books["book price"].max()
price_min = df_top_100_books["book price"].min()

max_price = st.sidebar.slider("Price range", price_min, price_max, price_max)

df_top_100_books_price_range_filter = df_top_100_books[df_top_100_books["book price"] <= max_price]


#plotly
df_year_publication = df_top_100_books_price_range_filter['year of publication'].value_counts()
df_book_price = df_top_100_books_price_range_filter['book price']
df_n_books_by_authors = df_top_100_books_price_range_filter['author'].value_counts()

fig = px.bar(df_year_publication)
fig2 = px.histogram(df_book_price)
fig3 = px.area(df_n_books_by_authors)

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)
st.plotly_chart(fig3)
df_top_100_books_price_range_filter