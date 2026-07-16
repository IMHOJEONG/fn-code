from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str
    is_completed: bool = False

    def complete(self) -> None:
        self.is_completed = True
