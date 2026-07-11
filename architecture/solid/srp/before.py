# 엔터티 
# 특정 애플리케이션 동작이나 외부 관심사와 무관하게 가장 일반적이고 고수준의 규칙만 담은 핵심 비즈니스 객체
#

class User:
    def __init__(self, user_id: str, username: str, email: str):
        self.user_id = user_id;
        self.username = username;
        self.email = email;
        self.posts = [];

    def create_post(self, content: str) -> dict:
        post = {
            "id": len(self.posts) + 1,
            "content": content,
            "likes": 0
        };

        self.posts.append(post)
        return post
    
    def get_timeline(self) -> list:
        pass

    def update_profile(self, new_username: str = None, new_email: str = None):
        if new_username:
            self.username = new_username;

        if new_email:
            self.email = new_email;