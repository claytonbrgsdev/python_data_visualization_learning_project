import streamlit as st
import pandas as pd

#page configuration
st.set_page_config(layout='wide')

df_reviews = pd.read_csv("dataset/customer-reviews.csv")
df_top100_books = pd.read_csv("datasets/top-100-trending-books.csv")