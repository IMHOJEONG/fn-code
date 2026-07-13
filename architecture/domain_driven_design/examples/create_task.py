from architecture.domain_driven_design.domain.tasks.entities.task import Task
from architecture.domain_driven_design.domain.tasks.enums.priority import Priority


task = Task(
    title="Complete proposal",
    description="Draft and review the proposal document",
    priority=Priority.HIGH,
)

print(f"{task.title}, {task.priority}, {task.status}")
