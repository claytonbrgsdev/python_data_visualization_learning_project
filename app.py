import streamlit as st
import pandas as pd

#page configuration
st.set_page_config(layout='wide')

#csv variables
df_reviews = pd.read_csv("dataset/customer-reviews.csv")
df_top_100_books = pd.read_csv("dataset/top-100-trending-books.csv")

#price range - slider
price_max = df_top_100_books["book price"].max()
price_min = df_top_100_books["book price"].min()

max_price = st.sidebar.slider("Price range", price_min, price_max, price_max)

df_top_100_books_price_range_filter = df_top_100_books[df_top_100_books["book price"] <= max_price]

df_top_100_books_price_range_filter
