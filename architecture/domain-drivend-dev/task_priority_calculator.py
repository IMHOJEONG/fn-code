from task import Task
from task_status import Priority
from datetime import timedelta

class TaskPriorityCalculator:
    @staticmethod
    def calculate_priority(task: Task) -> Priority:
        if task.is_overdue():
            return Priority.HIGH
        
        elif (
            task.due_date and task.due_date.time_remaining() 
            <= timedelta(days=2)
        ):
            return Priority.MEDIUM

        else:
            return Priority.LOW
        

