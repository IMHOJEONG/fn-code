from architecture.domain_driven_design.domain.tasks.entities.task import Task
from architecture.domain_driven_design.domain.tasks.enums.task_status import TaskStatus


task = Task("Complete project", "The important project")

# This is possible at runtime, but it breaks the domain type contract.
task.status = "Finished"
print(task.status == "done")

task = Task("Complete project", "The important project")
task.status = TaskStatus.DONE
print(task.status == TaskStatus.DONE)
