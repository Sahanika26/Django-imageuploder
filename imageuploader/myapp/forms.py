from django import forms
from myapp.models import Image
from myapp.models import Contact


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image  # Specify the model that the form corresponds to
        fields = '__all__'  # Or you can specify fields explicitly like: ['field1', 'field2', ...]
        labels = {'photo': ' '}



class ContactForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(label='Name', max_length=100)
        email = forms.EmailField(label='Email', max_length=100)
        message = forms.CharField(label='Message', widget=forms.Textarea)

