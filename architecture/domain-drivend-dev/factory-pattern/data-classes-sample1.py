from dataclasses import dataclass

# dataclass 정의는 __init__ 메서드를 자동으로 생성
# 전통적인 팩토리가 담당하던 작업 상당 부분을 대신 
# 기본값 설정, 선택적 매개변수 관리, 타입 일관성 보장
@dataclass
class Task(Entity): 
    title: str;
    description: str;
    due_date: Optional[Deadline] = None
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = field(default=TaskStatus.TODO, init=False)