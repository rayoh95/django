from django import forms
from .models import Board       # 그 전에 없던 Board 를 import 해와야 한다.

class BoardForm(forms.ModelForm):           # ModelForm 과 Form 이 있는데, Form 은 너무 노가다이다.
    class Meta:
        model = Board
        fields = ['title', 'content'] # '__all__'               #Board 중에 사용할 것을 고른다.