# after refactoring
from abc import ABC, abstractmethod
from dataclasses import dataclass
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
        # 이메일 전송 X - 이 책임은 외부 계층에 있음 

class TaskCompleteNotifier(ABC):
    @abstractmethod
    def notify_completion(self, task):
        pass

# 이 클래스 - 외부 계층에서 구현됨
class EmailTaskCompleteNotifier(TaskCompleteNotifier):
    def notify_completion(self, task):
        printf(f"이메일 전송: 작업 '{task.title}' 완료")