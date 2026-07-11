class PostManager:
    def __init__(self):
        self.posts = []

    def create_post(self, user, content: str) -> dict:
        post = {
            "id": self.generate_post_id(),
            "user_id": user.user_id,
            "content": content,
            "likes": 0,
        }

        self.posts.append(post)
        return post

    def generate_post_id(self) -> int:
        return len(self.posts) + 1
