from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from uuid import UUID
from entity import Entity
from task import Task


class UiComponent(Protocol):
    def refresh(self) -> None:
        ...

@dataclass
class ProjectWithUI(Entity):
    name: str
    ui: UiComponent
    description: str = ""
    _tasks: dict[UUID, Task] = field(default_factory=dict, init=False)

    def add_task(self, task: Task) -> None:
        self._tasks[task.id] = task
        self.ui.refresh()  # 의존성 규칙 위반
