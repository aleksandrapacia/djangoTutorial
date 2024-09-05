from django import forms
from .models import Topic 

# here we create a model form for user to input their entries
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text': ''}
        