from dataclasses import dataclass

@dataclass(frozen=True)
class CreateTaskRequest:

    title: str
    description: str
    due_date: Optional[str] = None
    priority: Optional[str] = None

    def to_execution_params(self) -> dict:

        params = {
            "title": self.title.strip(),
            "description": self.description.strip()
        }

        if self.priority:
            params["priority"] = Priority[self.priority.upper()]

        return params