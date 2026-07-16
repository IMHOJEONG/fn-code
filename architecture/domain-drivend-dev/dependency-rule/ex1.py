from dataclasses import dataclass, field
from task_status import Priority, Deadline, TaskStatus

@dataclass
class TaskWithDatabase:
    title: str
    description: str
    db: DbConnection # 의존성 규칙을 위반하는 코드
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    def mark_as_complete(self):
        self.status = TaskStatus.DONE
        self.db.update(self) # 의존성 규칙 위반