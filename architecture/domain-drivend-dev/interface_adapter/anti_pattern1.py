

class TightlyCoupledTaskController:

    def __init__(self):
        # 구체 클래스를 직접 생성 -> 강한 결합
        self.use_case = TaskUseCase(SqliteTaskRepository())
        self.presenter = CliTaskPresenter()


    def handle_create(self, title: str, description: str):

        pass