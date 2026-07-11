# 의존성 역전 원칙?

class A:
    def __init__(self):
        self.b = B()

class B:
    def __init__(self):
        pass


# ------
# 구체적인 예제

class UserEntity:
    def __init__(self, user_id: str):
        self.user_id = user_id
        # 저수준 모듈에 대한 직접 의존
        self.database = MySQLDatabase()

    def save(self):
        self.database.insert(
            "users",
            {
                "id": self.user_id
            }
        )

class MySQLDatabase:
    def insert(self, table: str, data: dict):
        print(f"Inserting {data} into {table} table in MySQL")

