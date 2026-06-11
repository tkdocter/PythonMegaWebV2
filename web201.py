# First Streamlit version of the todo app — UI only, no interactivity yet.
##
# INSTALL
#     pip install streamlit
# (or in PyCharm: Python Packages -> search "streamlit" -> Install.)
#
# RUN
# Unlike a normal Python script, Streamlit apps need their own runner:
# ####    streamlit run web201.py instead from Terminal ###
# That command starts a small local server and opens the app in your
# browser at http://localhost:8501 (or 8502 if 8501 is busy).
#
# HOW STREAMLIT WORKS
# Each function call (st.title, st.write, st.checkbox, ...) adds a
# widget to the page. The ORDER OF THE CALLS = the order they appear
# on the page (top to bottom). To change layout, just reorder the calls.
#
# When the user does anything that changes state (presses Enter in an
# input, clicks a checkbox), Streamlit re-runs the WHOLE SCRIPT from
# the top with the new values. Keep that mental model in mind.
###streamlit run web201.py
import functions201
import streamlit as st
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions201.write_todos(todos)

todos = functions201.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions201.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

###deployed on streamlit https://tkdocter-pythonmegaweb1-web201-rlvicl.streamlit.app
### I think use: tkdocter/pythonmegaweb1/main/web201.py maybe??? or the above