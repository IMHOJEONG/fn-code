from datetime import timedelta

from architecture.domain_driven_design.domain.tasks.entities.task import Task
from architecture.domain_driven_design.domain.tasks.enums.priority import Priority


class TaskPriorityCalculator:
    @staticmethod
    def calculate_priority(task: Task) -> Priority:
        if task.is_overdue():
            return Priority.HIGH

        if task.due_date and task.due_date.time_remaining() <= timedelta(days=2):
            return Priority.MEDIUM

        return Priority.LOW
