from dataclasses import dataclass

@dataclass
class OperationResult(Generic[T]):

    """
        성공 값 또는 오류를 담는 작업 결과 객체

        Either 패턴 구현 - 성공과 실패 중 하나만 존재
        - 명시적 오류 처리와 None 검사를 대체
        - Mypy 등 정적 타입 검사도 지원
    """

    _success: Optional[T] = None
    _error: Optional[ErrorViewModel] = None

    @property
    def is_success(self) -> bool:
        """작업 성공 여부 반환"""
        return self._success is not None

    @property
    def success(self) -> T:
        """성공 값을 반환. 오류 결과에서 접근 시 ValueError 발생"""
        if self._success is None:
            raise ValueError(
                "Cannot Access success value on error result",
                "~~~"
            )
        return self._success

    @property
    def error(self) -> ErrorViewModel:
        """오류 정보를 반환. 성공 결과에서는 접근할 떄는 ValueError 발생"""
        if self._error is None:
            raise ValueError(
                "Cannot access error value on success result"
            )
        return self._error

    @classmethod
    def succeed(cls, value: T) -> "OperationResult[T]":
        """주어진 값으로 성공한 결과를 생성"""
        return cls(_success=value)

    @classmethod
    def fail(cls, message: str, code: Optional[str] = None) -> "OperationResult[T]":
        """오류 메시지와 선택적 코드로 실패한 결과를 생성"""
        return cls(error=ErrorViewModel(message, code))
