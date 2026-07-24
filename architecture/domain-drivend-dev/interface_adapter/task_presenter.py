from abc import ABC, abstractmethod

class TaskPresenter(ABC):
    """작업 관련 출력을 담당하는 추상 프레젠터"""

    @abstractmethod
    def present_task(
        self, 
        task_response: TaskResponse
    ) -> TaskViewModel:
        """
            작업 응답을 뷰 모델로 변환
        """
        pass

    @abstractmethod
    def present_error(
        self,
        error_msg: str, 
        code: Optional[str] = None
    ) -> ErrorViewModel:

        """
            화면 표시를 위한 오류 메시지 형식화
        """
        pass