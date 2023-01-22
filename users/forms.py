from django import forms
from users.models import CustomUser


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'email', 'password', 'last_name')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
    #
    #     return user
    # username = forms.CharField(max_length=150)
    # email = forms.EmailField()
    # first_name = forms.CharField(max_length=150)
    # last_name = forms.CharField(max_length=150)
    # password = forms.CharField(max_length=128)
    #
    # def save(self):
    #     username = self.changed_data['username']
    #     email = self.changed_data['email']
    #     first_name = self.changed_data['first_name']
    #     last_name = self.changed_data['last_name']
    #     password = self.changed_data['password']
    #
    #     user = User.objects.create_user(
    #         username=username,
    #         last_name=last_name,
    #         email=email,
    #         first_name=first_name,
    #         password=password
    #
    #     )
    #     user.set_password(password)
    #     user.save()
    #     return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'first_name', 'email', 'profile_picture')
