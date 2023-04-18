# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:39:47 2023

@author: ARNOLD
"""

#import necessary libraries
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#build page

st.header("This is Day 5; learning how to use the write function")

#example uno
st.write("Hi, this is how you write using st. Pretty cool eyyy.. :sunglasses:")

#example dos
df=pd.DataFrame({
    "Column one" : [1,2,3,4],
    "Column two" : [5,6,7,8]
    })


st.write("Below I printed the df using st.write",df)

st.dataframe(df)

st.write("Above, I used st.dataframe")

#example tree

df2 = pd.DataFrame(np.random.randn(200,3),columns=['a','b','c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c'])

st.write(c)





