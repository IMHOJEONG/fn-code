from abc import ABC, abstractmethod

# Port: 애플리케이션 계층이 필요로 하는 기능 정의
class NotificationPort(ABC):

    @abstractmethod
    def notify_task_completed(self, task: Task) -> None:
        """작업이 완료됐을 때 알림"""
        pass 

    # 필요에 따라 추가 기능 확장