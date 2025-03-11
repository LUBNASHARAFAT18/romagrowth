import streamlit as st
import pandas as pd
import numpy as np

# Set page title and description
st.set_page_config(page_title="Growth Mindset App", page_icon="\U0001F680", layout="wide")

# Title and Introduction
st.title("Embracing a Growth Mindset")
st.write("This app helps you track and cultivate a growth mindset by setting learning goals, reflecting on progress, and staying motivated.")

# Sidebar for user input
st.sidebar.header("Your Growth Mindset Plan")

goal = st.sidebar.text_input("Set Your Learning Goal:", "Learn a new programming language")
progress = st.sidebar.slider("Track Your Progress:", 0, 100, 50)
reflection = st.sidebar.text_area("Reflection on Learning:", "What have you learned so far?")

# Display user inputs
st.subheader("Your Personalized Growth Journey")
st.write(f"**Learning Goal:** {goal}")
st.progress(progress / 100)
st.write(f"**Reflection:** {reflection}")

# Generate motivational message
messages = [
    "Keep pushing forward! Growth comes with effort.",
    "Mistakes are proof that you are trying!", 
    "Stay positive and keep learning.",
    "Small progress is still progress!"
]

if st.button("Get Motivation"):
    st.success(np.random.choice(messages))

# Data visualization example
data = pd.DataFrame({
    'Days': list(range(1, 11)),
    'Effort': np.random.randint(50, 100, 10)
})

st.subheader("Your Learning Effort Over Time")
st.line_chart(data.set_index('Days'))

# Conclusion
st.write("**Remember, growth is a continuous journey. Keep learning and stay persistent!**")
