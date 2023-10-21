

#  import modules
import streamlit as st
import pandas as pd
import numpy as np
import requests

#  load SKAI
exec(requests.get("http://skai.epistemology.ninja/get_skai").text)

#--------------------------------------------------------


#  logo
st.image("XX-MEDIA/RI-LOGO-sm.png")
st.header("  ")

#  write labels
#  st.title("SKAI on AWS")
st.write("Humanitarian Risk in Gaza")

where = "gaza@coord"

#  get latitude and longitude
lat = f().lookat("latitude").of(where).state()
long = f().lookat("longitude").of(where).state()


#  draw map
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [lat, long],
    columns=['lat', 'lon'])
st.map(df)


#--------------------------------------


#  predict thing
dataset= f().auth("zaq1").lookat("unknown_real").geo(where).time_series(arg_unis = 1, arg_start = "now", arg_stop = "next_week")[0]



#  simulate intervention
st.text("  ")
warming = st.slider("Worsening effects after X days: ", min_value = 0, max_value = 10, value = 2)
st.text("  ")
dataset = [x + warming for x in dataset]
st.line_chart(dataset)




