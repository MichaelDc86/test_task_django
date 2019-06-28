from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from django.forms import ModelForm
from mainapp.models import Blogger, PostBlog


class AdminShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = Blogger
        fields = ('username', 'name', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            # if field_name == 'password':
            #     field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class PostblogReadForm(ModelForm):
    class Meta:
        model = PostBlog
        fields = ('blogger', 'readed', 'blog', 'title', 'text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
