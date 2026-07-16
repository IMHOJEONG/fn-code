from dataclasses import dataclass, field, 
from uuid import UUID
from task import Task

@dataclass
class ProjectWithUI(Entity):
    name: str
    ui: UiComponent
    description: str = ""
    _tasks: dict[UUID, Task] = field(default_factory=dict, init=False)

    def add_task(self, task: Task):
        self._tasks[task.id] = task
        self.ui.refresh() # 의존성 규칙 위반
