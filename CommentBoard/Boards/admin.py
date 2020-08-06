from django.contrib import admin
from .models import Board, Comment

# Register your models here.
admin.site.register(Board)
admin.site.register(Comment)

# class Board(admin.ModelAdmin):
#     list_display = ("title", "content", "author")
#     search_fields = ['title = field1', 'content = field2' 'author__name']
