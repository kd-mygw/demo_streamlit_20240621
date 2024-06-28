import streamlit as st
st.write("Hello world!!")

#import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)


#import streamlit as st

st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')


#import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')


#import streamlit as st

st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')


#import streamlit as st

st.text('This is some text.')


#import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")


#import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)


#import streamlit as st
#import pandas as pd
#import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))


st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')


#import streamlit as st

#st.page_link("your_app.py", label="Home", icon="🏠")
#st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
#st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")


#import streamlit as st

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)