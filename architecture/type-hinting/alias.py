UserDict = dict[str, str]
UserList = list[UserDict]

def process_users(users: UserList) -> None:
    for user in users:
        print(f"Processing user: {user['name']}")

users: UserList = [
    {"name": "Alice"},
    {"name": "test-ho"}
]

process_users(users)