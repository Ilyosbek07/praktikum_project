from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import message
from django.views.generic import ListView

from books.models import Book
from users.models import CustomUser
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreateForm, UserUpdateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        # first_name = request.POST['first_name']
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # last_name = request.POST['last_name']
        # user = User.objects.create(
        #     username=username,
        #     first_name=first_name,
        #     email=email,
        #     password=password,
        #     last_name=last_name
        # )
        # user.set_password(password)
        # user.save()
        # return redirect('user:login')
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('landing_page')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, 'users/login.html', {'login_form': login_form})


class BaseTemplate(View):
    def get(self, requests):
        return render(requests, 'base.html', {})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html', {"user": request.user})


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile_edit.html', {'form': user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, 'Success')

            return redirect('users:profile')
        return redirect(request, 'users/profile_edit.html', {'form': user_update_form})
