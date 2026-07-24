from dataclasses import dataclass

@dataclass(frozen=True)
class CompleteProjectRequest:
    """프로젝트 완료 요청을 위한 데이터 구조임~~~"""
    project_id: str # API -> UUID?
    completion_notes: Optional[str] = None

    def __post_init__(self) -> None:
        """요청 데이터 검증"""
        if not self.project_id.strip():
            raise ValidationError("프로젝트 ID는 필수")
        
        if self.completion_notes and len(self.completion_notes) > 1000:
            raise ValidationError(
                "완료 메모 1000자 초과 불가능"
            )
        
    def to_execution_params(self) -> dict:
        """검증된 요청 데이터를 유스케이스 매개변수로 변환"""
        return {
            "project_id": UUID(self.project_id),
            "completion_notes": self.completion_notes
        }