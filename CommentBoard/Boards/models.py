from django.db import models

# Create your models here.
class Board(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField()


class Comment(models.Model):

    # post = models.ForeignKey(Board)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)   #, related_name='comments'
    author = models.CharField(max_length = 10)
    message = models.TextField()

