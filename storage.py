import os
import json

class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.save([])

    def load(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump(tasks, file, indent=2)