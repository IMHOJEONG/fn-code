# use case interactor

from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from result import Result
from error import Error

@dataclass(frozen=True)
class CompleteTaskUseCase:
    """작업을 완료로 표시하고 이해관계자에게 알리는 유스 케이스"""
    task_repository: TaskRepository

    def execute(
            self, task_id: UUID, completion_notes: Optional[str] = None
    ) -> Result:
        # ...
        try: 
            # 입력 검증
            task = self.task_repository.get(task_id)
            task.complete(
                notes=completion_notes
            )
            self.task_repository.save(task)

            # 
            return Result.success({
                "id": str(task.id),
                "status": "completed",
                "completion_date": task.completed_at.isoformat()
            })
        
        except TaskNotFoundError:
            divmod
        except ValidationError as e:
            return Result.failure(Error.validation_error(str(e)))