from utils.base_for_tests.base_for_login import BaseLoginAuthor
from social_echo.models import Posts


class BaseCreatePost(BaseLoginAuthor):
    def setUp(self) -> None:
        super().setUp()

        self.post = Posts.objects.create(
            title='I am a test title',
            message='I am a test message',
            author=self.author_user.author,
        )

    def create_post(self,
                    title='I am a test title2',
                    message='I am a test message2',):
        self.post = Posts.objects.create(
            title=title,
            message=message,
            author=self.author_user.author,
        )
