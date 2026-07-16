from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Protocol
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from task_status import Deadline, Priority, TaskStatus


class DbConnection(Protocol):
    def update(self, task: "TaskWithDatabase") -> None:
        ...

@dataclass
class TaskWithDatabase:
    title: str
    description: str
    db: DbConnection  # 의존성 규칙을 위반하는 코드
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    def mark_as_complete(self) -> None:
        self.status = TaskStatus.DONE
        self.db.update(self)  # 의존성 규칙 위반
