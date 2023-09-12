from django.test import TestCase
from django.contrib.auth import get_user_model
from blogs.models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='testuser', 
            email='test@email.com',
            password='secret'
            )
        cls.post=Post.objects.create(
            title='test title',
            body='test body',
            author =cls.user,
        )
    def test_post_model(self):
        self.assertEqual(self.post.title,'test title')
        self.assertEqual(self.post.body,'test body')
        self.assertEqual(self.post.author.username,'testuser')
        self.assertEqual(self.post.get_absolute_url(),'/blog/1/')