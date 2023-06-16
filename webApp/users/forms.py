from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class CreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        label='Подразделение'
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('groups','username')
