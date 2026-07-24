

class WebTaskController:

    def __init__(self, app: FastAPI):
        self.app = app;
        # 유스 케이스를 직접 생성하여 강한 결합 발생
        self.use_case = CreateTaskUseCase()

    async def handle_create(self, request: Request):

        try:
            data = await request.json()
            # 컨트롤러가 fastAPi에 의존
            return JSONResponse(status_code=201, content={"task": result})

        except ValidationError as e:
            raise HTTPException(status_code=400, detail=str(e))
