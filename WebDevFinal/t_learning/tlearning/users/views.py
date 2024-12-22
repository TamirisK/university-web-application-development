from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View


# Login view
class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')

    def get(self, request):
        return render(request, 'users/login.html')


# Logout view
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')  # Redirect to login page after logout


# Register view
class RegisterView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        else:
            form = UserCreationForm()

    def get(self, request):
        return render(request, 'users/register.html', {'form': form})
