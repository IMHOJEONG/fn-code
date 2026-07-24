from dataclasses import dataclass
from error import Error
@dataclass(frozen=True)
class Result:
    """유스 케이스 실행의 성공 또는 실패를 나타냄"""
    value: Any = None
    error: Optional[Error] = None
    
    @property
    def is_success(self) -> bool:
        return self.error is None
    
    @classmethod
    def success(cls, value: Any) -> Self:
        return cls(value=value)

    @classmethod
    def failure(cls, error: Error) -> Self:
        return cls(error=error)