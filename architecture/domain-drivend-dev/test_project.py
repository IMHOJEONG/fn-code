from project import Project
from task import Task
from task_status import Deadline, Priority
from datetime import datetime, timezone


project = Project("Website RERERE")

task1 = Task(
    title="Design homepage",
    description="create new homepage layout",
    due_date=Deadline(datetime(2027, 12, 31, tzinfo=timezone.utc)),
    priority=Priority.HIGH
)

task2 = Task(
    title="Implement login",
    description="Add user auth",
    due_date=Deadline(datetime(2027, 11, 30, tzinfo=timezone.utc)),
    priority=Priority.MEDIUM
)

project.add_task(task1)
project.add_task(task2)

print(f"프로젝트: {project.name}")
print(f"작업 수: {len(project.tasks)}")
print(f"첫 번째 작업: {project.tasks[0].title}")