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
    status: TaskStatus = field(
        default=TaskStatus.TODO,
        init=False
    )

    def mark_as_complete(self) -> None:
        self.status = TaskStatus.DONE
        self.send_completion_email()

    def send_completion_email(self) -> None:
        print(f"이메일 전송: 작업 '{self.title}' 완료")
