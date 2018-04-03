from django import forms
from .models import Project, Module, Activity

class NewProjectForm(forms.ModelForm):
    description = forms.CharField(
                              widget=forms.Textarea(
                                                    attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
                                                    ),
                              max_length=4000,
                              help_text='The max length of the text is 4000.'
                              )

    class Meta:
        model = Module
        fields = ['name', 'description', 'submission_deadline']

class NewModuleForm(forms.ModelForm):
    description = forms.CharField(
                                  widget=forms.Textarea(
                                                        attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
                                                        ),
                                  max_length=4000,
                                  help_text='The max length of the text is 4000.'
                                  )
        
    class Meta:
        model = Module
        fields = ['name', 'description', 'submission_deadline', 'status']
