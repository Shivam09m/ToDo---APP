import streamlit as st
import function

todos = function.get_todos()

st.title("My To-Do App")
st.subheader("Place all your daily tasks here!!!")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To-Do", placeholder="add to-do")