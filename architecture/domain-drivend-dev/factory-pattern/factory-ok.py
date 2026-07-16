# 언제 기존 팩토리가 적합한가?
from pathlib import Path
import sys
from typing import Protocol
from uuid import UUID

sys.path.append(str(Path(__file__).resolve().parents[1]))

from task import Task
from task_status import Priority


class User(Protocol):
    def is_manager(self) -> bool:
        ...


class UserService(Protocol):
    def get_user(self, assignee_id: UUID) -> User:
        ...


class Project(Protocol):
    def is_high_priority(self) -> bool:
        ...

    def add_task(self, task: Task) -> None:
        ...


class ProjectRepository(Protocol):
    def get_by_id(self, project_id: UUID) -> Project:
        ...


class TaskFactory:
    def __init__(
        self,
        user_service: UserService,
        project_repository: ProjectRepository,
    ) -> None:
        self.user_service = user_service
        self.project_repository = project_repository

    def create_task_in_project(
        self,
        title: str,
        description: str,
        project_id: UUID,
        assignee_id: UUID,
    ) -> Task:
        project = self.project_repository.get_by_id(project_id)
        assignee = self.user_service.get_user(assignee_id)

        task = Task(title, description)
        task.project = project
        task.assignee = assignee

        if project.is_high_priority() and assignee.is_manager():
            task.priority = Priority.HIGH

        project.add_task(task)
        return task
