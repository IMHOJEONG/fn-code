from dataclasses import dataclass

class ErrorCode(Enum):
    NOT_FOUND = "NOT_FOUND"
    VALIDATION_ERROR = "VALIDATION_ERROR"

    # 필요에 따라 다른 에러 코드 추가 가능 

@dataclass(frozen=True)
class Error:
    """표준화된 에러 정보는 여기서"""
    code: ErrorCode
    message: str
    details: Optional[dict[str, Any]] = None

    @classmethod
    def not_found(cls, entity: str, entity_id: str) -> Self:
        return cls(
            code=ErrorCode.NOT_FOUND,
            message=f"ID가 {entity_id}인 {entity}를 찾을 수 없음"
        )
    
    @classmethod
    def validation_error(cls, message: str) -> Self:
        return cls(
            code=ErrorCode.VALIDATION_ERROR,
            message=message
        )