from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class CompleteProjectResponse:
    """프로젝트 완료 응답을 위한 데이터 구조"""
    id: str
    status: str
    completion_date: str
    task_count: int
    completion_notes: Optional[str]

    @classmethod
    def from_entity(cls, project: Project) -> Self:
        """프로젝트 엔터티로부터 응답 객체 생성"""
        return cls(
            id=str(project_id),
            status=project.status,
            completion_date=project.completed_at,
            task_count=len(project.tasks),
            completion_notes=project.completion_notes
        )
