import json

def get_task(task_name,tasks):
    tasks_names=[task["title"] for task in tasks]
    pos=tasks_names.index(task_name)
    return tasks.pop(pos)


class TaskManager:
    def __init__(self) -> None:
        self.tasks=[]
    def add_task(self,title,priority,status,deadline):
        new_task={
            "title":title,
            "prioriry":priority,
            "status":status,
            "deadline":deadline
        }
        self.tasks.append(new_task)
    def complete_task(self,task_name):
        task=get_task(task_name,self.tasks)
        task["status"]="complete"
        self.tasks.append(task)
    def delete_task(self,task_name):
        print("Task deleted succesfully")
        get_task(task_name,self.tasks)

    def filter_by_priority(self):
        high_tasks=[task for task in self.tasks if task["priorety"]=="high"]
        print("High priority tasks")
        for t in high_tasks:
            print(f"""
                 title: {t["name"]}
                 status:
                 deadline:
""")
        medium_tasks=[task for task in self.tasks if task["priorety"]=="medium"]
        print("medium priority tasks")
        for t in medium_tasks:
            print(f"""
                 title: {t["name"]}
                 status:
                 deadline:
""")  
        medium_tasks=[task for task in self.tasks if task["priorety"]=="low"]
        print("low priority tasks")
        for t in medium_tasks:
            print(f"""
                 title: {t["name"]}
                 status:
                 deadline:
""")    
              
            
        

