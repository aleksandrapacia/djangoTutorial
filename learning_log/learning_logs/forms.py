from django import forms
from .models import Topic , Entry

# here we create a model form for user to input their entries
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}