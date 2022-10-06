from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Task Title', max_length=50)
