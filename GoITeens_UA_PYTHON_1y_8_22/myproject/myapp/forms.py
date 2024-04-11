from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, TableReservation, Table


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ReservedForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    table_number = forms.IntegerField()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']


class TableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ['first_name', 'last_name', 'phone_number', 'table_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table_number'].queryset = Table.objects.all()
        self.fields['table_number'].label_from_instance = lambda obj: str(obj.name)