from datetime import datetime, timedelta, timezone

from architecture.domain_driven_design.domain.tasks.entities.task import Task
from architecture.domain_driven_design.domain.tasks.enums.priority import Priority
from architecture.domain_driven_design.domain.tasks.value_objects.deadline import Deadline


task = Task(
    title="Complete project",
    description="Draft and review deliverables",
    due_date=Deadline(datetime.now(timezone.utc) + timedelta(days=7)),
    priority=Priority.HIGH,
)

task.start()
print(task.status)

task.complete()
print(task.status)

try:
    task.start()
except ValueError as error:
    print(str(error))

print(task.is_overdue())
