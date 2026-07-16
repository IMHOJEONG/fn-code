from dataclasses import dataclass
from task_status import Priority, Deadline
@dataclass
class Task(Entity): 
    title: str;
    description: str;
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)

    @classmethod
    def create_urgent_taks(cls, title: str, description: str,
                           due_date: Deadline):
        return cls(title, description, due_date, Priority.HIGH)

