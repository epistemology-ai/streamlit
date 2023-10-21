

#  import modules
import streamlit as st
import pandas as pd
import numpy as np
import requests

#  load SKAI
exec(requests.get("http://skai.epistemology.ninja/get_skai").text)

#  write labels
#  st.title("SKAI on AWS")
st.header("Temperature in Sydney")

#  get latitude and longitude
lat = f().lookat("latitude").of("sydney@coord").state()
long = f().lookat("longitude").of("sydney@coord").state()

#  predict temperature
dataset= f().auth("demo").lookat("temperature").of("gaza@coord").time_series(arg_unis = 1, arg_start = "now", arg_stop = "next_week")[0]

#  simulate global warming
st.text("  ")
warming = st.slider("Simulate additional warming of: ", min_value = -5, max_value = 10, value = 2)
st.text("  ")
dataset = [x + warming for x in dataset]
st.line_chart(dataset)


#  draw map
st.header("Map of Sydney")
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [lat, long],
    columns=['lat', 'lon'])
st.map(df)

