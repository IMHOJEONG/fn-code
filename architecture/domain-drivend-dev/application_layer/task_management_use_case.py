from dataclasses import dataclass, field
from notification_port import NotificationPort
from task_repository import TaskRepository
from typing import Any

@dataclass(frozen=True)
class TaskManagementUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort
    _optional_services: dict[str, Any] = field(
        default_factory=dict
    )

    def register_service(self, name: str, service: Any) -> None:
        """ 선택적 서비스를 등록 """
        self._optional_services[name] = service

    def complete_task(self, task_id: UUID) -> Result:
        try: 

            task = self.task_repository.get(task_id)
            task.complete()
            self.task_repository.save(task)

            # 필수 알림 처리
            self.notification_service.notify_task_completed(task)

            # 선택적 연동 서비스 처리
            if analytics := self._optional_services.get("analytics"):
                analytics.track_task_completion(task.id)
            if audit := self._optional_services.get("audit"):
                audit.log_task_completion(task.id)

            return Result.success(TaskResponse.from_entity(task))

        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))