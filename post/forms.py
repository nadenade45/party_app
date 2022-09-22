from django import forms
from .models import Post
from accounts.models import CustomUser
from django.contrib.admin.widgets import AdminDateWidget




class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 5, 'cols': 30,
                        'placeholder': 'ここに入力してください'}
            ),
        
        }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'content',
        )
        widgets = {
            'content':forms.Textarea(
                attrs={'rows':5,'cols':30}
            ),
        }

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):#*argsはtuple型**kwargsはdict型
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():  # bootstrapで使用するform-controlクラス
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ('nickname','email','comment','birthday','avatar')
        help_texts = {
            'nickname': "ユーザーネーム",
            'email': None,
            'comment':"自己紹介",
            'birthday':"生年月日",
            
            
        }        