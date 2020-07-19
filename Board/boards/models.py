from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # def __str__(self):
    #     return f'게시글 제목 : {self.title}'
# Create your models here.