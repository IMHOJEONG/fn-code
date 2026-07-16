# after refactoring
from abc import ABC, abstractmethod
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
        # 이메일 전송 X - 이 책임은 외부 계층에 있음 

class TaskCompleteNotifier(ABC):
    @abstractmethod
    def notify_completion(self, task: Task) -> None:
        pass

# 이 클래스 - 외부 계층에서 구현됨
class EmailTaskCompleteNotifier(TaskCompleteNotifier):
    def notify_completion(self, task: Task) -> None:
        print(f"이메일 전송: 작업 '{task.title}' 완료")
