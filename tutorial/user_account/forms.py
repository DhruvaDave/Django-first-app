from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import UserProfile,Message


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = ['user_messsage', 'user_id']
        exclude = []

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        print("--------------init------------",user)
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['user_id']=forms.ModelChoiceField(queryset=User.objects.filter(username=user))
        self.fields['user_messsage']=forms.CharField(max_length=15)
        print("-----------self.fields---------",self.fields)





class MsgEditForm(forms.Form):
    # template_name='/something/else'
    user_messsage = forms.CharField(max_length=300)
    

    class Meta:
        model = Message
        fields = (
            'user_messsage',
            'user_id'
        )
