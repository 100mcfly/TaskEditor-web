import streamlit as st
import TaskEdirorGUI_functions

tasks = TaskEdirorGUI_functions.read_tasks()

def add_task():
    new_task = st.session_state["new_task"]
    new_task = new_task.title() + "\n"
    tasks.append(new_task)
    TaskEdirorGUI_functions.write_tasks(tasks)


st.title("Task Editor")
st.subheader("Add, Edit and Delete Tasks")
st.write("The goal is to improve <b>organization</b> and <b>productivity</b>.", unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new task", on_change=add_task, key="new_task")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        TaskEdirorGUI_functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()