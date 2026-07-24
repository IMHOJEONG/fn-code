from abc import ABC, abstractmethod
from uuid import UUID

class TaskRepository(ABC):
    """애플리케이션 계층에서 정의한 리포지터리 인터페이스"""
    @abstractmethod
    def get(self, task_id: UUID) -> Task:
        """ID로 작업을 조회"""
        pass

    @abstractmethod
    def save(self, task: Task) -> None:
        """작업을 리포지터리에 저장"""
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        """리포지터리에서 작업을 삭제"""
        pass

class NotificationService(ABC):
    """알림 전송을 위한 서비스 인터페이스"""
    @abstractmethod
    def notify_task_assigned(self, task_id: UUID) -> None:
        """작업이 할당됐을 때 알림"""
        pass

    @abstractmethod
    def notify_task_completed(self, task: Task) -> None:
        """작업이 완료됐을 때 알림"""
        pass

class MongoDbTaskRepository(TaskRepository):
    """TaskRepository 인터페이스의 MongoDB 구현체"""
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = client.task_management
        self.tasks = self.db.tasks

    def get(self, task_id: UUID) -> Task:
        """ID로 작업을 조회"""
        document = self.tasks.find_one({
            "_id": str(task_id)
        })

        if not document:
            raise TaskNotFoundError(task_id)
        # 나머지 메시드 구현

    # 다른 인터페이스 메서드 구현
    