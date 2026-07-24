from task_presenter import TaskPresenter

class CliTaskPresenter(TaskPresenter):
    """ CLI 환경 특화 작업 프레젠터 """

    def present_task(
        self, 
        task_response: TaskResponse
    ) -> TaskViewModel:

        return TaskViewModel(
            id=str(task_response.id),
            title=task_response.title,
            description=task_response.description,
            status_display=self._format_status(task_response.status),
            priority_display=self._format_priority(
                task_response.priority
            ),
            due_date_display=self._format_due_date(
                task_response.due_date
            ),
            project_display=self._format_project(
                task_response.project_id
            ),
            completion_info=self._format_completion_info(
                task_response.completion_date,
                task_response.completion_notes,
            )
        )

    def _format_due_date(self, due_date: Optional[datetime]) -> str:
        """ 마감일 포맷, 기한 초과 여부 표시 """
        if not due_date:
            return "No due date"

        is_overdue = due_date < datetime.now(timezone.utc)
        date_str = due_date.strftime("%Y-%m-%d")
        return (
            f"OVERDUE - DUE: {date_str}"
            if is_overdue else f"Due: {date_str}"
        )

    def present_error(self, error_msg: str, code: Optional[str] = None) -> ErrorViewModel:
        return ErrorViewModel(message=error_msg, code=code)