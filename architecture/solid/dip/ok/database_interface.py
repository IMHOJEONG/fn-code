from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def insert(self, table: str, data: dict):
        pass

class UserEntity:
    def __init__(self, user_id: str, database: DatabaseInterface):
        self.user_id = user_id
        self.database = database
    def save(self):
        self.database.insert(
            "users",
            {
                "id": self.user_id
            }
        );

class MySQLDatabase(DatabaseInterface):
    def insert(self, table: str, data: dict):
        print(f"MySQL의 {table} 테이블에 {data} 삽입 중")

class PostgreSQLDatabase(DatabaseInterface):
    def insert(self, table: str, data: dict):
        print(f"PostgreSQL의 {table} 테이블에 {data} 삽입 중")

mysql_db = MySQLDatabase();
user = UserEntity("123", mysql_db)
user.save()


postgres_db = PostgreSQLDatabase();
another_user = UserEntity("456", postgres_db)
another_user.save()