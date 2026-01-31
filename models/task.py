class Task: #creating the class for the task object
    def __init__(self, name, category, deadline, priority, status):
        self.name = name
        self.category = category
        self.deadline = deadline
        self.status = status
        self.priority = priority

    def __str__(self): # declaring how the program should print the task object
        return f'Task: {self.name}, Category: {self.category}, Deadline: {self.deadline}, Priority: {self.priority}, Status: {self.status}'