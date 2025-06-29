import json
from storage import Storage

class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save(self.tasks)

    def get_tasks(self):
        return self.tasks

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.storage.save(self.tasks)
            return True
        return False