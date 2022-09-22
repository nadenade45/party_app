from django.db import models
from django.conf import settings

class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='オーナー', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'posts'
        ordering = ["-created_at"]