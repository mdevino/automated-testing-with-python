'''
    Key takeaways
    * test methods should always start with 'test_'

'''

from unittest import TestCase
from blog_app.main.post import Post


class PostTest(TestCase):
    def test_create_post(self):
        post = Post('Test', 'Test Content')
        self.assertEqual('Test', post.title)
        self.assertEqual('Test Content', post.content)

    def test_json(self):
        post = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
        self.assertDictEqual(expected, post.json())
