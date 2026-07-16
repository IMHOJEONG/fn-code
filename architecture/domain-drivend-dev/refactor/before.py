from dataclasses import dataclass, field
from typing import Optional

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

    def mark_as_complete(self):
        self.status = TaskStatus.DONE
        self.send_completion_email()

    def send_completion_email(self):
        print(f"이메일 전송: 작업 '{self.title}' 완료")