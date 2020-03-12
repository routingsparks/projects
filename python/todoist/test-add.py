from todoist.api import TodoistAPI

api = TodoistAPI('c420b289cf0cdc6f84dbbbd98bef00b62fc3aff6')
api.sync()
#print (api.state['projects'])

# What do you want to do?
# Menu to create project, update project, add task to project, change color, etc


def add_project():
    project1 = api.projects.add('Project1')
    api.commit()
    print (project1)

def add_task():
    project1 = api.projects.add('Project1')
    task1 = api.items.add('Task1', project_id=project1['id'])
    task2 = api.items.add('Task2', project_id=project1['id'])
    api.commit()
    print(task1, task2)

def modify_task():
    project1 = api.projects.get_by_id(2230297078)
    task1 = api.items.update(content='NewTask1', due={'string': 'tomorrow at 10:00'}, project_id=project1['id'], item_id=(3723463411))
    api.commit()

