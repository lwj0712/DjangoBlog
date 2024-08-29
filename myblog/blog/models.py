from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)  # 댓글 삭제 여부

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='likes', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.post:
            return f'{self.user} liked post {self.post}'
        return f'{self.user} liked comment {self.comment}'