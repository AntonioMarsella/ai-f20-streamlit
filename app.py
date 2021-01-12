import streamlit as st
from PIL import Image # Required to show images
import pandas as pd
logo = Image.open("logo.png")
st.sidebar.image(logo, width=100)
# Text/Title
st.title("This is a title")

st.sidebar.header("Sidebar")
st.sidebar.text("Writing on the sidebar!")
st.sidebar.markdown("""This is a template for [Streamlit](https://www.streamlit.io/) to publish some results from your first AI Build Week!
I wrote some examples of things you could do using Streamlit. Go at the end of the document to look for more resources to learn from!""")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

st.text("This is text")
st.markdown("""### And here I'm writing in markdown.
Hello guys, this is a template I built in Streamlit if you want to deploy a web app with what you have done so far.

I personally think it is pretty cool and straighforward!
I will leave here some of the commands that you could try and some of the links to make more advance stuff. 

Take a look at the code of this page to understand how things are implemented.""")

st.markdown("### Display stuff with `st.write(python_code)`")
hello_world_variable = "Hello World"
st.write(hello_world_variable)

st.markdown("### Create a button with `st.button('Text')`")
st.button("Click me")

st.markdown("### If statement with buttons")
if st.button("Click to show spoiler"):
    st.write("Hello :D")

st.markdown("### Success/Info/Warning/Error")

st.success("Successful!")
st.info("Information")
st.warning("Warning!")
st.error("Error!")

st.markdown("### Raise exceptions")

st.exception("AnError {This app is too cool. Cool it down.}")

st.markdown("### Load images")

img = Image.open("strive.jpeg")
st.image(img, caption="Strive Image Caption")

st.subheader("Widgets!")
# Widget 
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

status = st.radio("What is you status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are Active")
else:
    st.warning("You're Inactive")

# SelectBox
occupation = st.selectbox("Your occupation", ["Programmer", "Data Scientist", "Striver"])
st.write("You selected", occupation)

music = st.multiselect("Which music do you like?", ["Rock", "Pop", "EDM", "Electronic", "Classical", "Traditional"])
st.write("You selected", len(music), "music genres")

age = st.slider("How old are you?", 18,100)
st.write(age)

where = st.text_area("Where are you from? Write your city to display it on the map", "Type here...")
from geopy.geocoders import Nominatim
if st.button("Submit"):
    geolocator = Nominatim(user_agent="a")
    location = geolocator.geocode(where)
    lat = location.latitude
    lon = location.longitude
    map_df = pd.DataFrame.from_dict({"lat":[lat], "lon":[lon]})
    st.map(map_df)

import datetime
today = st.date_input("Today is", datetime.datetime.now())

st.text("Display JSON")
st.json({"Strive":{"Professor": {"name": "Jan", "subject":"being-great!"}, "TA":{"name":"Antonio", "subject":"being-awesome!"} }})

# Display Row Code

st.text("Display Raw Code")
st.code("import numpy as np")

with st.echo():
    import pandas as pd
    df = pd.DataFrame()

import time
st.text("Loading bar and spinner")
my_bar = st.progress(0)
if st.button("Progress bar"):
    with st.spinner("Waiting .."):
        
        for p in range(0,120,20):
            time.sleep(0.5)
            my_bar = my_bar.progress(p)
    st.success("Finished")


# st.balloons()

st.header("Pandas and Visualization")

st.markdown("""The great thing about Streamlit is that you can work in Python as you normally do, and then you can add an "interactive layer" to it!

If you look at the code down here, the dataset is loaded using pandas as you're used to.
In this example, we will use a csv file created scraping from IMDb last time.""")

import pandas as pd

df = pd.read_csv("example.csv")
if st.button("Show me the data."):
    st.dataframe(df)

st.markdown("If you want to display only few columns, you can do like the following:")

columns_to_show = st.multiselect("Select the columns you want to display", df.columns)
st.markdown("Filter out the movies under a threshold of ratings:")
threshold = st.slider("Filter movies for less than", 2, 10)
filtered = df[df["rating"] >= threshold]
st.dataframe(filtered[columns_to_show])



st.subheader("Visualization with Plotly")
import plotly.express as px
fig1 = px.bar(df, x = 'director', y = 'profit($ Mil)',title = 'Production House profits')

st.plotly_chart(fig1)

st.header("Conclusions")
st.markdown("""Here you have seen a couple of things you can do using Streamlit.

I found the process pretty smooth myself, very intuitive once you know a bit of Python.

I want to stress a bit the importance of visualizing things: you're going to deal with people, and if you can show 
stuff, people can trust you faster... and give you a job.

So I recommend you to take care of building a nice portfolio, to share it on the internet, so that you can be exposed to people that
are seeking smart guys and gals like you to be hired!
""")
st.header("More resources")

st.markdown("""Following a bunch of links to reduce your *Google fatigue*:

- Streamlit crash course (*not* covering pandas and plotting) https://www.youtube.com/watch?v=_9WiB2PDO7k
- Streamlit Tutorials Playlist from [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q) https://www.youtube.com/watch?v=ZZ4B0QUHuNc
- Streamlit official documentation https://docs.streamlit.io/
- Streamlit cheat sheet https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
- How to deploy your Streamlit web-app with Heroku https://towardsdatascience.com/from-streamlit-to-heroku-62a655b7319
 """)