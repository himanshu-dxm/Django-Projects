from django.forms import ModelForm
from .models import Todo
class TODOForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description','priority']
        