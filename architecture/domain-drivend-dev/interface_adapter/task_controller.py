from dataclasses import dataclass
from create_task_request import CreateTaskRequest
from operation_result import OperationResult


@dataclass
class TaskController:
    create_use_case: CreateTaskUseCase # 애플리케이션 계층 인터페이스

    # 필요에 따라 추가 유스 케이스 정의
    presenter: TaskPresenter # interface 게층 추상화

    def handle_create(
        self, title: str, description: str
    ) -> OperationResult[TaskViewModel]:

        try:
            # 요청 모델에 대한 외부 입력
            request = CreateTaskRequest(
                title=title, description=description
            )

            # 요청 모델을 도메인 실행 작업으로 전달
            result = self.create_use_case.execute(request)

            if result.is_success:
                # 도메인 실행 결과를 뷰 모델로 변환
                view_model = self.presenter.present_task(result.value)
                return OperationResult.succeed(view_model)

            # 오류 처리 및 형식화
            error_vm = self.presenter.present_error(
                result.error.message,
                str(result.error.code.name)
            )

            return OperationResult.fail(error_vm.message, error_vm.code)
        

        except ValueError as e:
            # 입력 검증 오류 처리
            error_vm = self.presenter.present_error(
                str(e), "VALIDATION_ERROR"
            )
            return OperationResult.fail(error_vm.message, error_vm.code)