from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from users.models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):

    password = ReadOnlyPasswordHashField()

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')
