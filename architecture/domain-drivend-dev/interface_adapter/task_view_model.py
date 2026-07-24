
@dataclass(frozen=True)
class TaskViewModel:
    """ 화면(UI) 표시를 위한 작업 전용 표현 모델 """
    id: str
    title: str
    description: str
    status_display: str
    priority_display: str
    due_date_display: Optional[str]
    project_display: Optional[str]
    completion_info: Optional[str]