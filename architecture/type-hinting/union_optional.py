from typing import Union, Optional

# def process_input(data: Union[str, int]) -> str:
def process_input(data: str | int) -> str:
    return str(data)

def find_user(user_id: Optional[int] = None) -> Optional[str]:
    if user_id is None:
        return None
    
    return "User found"

result1 = process_input("Hello")
result2 = process_input(42)

print(result1, result2)

user = find_user()