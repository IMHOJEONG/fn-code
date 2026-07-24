from dataclasses import dataclass
from typing import Optional
from complete_project_request import CompleteProjectRequest
from complete_project_response import CompleteProjectResponse
from project import Project
@dataclass
class CompleteProjectUseCase:
    project_repository: ProjectRepository
    task_repository: TaskRepository
    notification_service: NotificationService

    def execute(
            self,
            ## 2
            # project_id: UUID,
            # completion_notes: Optional[str] = None

            ## 1
            request: CompleteProjectRequest
    ) -> Result:
        # 3333

        try:


            ## 1
            params = request.to_execution_params()
            project = self.project_repository.get(params["project_id"])
            project.mark_completed(
                notes=params["completion_notes"]
            )
            self.project_repository.save(project)
            response = CompleteProjectResponse.from_entity(project)
            return Result.success(response)




            ## 2
            # 프로젝트 존재 여부 검증
            project = self.project_repository.get(project_id)

            # 미완료된 모든 작업 완료 처리
            for task in project.incomplete_tasks:
                task.complete()
                self.task_repository.save(task)
                self.notification_service.notify_task_completed(task)

            # 프로젝트 자체를 완료 처리
            project.mark_completed(
                notes=completion_notes
            )
            self.project_repository.save(project)

            return Result.success({
                "id": str(project.id),
                "status": project.status,
                "completion_date": project.completed_at,
                "task_count": len(project.tasks),
                "completion_notes": project.completion_notes,
            })

        except ProjectNotFoundError:
            return Result.failure(Error.not_found(
                "Project", str(project_id)
            ))
    
        except ValidationError as e:
            return Result.failure(
                Error.validation_error(str(e))
            )
        