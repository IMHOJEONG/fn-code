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

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("비어 있는 작업 제목 사용 불가능")
        if len(self.description) > 500:
            raise ValueError("작업 설명 500자 초과 불가")
