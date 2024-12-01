from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Post, Comment

class BlogProjectTestCase(TestCase):
  # # Base Set Up
  # def setUp(self):
  #   self.user1 = User.objects.create_user(username='user1', password='password1')
  #   self.user2 = User.objects.create_user(username='user2', password='password2')

  #   self.token1 = Token.objects.create(user=self.user1)
  #   self.token2 = Token.objects.create(user=self.user2)

  #   self.client = APIClient()

  #   self.post = Post.objects.create(
  #     title="Test Post 1",
  #     content="This is a test post 1.",
  #     author=self.user1,
  #     status='published'
  #   )

  #   self.comment = Comment.objects.create(
  #     post=self.post,
  #     content="This is a comment for test post 2.",
  #     author=self.user2
  #   )

  # # Task 4
  # # Posts Endpoints
  # def test_list_posts(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   response = self.client.get('/api/posts/')
  #   self.assertEqual(response.status_code, 200)
  #   self.assertEqual(len(response.data), 1)

  # def test_create_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   data = {
  #     "title": "New Post",
  #     "content": "Content of the new post.",
  #     "status": "draft"
  #   }
  #   response = self.client.post('/api/posts/', data)
  #   self.assertEqual(response.status_code, 201)
  #   self.assertEqual(response.data['title'], "New Post")

  # def test_retrieve_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   response = self.client.get(f'/api/posts/{self.post.id}/')
  #   self.assertEqual(response.status_code, 200)
  #   self.assertEqual(response.data['title'], "Sample Post")

  # def test_update_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   data = {"title": "Updated Title"}
  #   response = self.client.put(f'/api/posts/{self.post.id}/', data)
  #   self.assertEqual(response.status_code, 200)
  #   self.assertEqual(response.data['title'], "Updated Title")

  # def test_delete_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   response = self.client.delete(f'/api/posts/{self.post.id}/')
  #   self.assertEqual(response.status_code, 204)

  # # Task 4
  # # Comments Endpoints
  # def test_list_comments_for_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   response = self.client.get(f'/api/posts/{self.post.id}/comments/')
  #   self.assertEqual(response.status_code, 200)
  #   self.assertEqual(len(response.data), 1)

  # def test_create_comment_for_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
  #   data = {"content": "New comment"}
  #   response = self.client.post(f'/api/posts/{self.post.id}/comments/', data)
  #   self.assertEqual(response.status_code, 201)
  #   self.assertEqual(response.data['content'], "New comment")

  # # Task 6
  # # Permissions
  # def test_only_author_can_edit_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
  #   data = {"title": "Unauthorized Update"}
  #   response = self.client.put(f'/api/posts/{self.post.id}/', data)
  #   self.assertEqual(response.status_code, 403)

  # def test_only_author_can_delete_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
  #   response = self.client.delete(f'/api/posts/{self.post.id}/')
  #   self.assertEqual(response.status_code, 403)

  # # Other Tests
  # def test_create_post_without_authentication(self):
  #   response = self.client.post('/api/posts/', {"title": "Unauthorized Post"})
  #   self.assertEqual(response.status_code, 401)

  # def test_get_nonexistent_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
  #   response = self.client.get('/api/posts/9999/')
  #   self.assertEqual(response.status_code, 404)

  # def test_create_comment_for_nonexistent_post(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
  #   response = self.client.post('/api/posts/9999/comments/', {"content": "Invalid comment"})
  #   self.assertEqual(response.status_code, 404)

  # Exercise 2
  # Task 1
  def test_post_with_comments_includes_nested_comments(self):
    self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
    response = self.client.get(f'/api/posts/{self.post.id}/')
    self.assertEqual(response.status_code, 200)
    self.assertIn('comments', response.data)
    self.assertEqual(len(response.data['comments']), 1)
    self.assertEqual(response.data['comments'][0]['content'], "This is a comment.")

  # Task 2
  def test_v1_posts(self):
    response = self.client.get('/api/v1/posts/')
    self.assertEqual(response.status_code, 200)

  def test_v2_posts(self):
    response = self.client.get('/api/v2/posts/')
    self.assertEqual(response.status_code, 200)

  # # Task 3
  # def setUp(self):
  #   self.client = APIClient()
  #   self.user = User.objects.create_user(username='testuser', password='password')
  #   self.token = 'Token ' + self.user.auth_token.key

  # def test_anonymous_throttling(self):
  #   for _ in range(11): 
  #     response = self.client.get('/api/v1/posts/')
  #   self.assertEqual(response.status_code, 429)

  # def test_authenticated_throttling(self):
  #   self.client.credentials(HTTP_AUTHORIZATION=self.token)
  #   for _ in range(101):
  #     response = self.client.get('/api/v1/posts/')
  #   self.assertEqual(response.status_code, 429)

