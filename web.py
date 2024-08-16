import streamlit as st
import functions

def add_todo():
    """"
    call back function for widget using this function
    """
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

# view a web app
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # remove from session state
        st.rerun()


st.text_input(label="tmp", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#print("Hello")

# st.session_state looks like dictionary containing stuff entered in app, e.g., new_todo key

#st.session_state




