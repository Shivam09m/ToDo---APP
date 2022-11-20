import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    todo_new = st.session_state["new_todo"] + "\n"
    todos.append(todo_new)
    function.write_todos(todos)


st.title("My To-Do App")
st.subheader("Place all your daily tasks here!!!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a To-Do", placeholder="add to-do",
              on_change=add_todo, key='new_todo')