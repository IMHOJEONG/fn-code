
from todo_app.domain.entities.task import Task 
from todo_app.domain.repositories.task_repository import TaskRepository

class SQLiteTaskRepository(TaskRepository):
    def __init__(self, db_connection):
        self.db = db_connection

    def save(self, task: Task):
        # 구현 세부 사항...
        pass 

    def get(self, task_id: str) -> Task:
        # 구현 세부 사항
        pass 