# 어떤 타입이든 될 수 있음, 타입 알 수 없거나, 다양하게 달라질 수 있는 코드
from typing import Any

def log_data(data: Any) -> None:
    print(f"Logged: {data}")

log_data('문자열')
log_data(42)
log_data({"key": "value"})