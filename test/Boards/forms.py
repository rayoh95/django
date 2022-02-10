from django import forms
from .models import Boards  

class BoardForm(forms.ModelForm):          
    class Meta:
        model = Boards
        fields = ['title', 'content'] 