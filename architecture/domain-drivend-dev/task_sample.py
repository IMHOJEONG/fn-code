from task import Task
from task_status import Priority

# 새로운 작업 생성
task = Task(
    title="Complete",
    description="Draft and review the proposal for",
    priority=Priority.HIGH
);

print(f"{task.title}, {task.priority}, {task.status}")