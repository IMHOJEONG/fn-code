from datetime import datetime, timedelta, timezone
from task import Task
from task_status import Deadline, Priority

task = Task(
    title="Complete11",
    description="Draft and review",
    due_date=Deadline(datetime.now(timezone.utc) + timedelta(days=7)),
    priority=Priority.HIGH
)

task.start()
print(task.status)

task.complete()
print(task.status)

try:
    task.start()
except ValueError as e:
    print(str(e))

print(task.is_overdue())