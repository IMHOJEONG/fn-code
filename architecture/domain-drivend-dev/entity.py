from dataclasses import dataclass, field
from uuid import UUID, uuid4

# Entity 기본 클래스 
# 모든 엔터티의 토대, 고유 식별자 부여, 동등성 비교 및 해싱이 올바르게 동작
@dataclass
class Entity:
    # id 필드에 고유한 UUID를 자동으로 생성 
    # __init__ 메서드에서는 제외됨
    id: UUID = field(default_factory=uuid4, init=False)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
