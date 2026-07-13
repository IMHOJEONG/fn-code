from dataclasses import dataclass, field
from typing import Optional
from entity import Entity
from task_status import TaskStatus, Deadline, Priority

@dataclass
class Task(Entity):
    title: str
    description: str
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    # 
    def start(self) -> None:
        if self.status != TaskStatus.TODO:
            raise ValueError(
                "Only tasks with 'TODO' status can be started"
            )
    
        self.status = TaskStatus.IN_PROGRESS

    def complete(self) -> None:
        if self.status == TaskStatus.DONE:
            raise ValueError("Tasks is already completed!@#!@#")
        
        self.status = TaskStatus.DONE
    
    def is_overdue(self) -> bool:
        return self.due_date is not None and self.due_date.is_overdue()
