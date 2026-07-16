from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from entity import Entity
from task_status import Deadline, Priority, TaskStatus


@dataclass
class Task(Entity):
    title: str
    description: str
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    @classmethod
    def create_urgent_taks(
        cls,
        title: str,
        description: str,
        due_date: Deadline,
    ) -> "Task":
        return cls(title, description, due_date, Priority.HIGH)
