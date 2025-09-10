import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

import streamlit as st

st.header("Mouseville Simulation")

st.markdown("""
         How many shortest paths does each mouse have to get from school to
         home? We can run an experiment to try to guess the answer.

        All shortest paths are made of six left (`L`) or right (`R`) moves.
         Flipping a coin six times (once at each intersection), we go left if we 
         get heads, or right if we get tails. Each possible path is as likely as
         any other: for example, we have any equal chance of getting `LLLLLL`,
         `RRRRRR`, `LRRLRL`, or any other particular path.

        Let's do this many times and keep track of where we end up. Since each
         path is equally likely, the mouse's house we end up at the most often
         probably has the most paths leading to it.
""")

min_trials = 25
max_trials = 100000
trials = st.number_input(
    f"Enter a number between {min_trials:,} and {max_trials:,} to run the experiment that many times:",
    min_value=min_trials,
    max_value=max_trials,
    value=25,
    step=25,
)

routes = ["".join(np.random.choice(["R", "L"], size=6)) for _ in range(trials)]
results = [route.count("R") for route in routes]

df = pd.DataFrame({
    "trial": range(trials),
    "route": routes,
    "result": results,
})

tab1, tab2 = st.tabs(["Plot", "Data"])

with tab1:
    fig = px.histogram(
        df, x="result", title=f"Simulation with {trials:,} Trials", text_auto=True,
    )
    st.plotly_chart(fig)

with tab2:
    st.dataframe(df, hide_index=True)

st.markdown("[View Source Code on GitHub](https://github.com/NatalieWeaver/mouseville-explorer)")
