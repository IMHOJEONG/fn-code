from dataclasses import dataclass
from task_repository import TaskRepository
from notification_port import NotificationPort
@dataclass
class SetTaskPriorityUseCase:
    task_repository: TaskRepository
    notification_service: NotificationPort # 기능을 정의한 인터페이스에 의존

    def execute(
            self, request: SetTaskPriorityRequest
    ) -> Result:
        try:
            params = request.to_execution_params()

            task = self.task_repository.get(params['task_id'])
            task.priority = params["priority"]

            self.task_repository.save(task)

            if task.priority == Priority.HIGH:
                self.notification_service.notify_task_high_priority(task)

            return Result.success(TaskResponse.from_entity(task))

        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))