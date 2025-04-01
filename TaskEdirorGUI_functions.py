import time



# with open("Tasks.txt", "w") as file:
#     file.write("TASKS | TIME " + "\n")


def read_tasks():
    with open("Tasks.txt", "r") as file:
        tasks = file.readlines()
    return tasks

def write_tasks(tasks):
    with open("Tasks.txt", "w") as file:
        file.writelines(tasks)
