# Domain-Driven Design Task Example

`architecture/domain-drivend-dev` 아래의 예제를 DDD에 맞는 패키지 구조로 다시 정리한 복사본이다.

## 구조

- `domain/shared`: 여러 도메인에서 재사용 가능한 공통 개념
- `domain/tasks`: Task 도메인 모델
- `examples`: 도메인 모델 사용 예제

## 디렉터리 예시

```text
architecture/domain_driven_design
├── domain
│   ├── shared
│   │   └── entity.py
│   └── tasks
│       ├── entities
│       │   └── task.py
│       ├── enums
│       │   ├── priority.py
│       │   └── task_status.py
│       ├── services
│       │   └── task_priority_calculator.py
│       └── value_objects
│           └── deadline.py
└── examples
    ├── create_task.py
    ├── task_lifecycle.py
    └── task_status_type_safety.py
```

## 실행 예시

프로젝트 루트에서 아래처럼 모듈 실행 형태로 돌리면 import 경로가 안정적으로 동작한다.

```bash
python -m architecture.domain_driven_design.examples.create_task
python -m architecture.domain_driven_design.examples.task_lifecycle
python -m architecture.domain_driven_design.examples.task_status_type_safety
```
