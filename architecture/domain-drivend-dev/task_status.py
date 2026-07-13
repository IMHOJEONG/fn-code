from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# frozen=True -> 불변 설정 / 값 객체를 위함
@dataclass(frozen=True)
class Deadline:
    due_date: datetime

    def __post_init__(self):
        if self.due_date < datetime.now(timezone.utc):
            raise ValueError("Deadline cannot be in the past~~~")
        
    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) > self.due_date
    
    def time_remaining(self) -> timedelta:
        return max(
            timedelta(0),
            self.due_date - datetime.now(timezone.utc)
        )
    
    def is_approaching(
        self, warning_threshold: timedelta = timedelta(days=1)
    ) -> bool:
        return timedelta(0) < self.time_remaining() <= warning_threshold