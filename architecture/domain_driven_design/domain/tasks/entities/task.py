from dataclasses import dataclass, field
from typing import Optional

from architecture.domain_driven_design.domain.shared.entity import Entity
from architecture.domain_driven_design.domain.tasks.enums.priority import Priority
from architecture.domain_driven_design.domain.tasks.enums.task_status import TaskStatus
from architecture.domain_driven_design.domain.tasks.value_objects.deadline import Deadline


@dataclass
class Task(Entity):
    title: str
    description: str
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    def start(self) -> None:
        if self.status != TaskStatus.TODO:
            raise ValueError("Only tasks with 'TODO' status can be started")

        self.status = TaskStatus.IN_PROGRESS

    def complete(self) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Task is already completed")

        self.status = TaskStatus.DONE

    def is_overdue(self) -> bool:
        return self.due_date is not None and self.due_date.is_overdue()
