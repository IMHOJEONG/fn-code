def get_user(user_id: int) -> dict:
    return {
        "id": user_id,
        "name": "test-ho",
        "email": "test-ho@naver.com"
    }

def send_email(user: dict, subject: str) -> None:
    print(f"Sending email to {
        user['email']
    } with subject: {subject}");

user = get_user(123)
send_email(user, "TEST")