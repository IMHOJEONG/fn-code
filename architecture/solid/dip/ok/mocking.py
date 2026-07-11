from database_interface import DatabaseInterface, UserEntity

class MockingDatabase(DatabaseInterface):
    def __init__(self):
        self.inserted_data = [];

    def insert(self, table: str, data: dict):
        self.inserted_data.append((table, data))

    
mock_db = MockingDatabase()
user = UserEntity("test_user", mock_db);
user.save()
assert mock_db.inserted_data == [
    ("users", {
        "id": "test_user"
    })
]
