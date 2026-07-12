

from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level: LogLevel) -> None:
    print(f"Setting log level to {level}")

set_log_level("DEBUG")
set_log_level("CRITICAL")