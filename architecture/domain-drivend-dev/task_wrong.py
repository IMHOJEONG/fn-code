from task import Task
from task_status import TaskStatus

task = Task(
    "Complete project",
    "The important project"
)

# 허용되지만, 유효 X
task.status = "Finished"

# False, 대소문자 구분
print(task.status == "done")

# ----
task = Task("Complete Project", "The important Project")
task.status = TaskStatus.DONE # 타입 안전
print(task.status == TaskStatus.DONE)

