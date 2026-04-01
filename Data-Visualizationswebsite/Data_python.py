import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('amazon.csv')
st.subheader("Data Preview")
st.dataframe(df[['actual_price','discounted_price']].head(50))


